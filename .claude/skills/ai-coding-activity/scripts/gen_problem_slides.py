"""문제지 md 여러 개를 학습활동 덱의 「문제 → 입출력 예시」 쪽으로 바꾼다.

사용: python3 gen_problem_slides.py <문제 폴더> <문제 번호 목록(쉬운 순, 쉼표)> <첫 문제의 순번> <첫 문제의 절 번호> <출력 md>
예:   python3 gen_problem_slides.py "programmers_sql/[LAB-02] 데이터 조회하기" 59034,59403 2 5 /tmp/problems.md
      → 「## #05. 문제 2 — …」부터 만든다. 출력 파일의 내용을 덱의 「감사합니다」 쪽 앞에 붙여 넣는다.

- 문제 쪽: 왼쪽에 테이블 설명, 오른쪽에 구조표, 아래에 「문제」 상자(tag 에 수준 · 문제 번호)
- 입출력 예시 쪽: 예상 높이가 500px 을 넘으면 「입출력 예시 (1)」 · 「(2)」 로 나눈다. 8행이 넘는 표는 옆으로 나누거나 여러 조각으로 쪼갠다
- 출처 · 라이선스 문장("본 문제는 Kaggle의 …")은 빼고 옮긴다
- 높이는 글자 수로 어림한 값이다. 실제 넘침은 measure_overflow.py 로 잰다(사용자가 요청할 때만)
"""
import os,re,sys,math,unicodedata
SRC=sys.argv[1]; ORDER=sys.argv[2].split(","); FIRST_PN=int(sys.argv[3]); FIRST_SEC=int(sys.argv[4]); OUT=sys.argv[5]
FULL=1136; HALF=545; ROW=45
def tw(t):  # 글자 폭 추정(px)
    t=t.replace('`','')
    return sum(19 if ord(c)>0x2E80 else 10.5 for c in t)
def blocks(body):
    out=[]
    for b in re.split(r'\n\s*\n',body.strip()):
        b=b.strip('\n')
        if not b.strip(): continue
        kind='table' if b.lstrip().startswith('|') else 'list' if b.lstrip().startswith('- ') else 'p'
        out.append((kind,b))
    return out
def trows(b): 
    L=[l for l in b.split('\n') if l.strip()]
    return L[0],L[1],L[2:]
def cells(l): return [c.strip() for c in l.strip().strip('|').split('|')]
def twidth(b):
    h,_,rows=trows(b); cols=len(cells(h)); w=0
    for i in range(cols):
        w+=max([tw(cells(h)[i])]+[tw(cells(r)[i]) if i<len(cells(r)) else 0 for r in rows])+30
    return w,cols
def h_p(b,width=FULL): return sum(max(1,math.ceil(tw(l)/width)) for l in b.split('\n'))*34+18
def h_table(b,width=FULL):
    h,_,rows=trows(b); w,_=twidth(b); k=1 if w<=width else math.ceil(w/width)
    return (len(rows)*k+1)*ROW+20
def render_table(b):
    """표 하나를 (높이, md) 조각 목록으로. 긴 표는 옆으로 나누거나 여러 조각으로 쪼갠다."""
    h,sep,rows=trows(b); w,cols=twidth(b); n=len(rows)
    if n<=8: return [(h_table(b),b)]
    k=3 if (cols==1 and w<=FULL/3-40) else 2
    if w<=FULL/k-30:
        per=math.ceil(n/k); parts=[rows[i:i+per] for i in range(0,n,per)]
        md='<Grid cols="%d" align="start">\n'%k+''.join('<div>\n\n'+'\n'.join([h,sep]+p)+'\n\n</div>\n' for p in parts)+'</Grid>'
        return [((per+1)*ROW+30,md)]
    per=math.ceil(n/math.ceil(n/8)); res=[]
    for i in range(0,n,per):
        part='\n'.join([h,sep]+rows[i:i+per]); res.append((h_table(part),part))
    return res
files={re.match(r'Lv\d-([A-Z0-9]+)-',unicodedata.normalize("NFC",f)).group(1):f for f in os.listdir(SRC) if f.endswith(".md") and re.match(r'Lv\d-',unicodedata.normalize("NFC",f))}
out=[]; report=[]
for idx,num in enumerate(ORDER):
    pn=FIRST_PN+idx; sec=FIRST_SEC+idx; tag=f"#{sec:02d}"
    s=open(os.path.join(SRC,files[num]),encoding="utf-8").read()
    title=re.match(r'# \[Lv\.(\d)\] (.*)',s); lv,name=title.group(1),title.group(2).strip()
    m_url=re.search(r'- 링크: (https?://\S+)',s); url=m_url.group(1) if m_url else ''
    custom=not num.isdigit()   # L05P1 처럼 직접 만든 문제
    secs={m.group(1):m.group(2) for m in re.finditer(r'^## (\S+)\n(.*?)(?=^## |\Z)',s,flags=re.S|re.M)}
    assert not re.search(r'^#{3,} ',s,flags=re.M),num
    desc=blocks(secs.get('테이블','')); prob=blocks(secs['문제']); ex=blocks(secs.get('예시',''))
    # 출처 · 라이선스 문장("본 문제는 Kaggle의 …")은 싣지 않는다. 학생이 프로그래머스 페이지에서 확인할 수 있다
    drop=lambda bs:[(k,b) for k,b in bs if not b.startswith('본 문제는')]
    desc,prob,ex=drop(desc),drop(prob),drop(ex)
    if not desc:  # 문제 절 안에 구조표가 있음
        # 구조표(머리행이 NAME | TYPE 또는 Column name)가 여러 개면 마지막 구조표까지 테이블 설명으로 본다
        isstruct=lambda b: re.match(r'\|\s*(NAME|Column name)\s*\|\s*TYPE',b,flags=re.I) is not None
        st=[i for i,(k,b) in enumerate(prob) if k=='table' and isstruct(b)]
        ti=st[-1] if st else [i for i,(k,_) in enumerate(prob) if k=='table'][0]
        desc=prob[:ti+1]; prob=prob[ti+1:]
    if not ex:    # 예시 절이 없으면 결과 표부터 예시로 넘김
        ti=[i for i,(k,_) in enumerate(prob) if k=='table'][0]
        ex=prob[ti:]; prob=prob[:ti]
        k,last=prob[-1]; m=re.match(r'(.*작성해주세요\.)\s*(SQL을 실행하면.*)$',last,flags=re.S)
        if m: prob[-1]=(k,m.group(1)); ex=[('p',m.group(2))]+ex
    struct=[b for k,b in desc if k=='table']; assert struct,num
    # 테이블이 여러 개(JOIN 문제)면 테이블마다 앞의 설명 문단과 묶어 나란히 둔다
    groups=[]; buf=[]
    for k,b in desc:
        if k=='table': groups.append((buf,b)); buf=[]
        else: buf.append(b)
    left=[b for k,b in desc if k!='table']
    task=' '.join(b.replace('\n',' ') for k,b in prob if k!='table'); assert all(k!='table' for k,_ in prob),num
    hl=sum(h_p(b,HALF) for b in left); hr=h_table(struct[0],HALF)
    hc=45+40+max(1,math.ceil(tw(task)/(FULL-60)))*34
    est=190+max(hl,hr)+20+hc
    chips=False; est-=50; tight=est>655
    page=("---\nclass: tight\n---\n\n" if tight else "---\n\n")+f"## {tag}. 문제 {pn} — {name}\n\n"
    if chips: page+=f'<p><Chip color="py">Level {lv}</Chip> <Chip kind="outline" color="py">프로그래머스 {num}</Chip> {url}</p>\n\n'
    if len(struct)==1:
        page+='<Grid cols="2" align="start">\n<div>\n\n'+'\n\n'.join(left)+'\n\n</div>\n<div>\n\n'+struct[0]+'\n\n</div>\n</Grid>\n\n'
    else:
        # 테이블이 여러 개면 한 화면에 들어가지 않는다: 문제 쪽에는 설명 문단과 문제 상자만 두고,
        # 바로 뒤 「테이블 구조」 쪽에 구조표를 테이블 이름과 함께 나란히 둔다
        page+='\n\n'.join(left)+'\n\n'
        names=[]
        for ps,t in groups:
            m=re.search(r'`([A-Z][A-Z0-9_]+)`',' '.join(ps)); names.append(m.group(1) if m else '')
        struct_page=f"---\n\n### {tag}-1. 테이블 구조\n\n"+f'<Grid cols="{len(groups)}" align="start">\n'+''.join(f'<div>\n\n<div class="kicker">{n}</div>\n\n{t}\n\n</div>\n' for n,(ps,t) in zip(names,groups))+'</Grid>\n\n'
    tagattr='' if chips else (f' tag="직접 만든 문제"' if custom else f' tag="Level {lv} · 프로그래머스 {num}"')
    page+=f'<Callout kind="plain" color="py" icon="📝" title="문제"{tagattr}>\n\n{task}\n\n</Callout>\n\n'
    out.append(page); report.append((tag,'문제',est,'tight' if tight else ''))
    off=0
    if len(struct)>1: out.append(struct_page); report.append((f"{tag}-1",'테이블 구조',0,'')); off=1
    # 예시 쪽
    pieces=[]
    for k,b in ex:
        if k=='table': pieces+=render_table(b)
        else: pieces.append((h_p(b),b))
    pages=[[]]; used=0   # pages 원소: (높이, md, 표 여부)
    for i,(h,md) in enumerate(pieces):
        is_t=md.lstrip().startswith('|') or md.startswith('<Grid')
        if pages[-1] and used+h>500:
            carry=[]
            # 표를 소개하는 문단이 쪽 끝에 홀로 남지 않게 다음 쪽으로 함께 넘긴다
            if is_t and len(pages[-1])>1 and not pages[-1][-1][2]: carry=[pages[-1].pop()]
            pages.append(carry); used=sum(x[0] for x in carry)
        pages[-1].append((h,md,is_t)); used+=h
    clean=[([x[1] for x in pg],sum(x[0] for x in pg)) for pg in pages]
    for j,(mds,hh) in enumerate(clean,1):
        t='입출력 예시' if len(clean)==1 else f'입출력 예시 ({j})'
        out.append(f"---\n\n### {tag}-{j+off}. {t}\n\n"+'\n\n'.join(mds)+'\n\n'); report.append((f"{tag}-{j+off}",t,142+hh,''))
# Slidev 코드 강조기에 없는 언어(dbml 등)는 쪽 전체를 깨뜨리므로 text 로 바꾼다
open(OUT,"w",encoding="utf-8").write(re.sub(r'^```dbml$','```text',''.join(out),flags=re.M))
for r in report: print(r)
print("쪽 수:",len(report))

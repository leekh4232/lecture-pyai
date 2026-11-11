"""입출력 예시 (k) 쪽을 앞쪽과 합쳐 보고, 넘치지 않으면 합친 상태로 둔다. 합친 뒤 (k) 번호를 다시 매긴다."""
import re, subprocess, sys, time, urllib.request
from playwright.sync_api import sync_playwright

DECK = sys.argv[1]
PORT = 3187


def pages(text):
    """쪽 번호 -> (시작 줄, 끝 줄, 첫 제목)."""
    s = text.split('\n'); fence = False; seps = []
    for i, l in enumerate(s):
        if l.startswith('```'): fence = not fence
        if l == '---' and not fence: seps.append(i)
    starts = [seps[0]]
    for a in seps[1:]:
        prev = starts[-1]; between = s[prev + 1:a]
        if between and (a - prev) < 12 and all((':' in x or not x.strip()) for x in between) \
                and not any(x.startswith(('#', '<', '|', '-')) for x in between):
            continue
        starts.append(a)
    out = []
    for n, a in enumerate(starts):
        b = starts[n + 1] if n + 1 < len(starts) else len(s)
        out.append(next((x for x in s[a:b] if x.startswith('#')), ''))
    return out


def merge_once(text, sec, k):
    """#sec-k 쪽을 #sec-(k-1) 쪽 끝에 붙인다. 이어지는 표의 반복 머리행은 뺀다."""
    pat = re.compile(r'\n\n---\n(?:class: \w+\n---\n)?\n### #' + sec + '-' + str(k) + r'\. 입출력 예시 \(\d\)\n\n')
    m = pat.search(text)
    if not m: return None
    before, after = text[:m.start()], text[m.end():]
    lb = before.rstrip('\n').split('\n'); la = after.split('\n')
    if lb and lb[-1].startswith('|') and len(la) > 1 and la[0].startswith('|') and la[1].startswith('| ---'):
        # 앞 표의 머리행과 같으면 머리행 두 줄을 빼고 표를 잇는다
        i = len(lb) - 1
        while i > 0 and lb[i - 1].startswith('|'): i -= 1
        if lb[i] == la[0]:
            return before.rstrip('\n') + '\n' + '\n'.join(la[2:])
    return before + '\n\n' + after


def renumber(text):
    """절마다 입출력 예시 쪽의 번호와 (k)를 다시 매긴다."""
    def fix(sec_match):
        return sec_match
    lines = text.split('\n'); cnt = {}
    heads = [(i, re.match(r'### #(\d\d)-(\d+)\. 입출력 예시( \(\d\))?$', l)) for i, l in enumerate(lines)]
    heads = [(i, m) for i, m in heads if m]
    for i, m in heads: cnt[m.group(1)] = cnt.get(m.group(1), 0) + 1
    seen = {}
    for i, m in heads:
        sec = m.group(1); seen[sec] = seen.get(sec, 0) + 1
        k = seen[sec] + (1 if f'### #{sec}-1. 테이블 구조' in text else 0)
        suffix = f' ({k})' if cnt[sec] > 1 else ''
        lines[i] = f'### #{sec}-{k}. 입출력 예시{suffix}'
    return '\n'.join(lines)


def measure(pg, n):
    pg.goto(f'http://localhost:{PORT}/{n}', wait_until='load'); time.sleep(2.5)
    return pg.evaluate("()=>document.querySelector('.over-tag')?.innerText||''")


proc = subprocess.Popen(['npx', 'slidev', DECK, '--port', str(PORT)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(90):
        try: urllib.request.urlopen(f'http://localhost:{PORT}/', timeout=2); break
        except Exception: time.sleep(1)
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={'width': 1280, 'height': 720})
        changed = True
        while changed:
            changed = False
            text = open(DECK, encoding='utf-8').read()
            for m in re.finditer(r'^### #(\d\d)-(\d+)\. 입출력 예시 \(\d\)$', text, re.M):
                sec, k = m.group(1), int(m.group(2))
                if k < 2 or f'### #{sec}-{k - 1}. 테이블 구조' in text: continue
                new = merge_once(text, sec, k)
                if new is None: continue
                open(DECK, 'w', encoding='utf-8').write(new); time.sleep(3)
                heads = pages(new)
                n = next(i + 1 for i, h in enumerate(heads) if h.startswith(f'### #{sec}-{k - 1}.'))
                tag = measure(pg, n)
                if tag:   # 넘침 → 되돌림
                    open(DECK, 'w', encoding='utf-8').write(text); time.sleep(3)
                    print(f'#{sec}-{k - 1}+{k}: 넘침 {tag} → 그대로 둠')
                else:
                    print(f'#{sec}-{k - 1}+{k}: 합침')
                    open(DECK, 'w', encoding='utf-8').write(renumber(new)); time.sleep(2)
                    changed = True
                    break
        # 최종 전체 측정
        heads = pages(open(DECK, encoding='utf-8').read())
        time.sleep(3)
        for n in range(1, len(heads) + 1):
            tag = measure(pg, n)
            if tag: print('넘침', n, heads[n - 1], tag)
        print('쪽 수', len(heads))
        b.close()
finally:
    proc.terminate(); subprocess.run(['pkill', '-f', f'port {PORT}'])

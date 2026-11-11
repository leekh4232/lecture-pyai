"""학습활동 덱의 모범답안 md 를 만든다. 쿼리는 myschool 에서 실제로 실행한 결과만 싣는다.

사용: python3 gen_answer_key.py <설정 .py> <출력 md>

설정 파일은 파이썬 파일이며 아래 이름을 정의한다.
- DECK: 덱 파일 이름(설명 문장에 씀)
- UNIT: 맥락 문장의 단원 이름. 예: "SQL 함수"  → "SQL 함수를 배우는 중이야."
- RANGE: 방향 묻기 프롬프트의 제약 한 줄. 예: "… 범위 안에서만"
- NOTES: (쓰지 않음, 일러두기 절은 넣지 않음)
- MEAN: {테이블: "컬럼 뜻 · …"}
- P: 문제 목록. 각 항목은 dict
    title, level(숫자 또는 None), pid(프로그래머스 번호 또는 None = 직접 만든 문제),
    tables(목록), sql, official(정답 파일 쿼리, 다르면 결과가 같은지 확인), understand, key, wrong, mistake

규칙(LAB-02에서 사용자와 정함)
- 상위 한 건은 LIMIT 0, 1, '다르다'는 != 로 씀
- 테이블 구조는 DESC 결과(테두리 표)를 그대로 붙임
- 기대한 결과 · 실제 결과는 행 수와 두 결과가 처음 달라지는 곳의 행을 적음. 에러는 원문
"""
import runpy, subprocess, sys

DB = ["mariadb", "-uroot", "-p1234", "-P9901", "-h127.0.0.1", "--default-character-set=utf8mb4", "myschool"]
cfg = runpy.run_path(sys.argv[1])


def run(sql, table=False):
    p = subprocess.run(DB + (["-t"] if table else ["-N", "-B"]) + ["-e", sql], capture_output=True, text=True)
    if p.returncode:
        err = next(l for l in p.stderr.splitlines() if l.startswith("ERROR"))
        return None, err.replace(" at line 1", "")
    if table:
        return p.stdout.rstrip("\n"), None
    return ([r.split("\t") for r in p.stdout.rstrip("\n").split("\n")] if p.stdout.strip() else []), None


def describe(rows, other, err):
    if err:
        return err
    n = len(rows)
    if n == 0:
        return "0행 (결과가 비어 있음)"
    i = 0
    while other is not None and i < min(n, len(other)) and rows[i] == other[i]:
        i += 1
    if i >= n:
        i = max(n - 2, 0)
    part = rows if n <= 2 else rows[i:i + 2]
    where = "" if n <= 2 else (f", {i + 1}번째 행부터: " if i else ", 앞 2행: ")
    return f"{n}행" + (where or " ") + " / ".join("(" + ", ".join(r) + ")" for r in part) + (" …" if i + 2 < n else "")


def structure(tables):
    out = []
    for t in tables:
        d, e = run(f"DESC {t};", table=True)
        assert not e, e
        out.append(f"{t} 테이블 구조:\n{d}")
    return "\n".join(out)


P = cfg["P"]
o = []
w = o.append
w(f"# {cfg['DECK'].split('(')[0].strip()} 모범답안\n")
w(f"「{cfg['DECK']}」 덱의 문제 {len(P)}개에 대한 정답 SQL과, 두 템플릿(방향 묻기 · 원인 묻기)을 빈칸 없이 채운 프롬프트를 담았다.\n")

for n, p in enumerate(P, 1):
    good, e = run(p["sql"]); assert not e, (n, e)
    if p.get("official"):
        off, e = run(p["official"]); assert not e and off == good, (n, "정답 파일과 결과가 다름", e)
    bad, berr = run(p["wrong"])
    assert berr or bad != good, (n, "틀린 쿼리 결과가 정답과 같음")
    struct = structure(p["tables"])
    w(f"## 문제 {n}. {p['title']}\n")
    if p.get("pid"):
        w(f"- Level {p['level']} · 프로그래머스 {p['pid']} · https://school.programmers.co.kr/learn/courses/30/lessons/{p['pid']}\n")
    else:
        w("- 직접 만든 문제 · 수업용 DB `myschool`의 테이블을 씀\n")
    w("### 정답 SQL\n")
    w("```sql\n" + p["sql"] + "\n```\n")
    w(f"- 결과: {len(good)}행")
    w(f"- 풀이 핵심: {p['key']}\n")
    w("### 방향 묻기 프롬프트\n")
    w("````md")
    w(f"## 맥락\nSQL {cfg['UNIT']}를 배우는 중이야. 쿼리는 내가 직접 쓸게.\n")
    w(f"## 상황\n{struct}")
    for t in p["tables"]:
        w(f"- {t} 컬럼 뜻: {cfg['MEAN'][t]}" if len(p["tables"]) > 1 else f"- 컬럼 뜻: {cfg['MEAN'][t]}")
    w(f"- 내가 이해한 문제: {p['understand']}\n")
    w("## 질문\n내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.\n")
    w(f"## 제약\n- {cfg['RANGE']}\n")
    w("## 출력 형식\n| 순서 | 절 | 하는 일 | 표로")
    w("````\n")
    w("### 원인 묻기 프롬프트\n")
    w(f"- 가정한 실수: {p['mistake']}\n")
    w("````md")
    w(f"## 맥락\nSQL {cfg['UNIT']}를 배우는 중이야. 쿼리는 내가 고칠게.\n")
    w(f"## 상황\n{p['understand'].split('. ')[0]}하려고 해.\n{struct}")
    w("```sql\n" + p["wrong"] + "\n```")
    w(f"- 기대한 결과: {describe(good, bad, None)}")
    w(f"- 실제 결과: {describe(bad, good, berr)}\n")
    w("## 질문\n기대와 다른 이유를 찾게 확인할 곳을 알려줘.\n")
    w("## 출력 형식\n| 확인할 곳 | 이유 | 표로")
    w("````\n")

open(sys.argv[2], "w", encoding="utf-8").write("\n".join(o).rstrip() + "\n")
print("ok", len(P))

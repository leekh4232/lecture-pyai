---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 파일입출력 — CSV 읽고 집계하기
layout: cover
---

# CSV 읽고 집계하기 — 파일에서 숫자까지

covid19.csv를 읽어 합계 · 비율 · 최댓값 · 연도별 집계를 구하고, 받은 코드를 내 데이터로 검증하는 연습

<p class="sub">[LAB-08] 파일입출력 3 · ITWILL · {teacher} 강사</p>

<!--
「open함수의 사용」「CSV파일 다루기」를 마친 뒤 하는 ② 답 받기 단계 두 번째 실습. 지침은 「ChatGPT 지침(답 받기).md」가 들어가 있다고 전제한다.
결과물: A-1 ~ A-4 코드(4단 확인 표시), seoul_yearly.csv, 템플릿 ⑲.
새 템플릿은 ⑲ 하나. ⑰ 코드 받기 · ⑱ 내 코드 고쳐 받기는 LAB-07에서 만들었으므로 다시 가르치지 않고 번호로만 부른다.
-->

---

## #01. 오늘의 진행 — 답 받기 단계, 2교시

<Timeline color="ai">
<li><b>A 구현 · 40분</b>15분 직접 시도 → 답 받기 → 4단 확인</li>
<li><b>B 결과가 이상할 때 · 25분</b>"AI 답"의 함정 찾기</li>
<li><b>C 에러 수정 · 25분</b>받은 코드를 내 노트북에 붙였을 때</li>
<li><b>D 정리 · 10분</b>템플릿 ⑲ 추가 · 오늘 고친 실수 한 줄</li>
</Timeline>

<Callout kind="real" title="오늘의 규칙">

- 지침은 「ChatGPT 지침(답 받기).md」. 코드를 받되, 받은 코드는 내가 검증한다
- 문제마다 **15분 직접 시도**. 막힌 코드를 `## 내 시도`에 붙여 답을 받는다
- 프롬프트는 여섯 섹션. `## 맥락` `## 상황` `## 내 시도` `## 질문` `## 제약` `## 출력 형식`
- 정답은 내 노트북 실행 결과

</Callout>

<!--
시작 전에 개인 맞춤 설정의 지침이 「ChatGPT 지침(답 받기).md」인지 확인한다. 노트북과 같은 폴더에 covid19.csv가 있는지도 이때 확인한다(C의 FileNotFoundError를 수업 초반에 겪지 않게).
템플릿 ⑰ · ⑱은 LAB-07의 것을 「내 프롬프트 템플릿.md」에서 꺼내 쓴다.
-->

---
layout: cards
cols: 4
---

## #02. 받은 코드 4단 확인 — 넷을 통과해야 내 코드

<Tile kind="soft" color="py" tag="① 실행" title="정답과 대조">
내 노트북에서 실행해 정답과 같은 값이 나오는지
</Tile>

<Tile kind="soft" color="ai" tag="② 범위" title="배운 문법인지">
`csv` 모듈 · 리스트 컴프리헨션 · lambda처럼 배우지 않은 문법이 없는지
</Tile>

<Tile kind="soft" color="ok" tag="③ 설명" title="줄마다 말로">
줄마다 무슨 일을 하는지 막힘없이 설명되는지
</Tile>

<Tile kind="soft" color="yellow" tag="④ 변형" title="AI 없이 풀기">
조건 하나를 바꾼 변형 문제를 직접 풀어 정답이 나오는지
</Tile>

<Core color="ai">하나라도 통과하지 못하면 아직 AI의 코드. 배우지 않은 문법이 나오면 범위 안으로 다시 요청한다</Core>

<!--
LAB-07에서 처음 쓴 4단 확인을 다시 상기만 한다. 오늘 특히 ② 범위에서 자주 걸리는 것이 csv 모듈이다. AI는 CSV를 보면 csv 모듈부터 꺼낸다. 교안은 split 방식이므로 범위 밖이다.
-->

---

## #03. `## 제약`에 적는 범위

| 단원 | 범위 |
|:--|:--|
| 1 open함수의 사용 | 절대 · 상대 경로, open · read · write, with 문, readlines |
| 2 CSV파일 다루기 | 리스트 · 딕셔너리를 CSV로 저장, CSV를 파이썬 데이터로 변환(split), encoding |
| 이전 LAB | 조건문 · 반복문 · 리스트 · 문자열 · 딕셔너리 · 함수 · 예외처리 |

<Callout kind="warn" title="AI가 자주 꺼내는 범위 밖 도구">
<code>csv</code> 모듈 · <code>pandas</code>. 오늘은 <code>open</code> · <code>with</code> · <code>readlines</code> · <code>split</code>만 쓴다
</Callout>

<!--
pandas는 LAB-10 이후에 배운다. 오늘은 pandas가 한 줄로 하는 일을 직접 해 보는 시간이라는 점을 짧게 말해 둔다.
-->

---
layout: infographic
---

## #04. 연습 데이터 — 교안의 covid19.csv

<p><Chip color="py">날짜</Chip><Chip color="ai">서울시 일일 확진</Chip><Chip color="ai">서울시 일일 사망</Chip><Chip color="ok">전국 일일 확진</Chip><Chip color="ok">전국 일일 사망</Chip></p>

<Grid cols="3">
<Stat value="1,212" unit="행" label="헤더를 뺀 데이터 행" />
<Stat value="euc-kr" label="인코딩" color="ai">쉼표로 구분</Stat>
<Stat value="최신 → 과거" label="행의 순서" color="ok">2023-05-31 → 2020-02-05</Stat>
</Grid>

<Callout kind="warn" title="데이터 결함 두 가지">

- `2023-03-26` 행에 빈 칸 두 개(서울 확진 · 전국 확진)
- 서울시 일일 사망은 `2022-02-28` 이전이 모두 0

</Callout>

<!--
결함 두 가지를 처음부터 알려 준다. 첫째 결함은 A-2와 B의 "빈 칸 처리" 함정으로, 둘째 결함은 B의 치명률 0% 함정으로 이어진다. 학생이 엑셀이나 VS Code로 파일을 한 번 열어 보게 한다.
-->

---
layout: section
---

# A. 구현

15분 직접 시도 → 답 받기 → 받은 코드 4단 확인

---

## #05. 문제마다 같은 순서

<Flow color="pastel">
<li><carbon:pen /><b>15분 직접 시도</b>교안 방식으로 먼저 쓴다<span class="small muted">open · with · readlines · split</span></li>
<li><carbon:chat /><b>답 받기</b>막힌 코드를 <code>## 내 시도</code>에<span class="small muted">템플릿 ⑰ · ⑱ · ⑲</span></li>
<li><carbon:play /><b>① 실행</b>정답과 대조<span class="small muted">내 노트북 결과가 기준</span></li>
<li><carbon:rule /><b>② 범위</b>배운 문법만<span class="small muted">csv 모듈이면 다시 요청</span></li>
<li><carbon:education /><b>③ 설명 · ④ 변형</b>줄마다 말로, 변형은 AI 없이</li>
</Flow>

| 문제 | 구할 것 | 템플릿 |
|:--|:--|:--|
| A-1 기본 정보 | 헤더를 뺀 행 수, 첫 날짜와 마지막 날짜 | ⑰ |
| A-2 전체 합계와 비율 | 서울 · 전국 확진 합계, 전국 대비 서울 비율 | ⑲ |
| A-3 최대 확진일 | 서울 일일 확진이 가장 많은 날짜와 값 | ⑰ · ⑱ |
| A-4 연도별 집계 후 저장 | 연도별 서울 확진 합계 → `seoul_yearly.csv` | ⑰ · ⑱ |

<!--
A-1 · A-3 · A-4의 템플릿은 원고에 지정이 없다. 처음 받을 때는 ⑰, 내 코드가 에러를 내거나 값이 틀리면 ⑱로 안내한다. A-2는 새 템플릿 ⑲로 받는다.
-->

---

## #06. A-1 기본 정보

<Callout icon="📄" title="헤더를 뺀 행 수, 첫 날짜와 마지막 날짜를 구한다" color="pastel-1"></Callout>

<Grid cols="3">
<Stat value="1212" unit="행" label="헤더를 뺀 행 수" />
<Stat value="2023-05-31" label="첫 날짜(첫 데이터 행)" color="ai" />
<Stat value="2020-02-05" label="마지막 날짜(마지막 행)" color="ok" />
</Grid>

<Callout kind="tip" title="확인 포인트">
행 수가 1213이면 헤더까지 센 것. 첫 날짜가 더 최근이다. 최신 날짜가 위에 있는 파일이기 때문
</Callout>

<!--
readlines()로 읽으면 리스트 길이가 1213(헤더 포함). lines[1:]의 길이가 1212. 첫 날짜는 lines[1], 마지막 날짜는 lines[-1]을 split한 첫 칸이다.
자주 막히는 곳: 상대 경로 기준. 노트북 파일이 있는 폴더가 기준이다. euc-kr을 빼먹으면 첫 줄부터 UnicodeDecodeError가 난다(C에서 다시 다룬다).
-->

---
layout: infographic
---

## #07. A-2 전체 합계와 비율

<Callout icon="🧮" title="서울 확진 합계, 전국 확진 합계, 전국 대비 서울 비율(소수 첫째 자리). 빈 칸은 0으로 본다" color="pastel-2"></Callout>

<Grid cols="3">
<Stat value="6,204,725" label="서울 확진 합계" />
<Stat value="31,683,292" label="전국 확진 합계" color="ai" />
<Stat value="19.6" unit="%" label="전국 대비 서울 비율" color="ok" />
</Grid>

<p>템플릿 <Chip color="ai" kind="outline">⑲ 데이터 정보와 함께 받기</Chip>로 받는다. 다음 쪽에서 새 템플릿을 본다</p>

<!--
빈 칸 행(2023-03-26)에서 int("")를 하면 ValueError: invalid literal for int() with base 10: ''가 난다. 이것이 학생이 15분 시도에서 가장 많이 막히는 지점이고, ⑲의 ## 내 시도에 넣을 재료가 된다.
"빈 칸은 0으로 본다"는 분석하는 사람이 정한 규칙이다. AI가 정하지 않게 ## 상황에 적는다.
-->

---
class: dense
---

## #08. 템플릿 ⑲ 데이터 정보와 함께 받기

<Callout icon="💡" title="AI는 내 파일을 모른다. 파일 위치 · 인코딩 · 첫 몇 줄을 함께 보낸다" color="pastel-2"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2">

````md
## 맥락
파이썬 파일입출력 단원을 배우는 중이야. VS Code 주피터 노트북에서 실행해.

## 상황
- 노트북과 같은 폴더에 covid19.csv가 있어. 인코딩은 euc-kr
- 첫 3줄:
  날짜,서울시 일일 확진,서울시 일일 사망,전국 일일 확진,전국 일일 사망
  2023-05-31,5987,6,24411,17
  2023-05-30,3326,1,13529,7
- 빈 칸이 있는 행이 있어. 빈 칸은 0으로 볼 거야
- 원하는 것: 서울 확진 합계, 전국 확진 합계, 전국 대비 서울 비율(소수 첫째 자리)

## 내 시도
{내 코드와 막힌 지점}

## 질문
내 시도를 이어서 완성한 코드를 줘.

## 제약
- open · with · readlines · split만 써. csv 모듈 · pandas는 쓰지 마
- 열 이름과 파일 이름은 위에 적은 그대로 써

## 출력 형식
1. 코드
2. | 줄 | 하는 일 | 표로
3. 결과가 맞는지 확인할 방법 2줄
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 사용 방법</h3>

- 첫 3줄은 파일에서 그대로 복사한다
- 15분 시도한 코드와 막힌 지점을 `{내 코드와 막힌 지점}`에 넣는다
- 받은 코드는 #02의 4단 확인을 거친다

</div>

<Callout kind="warn" title="주의">
CSV를 첨부해도 ChatGPT가 계산한 값은 정답이 아니다. 정답은 내 노트북 실행 결과
</Callout>

</div>
</Grid>

<!--
⑰과 다른 점은 ## 상황에 "내 데이터의 정보"가 들어간다는 것. 위치(같은 폴더) · 인코딩(euc-kr) · 첫 3줄(열 이름) · 빈 칸 처리 규칙. C의 에러 네 가지 중 세 가지(UnicodeDecodeError · FileNotFoundError · 열 이름 추측)가 이 정보가 빠졌을 때 생긴다. C를 마친 뒤 이 쪽으로 돌아와 짚어 준다.
-->

---
layout: magazine
---

## #09. A-3 최대 확진일

서울 일일 확진이 가장 많은 날짜와 값을 구한다.

- 날짜와 값을 **함께** 기억해야 한다
- 빈 칸 행도 지나가야 한다. 빈 칸은 0으로 본다
- 처음 받으면 ⑰, 내 코드가 틀리면 ⑱

::right::

<Stat value="128,375" label="서울 일일 확진 최댓값" color="ai">2022-03-17</Stat>

<Callout kind="tip" title="정답 대조">
날짜와 값이 둘 다 맞아야 통과. 값만 맞고 날짜가 다르면 날짜를 기억하는 줄을 다시 본다
</Callout>

<!--
학생 코드에서 자주 보이는 것: 최댓값만 갱신하고 날짜는 갱신하지 않음, 문자열끼리 비교함("9" > "128375"가 True). 문자열 비교면 값이 틀리게 나온다. int로 바꾼 뒤 비교했는지 ③ 설명 단계에서 말로 확인한다.
-->

---

## #10. A-4 연도별 집계 후 저장

<Callout icon="💾" title="연도별 서울 확진 합계를 딕셔너리로 만들어 seoul_yearly.csv로 저장하고 엑셀로 연다" color="pastel-3"></Callout>

<Grid cols="4">
<Tile color="pastel-1" tag="2020" value="18,395">서울 확진 합계</Tile>
<Tile color="pastel-2" tag="2021" value="206,375">서울 확진 합계</Tile>
<Tile color="pastel-3" tag="2022" value="5,440,196">서울 확진 합계</Tile>
<Tile color="pastel-4" tag="2023" value="539,759">서울 확진 합계</Tile>
</Grid>

<Callout kind="ai" title="④ 변형 — AI 없이 직접">
연도별 <b>행 수</b>를 구한다. 정답 2020 <code>331</code> · 2021 <code>365</code> · 2022 <code>365</code> · 2023 <code>151</code>
</Callout>

<Core color="ok">네 연도의 합은 A-2의 서울 합계 6,204,725와 같아야 한다</Core>

<!--
연도는 날짜 문자열의 앞 네 글자(LAB-05 문자열 슬라이싱). 딕셔너리에 연도별로 더하는 것은 LAB-06의 그룹별 집계와 같다.
④ 변형은 "더하는 값"을 "1"로 바꾸면 되는 문제다. 받은 코드를 이해했다면 한 줄만 바꾸면 된다. AI 없이 풀었는지 꼭 확인한다.
네 연도 합의 검산: 18,395 + 206,375 + 5,440,196 + 539,759 = 6,204,725. 행 수 합 331 + 365 + 365 + 151 = 1,212.
엑셀에서 연 채로 다시 저장하면 PermissionError가 난다(C에서 다룬다).
-->

---
layout: section
---

# B. "AI 답"의 함정

실행은 되지만 틀린 값, 또는 맞는 값이지만 범위 밖. 강사가 미리 받아 둔 AI 답을 검증한다

---

## #11. 함정 ① 빈 칸이 있는 행

<Grid cols="3fr 2fr" align="start">
<div>

```python
with open("covid19.csv", "r", encoding="euc-kr") as f:
    lines = f.readlines()

death_sum = 0
for line in lines[1:]:
    cols = line.strip().split(",")
    if "" in cols:
        continue
    death_sum += int(cols[2])

print(death_sum)
```

</div>
<div>

<Output>4118</Output>

<Callout kind="danger" icon="🔍" title="증상">
서울 사망 합계 정답은 <b>4120</b>. 실행은 되지만 2가 모자란다
</Callout>

<Steps color="ai">
<li>정답과 다른 값이 나온 줄을 찾는다</li>
<li>의심 가는 행을 원본 파일에서 직접 연다</li>
</Steps>

</div>
</Grid>

<!--
강사용 원인: 빈 칸이 있는 행을 통째로 건너뛰었다. 2023-03-26 행은 서울 확진 · 전국 확진만 비어 있고 서울 사망 값(2)은 있다. 행을 버리면 그 행의 다른 열 값까지 사라진다.
빈 칸 처리 방식(0으로 보기 · 행 버리기)은 분석하는 사람이 정한다. AI가 정하게 두지 않는다. 그래서 ⑲의 ## 상황에 "빈 칸은 0으로 볼 거야"를 적는다.
-->

---

## #12. 함정 ② `csv` 모듈로 받은 코드

<Grid cols="3fr 2fr" align="start">
<div>

```python
import csv

seoul_sum = 0
with open("covid19.csv", "r", encoding="euc-kr") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[1] != "":
            seoul_sum += int(row[1])

print(seoul_sum)
```

</div>
<div>

<Output>6204725</Output>

<Callout kind="tip" icon="✔️" title="① 실행은 통과">
A-2의 서울 합계와 같은 값
</Callout>

<Callout kind="warn" title="4단 확인 ② 범위">
<code>import csv</code> · <code>csv.reader</code> · <code>next</code>가 배운 문법인지 #03 표와 대조한다
</Callout>

</div>
</Grid>

<!--
강사용 원인: 값은 맞지만 ② 범위 위반. csv 모듈은 교안에 없다. 교안의 split 방식으로 다시 요청한다. ## 제약에 "csv 모듈 · pandas는 쓰지 마"를 적으면 처음부터 막을 수 있다.
값이 맞으면 학생은 통과시키기 쉽다. 4단 확인이 실행 하나로 끝나지 않는다는 것을 보여 주는 사례다.
-->

---

## #13. 함정 ③ 연도별 저장

<Grid cols="3fr 2fr" align="start">
<div>

```python
# yearly: A-4에서 만든 연도별 서울 확진 합계 딕셔너리
for year in yearly:
    with open("seoul_yearly.csv", "w", encoding="euc-kr") as f:
        f.write(year + "," + str(yearly[year]) + "\n")
```

</div>
<div>

<Callout kind="danger" icon="🔍" title="증상">
에러 없이 끝나지만, 엑셀로 열면 파일에 <b>마지막 연도 한 줄만</b> 있다
</Callout>

<Callout kind="tip" title="확인할 곳">
저장 결과는 출력이 아니라 <b>파일을 직접 열어</b> 확인한다. 네 연도 네 줄이 있어야 한다
</Callout>

</div>
</Grid>

<!--
강사용 원인: open(..., "w")를 반복문 안에서 호출했다. w 모드는 열 때마다 내용을 지운다. 그래서 반복의 마지막 연도만 남는다. 파일을 반복문 바깥에서 한 번 열고, 반복문 안에서는 write만 한다.
A-4의 "엑셀로 연다"가 이 함정을 잡는 단계다.
-->

---

## #14. 함정 ④ 연도별 서울 치명률

<Grid cols="3fr 2fr" align="start">
<div>

```python
# 치명률 = 사망 ÷ 확진 × 100, 빈 칸은 0
with open("covid19.csv", "r", encoding="euc-kr") as f:
    lines = f.readlines()

cases = {}
deaths = {}
for line in lines[1:]:
    cols = line.strip().split(",")
    year = cols[0][:4]
    if year not in cases:
        cases[year] = 0
        deaths[year] = 0
    if cols[1] != "":
        cases[year] += int(cols[1])
    deaths[year] += int(cols[2])

for year in cases:
    print(year, round(deaths[year] / cases[year] * 100, 1))
```

</div>
<div>

<Grid cols="2" gap="8 16">
<Stat value="0" unit="%" label="2020년 치명률" color="ai" />
<Stat value="0" unit="%" label="2021년 치명률" color="ai" />
</Grid>

<Callout kind="danger" icon="🔍" title="증상">
2020 · 2021년 서울 치명률이 0%. 코드를 아무리 봐도 틀린 줄이 없다
</Callout>

</div>
</Grid>

<!--
꼭 다루는 사례. 학생은 코드에서 원인을 찾으려고 오래 헤맨다. 코드는 맞다. 충분히 헤매게 둔 뒤 다음 쪽으로 넘어간다.
-->

---

### #14-1. 결과가 이상하면 원본 데이터도 연다

<Timeline color="ok">
<li><b>2020-02-05</b>데이터 시작(파일의 마지막 행)</li>
<li class="now"><b>2022-02-28</b>서울시 일일 사망 기록이 이날부터 있음</li>
<li><b>2023-05-31</b>데이터 끝(파일의 첫 행)</li>
</Timeline>

<Grid cols="2">
<Tile kind="surface" color="danger" tag="2022-02-28 이전" title="서울시 일일 사망이 모두 0">
2020년과 2021년은 이 구간에 모두 들어간다
</Tile>
<Tile kind="surface" color="ok" tag="판단" title="코드가 아니라 데이터 문제">
0 ÷ 확진은 0. 계산은 맞고, 기록이 없을 뿐이다
</Tile>
</Grid>

<Core color="warn">결과가 이상하면 코드만 보지 말고 원본 데이터도 연다</Core>

<!--
강사용 원인: 코드가 아니라 데이터 문제. 서울시 사망 기록이 2022-02-28부터 있다. #04에서 미리 알려 준 결함 두 번째가 여기서 나온다.
이 0%를 "2020 · 2021년에는 아무도 죽지 않았다"로 해석해 보고서에 쓰면 틀린 결론이 된다. 데이터 분석에서 가장 흔한 실수 중 하나다. ChatGPT에게 물어도 데이터를 보지 못하면 코드만 의심한다.
-->

---
layout: section
---

# C. 에러 수정

받은 코드를 내 노트북에 붙였을 때 나는 에러를 고친다

---

## #15. 에러 ① · ② 파일을 열지 못한다

<Grid cols="2" align="start">
<div>

<div class="kicker">AI 답이 encoding 없이 열기</div>

```python
with open("covid19.csv", "r") as f:
    lines = f.readlines()
```

<Output label="에러">UnicodeDecodeError: 'utf-8' codec can't decode byte ...</Output>

</div>
<div>

<div class="kicker">AI 답의 파일 경로가 내 폴더와 다름</div>

```python
with open("data/covid19.csv", "r", encoding="euc-kr") as f:
    lines = f.readlines()
```

<Output label="에러">FileNotFoundError</Output>

</div>
</Grid>

<Callout kind="tip">
트레이스백은 맨 아래 줄부터 읽는다. 에러 이름과 내 파일 정보(인코딩 · 위치)를 맞춰 본다
</Callout>

<!--
강사용 원인
- UnicodeDecodeError: 이 파일은 euc-kr. AI는 내 파일의 인코딩을 모른다. ⑲의 "인코딩은 euc-kr"이 막아 준다.
- FileNotFoundError: 상대 경로의 기준은 노트북 위치. AI는 내 폴더 구조를 모른다. ⑲의 "노트북과 같은 폴더에"가 막아 준다.
경로 예시는 설명용이다. 실제 AI 답의 경로는 다를 수 있다.
-->

---

## #16. 에러 ③ · ④ 열 이름과 저장

<Grid cols="2" align="start">
<div>

<div class="kicker">AI 답이 열 이름을 지어냄</div>

```python
header = lines[0].strip().split(",")
idx = header.index("서울 확진")
```

<Output label="에러">ValueError: '서울 확진' is not in list</Output>

<p class="small muted">에러가 나지 않고 엉뚱한 열을 계산하는 경우도 있다</p>

</div>
<div>

<div class="kicker">엑셀에서 열어 둔 CSV에 저장</div>

```python
with open("seoul_yearly.csv", "w", encoding="euc-kr") as f:
    f.write("2020,18395\n")
```

<Output label="에러">PermissionError</Output>

</div>
</Grid>

<Steps color="ok">
<li>에러 원문을 그대로 두고 원인을 먼저 내 말로 적는다</li>
<li>스스로 못 고치면 템플릿 ⑱ 내 코드 고쳐 받기로 보낸다. <code>## 내 시도</code>에 내가 생각한 원인을 쓴다</li>
</Steps>

<!--
강사용 원인
- 열 이름: 첫 줄(헤더)을 붙여 넣지 않으면 AI가 열을 추측한다. 실제 열 이름은 "서울시 일일 확진". 열 위치(cols[1])를 추측해 엉뚱한 열을 계산하는 경우가 더 위험하다. 에러가 없기 때문. ⑲의 "첫 3줄"이 막아 준다.
- PermissionError: 엑셀이 파일을 잡고 있다. 파일을 닫고 다시 실행한다.
C를 마친 뒤 #08(템플릿 ⑲)로 돌아가 상황 섹션의 각 줄이 어느 에러를 막는지 함께 짚는다.
-->

---
layout: section
---

# D. 정리

새 템플릿을 내 파일에 추가하고, 오늘 고친 실수를 한 줄로 남긴다

---
layout: cards
cols: 3
---

## #17. 오늘의 결과물

<div class="py">

#### <carbon:code /> A-1 ~ A-4 코드

- 문제마다 4단 확인 표시
- ① 실행 · ② 범위 · ③ 설명 · ④ 변형

</div>
<div class="ai">

#### <carbon:document /> seoul_yearly.csv

- 연도별 서울 확진 합계 네 줄
- 엑셀로 열어 확인

</div>
<div class="ok">

#### <carbon:template /> 템플릿 ⑲

- 「내 프롬프트 템플릿.md」에 추가
- 오늘 고친 실수 한 줄 기록

</div>

<Callout kind="real" title="한 장으로 기억하기">
<b>받기</b> AI는 내 파일을 모른다. 위치 · 인코딩 · 첫 몇 줄을 보낸다(⑲)<br>
<b>빈 칸</b> 처리 방식은 내가 정한다<br>
<b>검증</b> 값이 맞아도 범위를 보고, 값이 이상하면 원본 데이터를 연다<br>
<b>정답</b> 내 노트북 실행 결과
</Callout>

<!--
자주 막히는 곳: 상대 경로 기준, euc-kr, 빈 칸 처리 결정.
데이터 분석 연결: 읽기 → 정제(LAB-05 · 07) → 집계(LAB-06) → 저장. LAB-10 이후 pandas가 한 줄로 하는 일을 오늘 직접 해 봤다.
다음 LAB-09에서는 클래스로 기록을 관리하고, ② 답 받기 단계를 마무리한다.
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-08] 파일입출력 3 · ITWILL · {teacher} 강사</p>

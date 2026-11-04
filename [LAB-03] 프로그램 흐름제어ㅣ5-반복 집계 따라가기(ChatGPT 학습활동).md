---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 프로그램 흐름제어 — 반복 집계 따라가기
layout: cover
---

# 반복 집계 따라가기 — 조건문과 반복문

코드는 내가 쓰고, 막히면 템플릿으로 조언을 받는다. 반복 회차마다 변수 값을 먼저 적어 보는 연습

<p class="sub">[LAB-03] 프로그램 흐름제어 5 · ITWILL · {teacher} 강사</p>

<!--
「조건문」「반복문 while」「반복문 for」「문법의 중첩」 수업을 마친 뒤 하는 실습. ① 조언 받기 단계(LAB-02 ~ 06)라서 코드는 학생이 쓰고, ChatGPT는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 맡는다(「ChatGPT 지침.md」 그대로).
LAB-02에서 모은 템플릿 ①~⑫를 그대로 꺼내 쓰고, 오늘 새 템플릿 ⑬ 추적표 점검받기를 하나 더한다.
-->

---

## #01. 오늘의 흐름 — 2교시 약 100분

<Timeline>
<li><b>A 구현 · 40분</b>문제를 직접 푼다. 막히면 템플릿으로 조언을 받는다</li>
<li><b>B 결과가 이상할 때 · 25분</b>강사가 준 코드의 틀린 값을 찾아 고친다</li>
<li><b>C 에러 수정 · 25분</b>에러 코드의 원인을 찾아 고친다</li>
<li class="now"><b>D 정리 · 10분</b>새 템플릿을 「내 프롬프트 템플릿.md」에 추가, 오늘 고친 실수 한 줄 기록</li>
</Timeline>

<Grid cols="2" align="start">

<Callout kind="real" title="오늘의 규칙">

- 코드는 내가 쓰고, AI에게는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 묻는다
- 프롬프트는 다섯 섹션 `## 맥락` `## 상황` `## 질문` `## 제약` `## 출력 형식`

</Callout>

<Tile kind="soft" color="ai" tag="오늘 새로 더하는 템플릿" title="⑬ 추적표 점검받기">
LAB-02의 ①~⑫ 뒤로 이어 매긴다. 반복 회차별 변수 값을 표로 먼저 채우고 점검받는다
</Tile>

</Grid>

<!--
B · C의 코드는 강사가 미리 준비해 나눠 준다. 시작 전에 ChatGPT 맞춤 지침이 들어 있는지, 템플릿마다 새 대화를 여는지 말로 확인한다.
-->

---

## #02. `## 제약`에 쓰는 범위 — 네 단원

<div class="kicker">오늘 쓰는 모든 프롬프트의 <code>## 제약</code>에는 이 표의 범위를 적는다</div>

| 단원 | 범위 |
|:--|:--|
| 1 조건문 | if · else · elif, 비교 · 논리 연산자, 논리값 조건 |
| 2 반복문 while | 증감식, 합계 누적 |
| 3 반복문 for | range(시작, 끝, 증감) |
| 4 문법의 중첩 | 중첩 조건문, 반복문 안의 조건문, 중첩 반복문, break · continue |

<Core color="ok">AI의 답이 이 범위를 벗어나면 메모만 하고 넘어간다.</Core>

<!--
학생이 범위를 비워 두면 AI가 리스트나 함수 같은 다음 단원 내용을 섞어 답한다. 표의 둘째 열을 그대로 복사해 쓰게 한다.
-->

---
layout: section
---

# A. 구현

40분. 문제를 직접 풀고, 막히면 템플릿으로 조언을 받는다

---
layout: magazine
---

## #03. A-1 조건 합계

1부터 100 중 **3의 배수이면서 5의 배수가 아닌 수**의 합을 구한다.

- 반복문으로 1부터 100까지 하나씩 본다
- 조건문으로 "3의 배수"와 "5의 배수가 아님"을 함께 검사한다
- 조건을 통과한 수만 합계에 누적한다

<p><Chip color="py">템플릿</Chip> ⑤ 단계로 쪼개기</p>

::right::

<Stat value="1368" label="정답" color="ok" />

<Callout kind="tip" title="막히면 ⑤">
만들 것과 정답 1368을 <code>## 상황</code>에 적고, 내가 생각한 첫 단계를 함께 보낸다
</Callout>

<!--
⑤ 단계로 쪼개기를 쓰는 문제. 처리 순서(반복 → 조건 검사 → 누적)를 받고 한 단계씩 써서 실행한다. 정답이 1368이 아니면 B에서 다룰 range 끝 값, 누적 변수 위치를 먼저 의심하게 한다.
-->

---

## #04. A-2 기온 등급

<div class="kicker">기온을 입력받아 33 이상이면 <code>폭염경보</code>, 31 이상이면 <code>폭염주의</code>, 그 밖은 <code>정상</code>을 출력한다</div>

<Grid cols="4">
<Tile kind="soft" color="ok" tag="확인 입력값" value="30.9">정상</Tile>
<Tile kind="soft" color="yellow" tag="확인 입력값" value="31">폭염주의</Tile>
<Tile kind="soft" color="yellow" tag="확인 입력값" value="32.9">폭염주의</Tile>
<Tile kind="soft" color="danger" tag="확인 입력값" value="33">폭염경보</Tile>
</Grid>

<Steps color="ai">
<li>코드를 쓰기 전에 <b>경계값을 내가 먼저</b> 고른다</li>
<li>템플릿 <b>⑨ 확인용 입력값 묻기</b>로 내가 고른 값을 보내고 <b>빠진 값</b>을 묻는다</li>
<li>위 네 값을 하나씩 넣어 실행하고, 출력이 맞는지 직접 확인한다</li>
</Steps>

<!--
⑨ 확인용 입력값 묻기를 쓰는 문제. 학생이 고르는 값은 대개 30 · 35 같은 "가운데" 값이다. 31 · 33처럼 등급이 바뀌는 바로 그 값과, 30.9 · 32.9처럼 바로 아래 값을 넣어 봐야 한다는 것을 AI 답에서 확인하게 한다.
입력값이 실수(30.9)이므로 float 변환이 필요하다. C-2의 TypeError와 이어진다.
-->

---
layout: infographic
---

## #05. A-3 누적 목표 도달일

<div class="kicker">첫날 방문자 100명, 매일 전날보다 15명씩 늘어난다. 누적 방문자가 처음 3000명 이상이 되는 날과 그때의 누적값을 구한다</div>

<Flow color="pastel">
<li><carbon:calendar /><b>day</b>며칠째인지</li>
<li><carbon:user-multiple /><b>v</b>그날의 방문자 수</li>
<li><carbon:add-alt /><b>tot</b>그날까지의 누적</li>
<li><carbon:stop-outline /><b>break</b>tot이 3000 이상이면 멈춤</li>
</Flow>

<Grid cols="3">
<Stat value="15" unit="일째" label="처음 3000명 이상이 되는 날" color="py" />
<Stat value="3075" unit="명" label="그때의 누적 방문자" color="ok" />
<Tile kind="soft" color="ai" tag="필수 문법" title="while + break">템플릿 ⑬ 추적표 점검받기</Tile>
</Grid>

<!--
변수 이름 day · v · tot는 템플릿 ⑬의 추적표와 같게 맞춘다. 그래야 학생이 표와 코드의 print 결과를 바로 대조할 수 있다.
자주 막히는 곳: 누적 변수를 반복문 밖에서 초기화하지 않음, break 위치(누적 전 · 후)에 따라 날짜가 하루 어긋남.
-->

---

## #06. A-3 추적표 — 실행 전에 먼저 채운다

<Grid cols="3fr 2fr" align="start">
<div>

| 회차 | day | v | tot | break 여부 |
|:--:|:--:|:--:|:--:|:--:|
| 1 | 1 | 100 | 100 | X |
| 2 | | | | |
| 3 | | | | |
| … | | | | |
| 마지막 | | | | |

</div>
<div>

<Steps>
<li>코드를 쓰고 <b>실행하기 전에</b> 회차별 값을 표에 채운다</li>
<li>⑬으로 표를 보내 <b>틀린 칸</b>만 점검받는다</li>
<li>반복문 안에 <code>print(day, v, tot)</code>를 넣어 실제 값과 대조한다</li>
</Steps>

</div>
</Grid>

<Callout kind="warn" title="주의">
첫 줄은 예시로 채워 두었다. 2회차부터는 손으로 계산해 적고, 마지막 회차의 day · tot이 #05의 정답과 같은지 본다
</Callout>

<!--
첫 행은 템플릿 ⑬ 원문의 예시(1 | 1 | 100 | 100 | X)다. break 여부 칸이 O가 되는 회차가 15회차여야 한다.
break를 누적 전에 검사하면 하루 늦게, 조건을 잘못 쓰면 하루 이르게 멈춘다. 학생이 표에서 이것을 먼저 발견하게 두고, 못 찾으면 print 결과와 대조하게 한다.
-->

---
class: dense
---

## #07. ⑬ 추적표 점검받기

<Callout icon="💡" title="반복문을 실행하기 전에 회차별 변수 값을 표로 먼저 채우고, 맞는지 점검받고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2">

````md
## 맥락
파이썬 반복문(while) 단원을 배우는 중이야.

## 상황
아래 코드를 실행하기 전에 내가 추적표를 먼저 채웠어.
{코드 붙여 넣기}

| 회차 | day | v | tot | break 여부 |
| 1 | 1 | 100 | 100 | X |
| 2 | ... |

## 질문
내 추적표에서 틀린 칸이 있으면 몇 회차 어느 칸인지, 왜 틀렸는지 알려줘.

## 제약
- 정답 표를 통째로 다시 쓰지 마. 틀린 칸만 짚어 줘
- 조건문 · while · for · break · continue 범위 안에서 설명해

## 출력 형식
| 회차 | 칸 | 내가 쓴 값 | 이유 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 사용 방법</h3>

- 코드와 내가 채운 추적표를 그대로 붙인다
- 틀린 칸과 이유만 받고, 고치는 건 내가 한다
- 점검받은 뒤 반복문 안에 `print(day, v, tot)`를 넣어 실제 값과 대조한다

</div>

<Callout kind="warn" title="주의">
"정답 표 보여 줘"라고 하면 내가 계산할 기회가 사라진다. 틀린 칸만 짚어 달라고 한다
</Callout>

</div>
</Grid>

<!--
새 템플릿 ⑬. ⑦ · ⑧이 "실행 후 값이 이상할 때"라면 ⑬은 "실행 전에 내 예측을 점검"하는 쪽이다. AI의 점검도 추측이므로, 마지막에 print 결과와 대조하는 단계를 빼지 않게 한다.
학생이 추적표를 몇 회차만 채우고 보내면 "마지막 회차까지 채우기"를 요구한다. 15회차까지 다 쓰기 어려우면 앞 3회차와 마지막 2회차만 채워도 된다.
-->

---
layout: section
---

# B. 결과가 이상할 때

25분. 에러는 없는데 값이 틀린 코드에서 틀린 곳을 찾아 고친다

---

## #08. 버그 찾기 진행 방법

<Flow color="ok">
<li><carbon:play /><b>실행</b>강사가 준 코드를 그대로 쓰고 실행</li>
<li><carbon:compare /><b>비교</b>기대한 값과 실제 값을 적는다</li>
<li><carbon:chat /><b>질문</b>짐작이 없으면 ⑦, 있으면 ⑧</li>
<li><carbon:edit /><b>수정</b>찍어 보고 내가 고친다</li>
</Flow>

| | 코드 | 증상 |
|:--:|:--|:--|
| B-1 | `for i in range(1, 10): total += i` 로 1~10 합계 | 55가 아니라 45 |
| B-2 | 반복문 안에서 `total = 0` | 합계가 마지막 값만 나옴 |
| B-3 | `if t >= 31:` 주의, 다음 `elif t >= 33:` 경보 | 35도에도 `폭염주의` |

<Core color="ai">AI가 알려 준 곳을 print()로 내가 찍어 보고 원인을 찾는다.</Core>

<!--
LAB-02의 ⑦ 확인할 곳 묻기 · ⑧ 내 추측 확인 방법 묻기를 그대로 꺼내 쓴다. 반복문 버그는 ⑬ 추적표로 보내도 된다.
-->

---
layout: cards
cols: 2
---

## #09. B-1 · B-2 — 1~10 합계

<div class="py">

#### B-1 · range로 1~10 더하기

```python
total = 0
for i in range(1, 10):
    total += i
print(total)
```

<Output label="증상">55가 아니라 45</Output>

</div>
<div class="ai">

#### B-2 · 반복문 안에서 초기화

```python
for i in range(1, 11):
    total = 0
    total += i
print(total)
```

<Output label="증상">합계가 마지막 값만 나옴</Output>

</div>

<!--
강사용 원인(학생 자료에는 없음):
B-1 range의 끝 값은 포함되지 않음. range(1, 11)로 고친다.
B-2 누적 변수 초기화 위치. total = 0을 반복문 밖(위)으로 옮긴다. A-3 추적표에서 tot이 매 회차 초기화되는 모습과 연결한다.
-->

---
layout: magazine
---

## #10. B-3 — 기온 등급

`if t >= 31:` 주의, 다음 `elif t >= 33:` 경보 순서로 쓴 코드. 35도를 넣었다.

```python
t = 35
if t >= 31:
    print("폭염주의")
elif t >= 33:
    print("폭염경보")
```

::right::

<Output label="증상">35도에도 폭염주의</Output>

<Callout kind="tip" title="A-2와 비교">
A-2의 규칙대로라면 33 이상은 <code>폭염경보</code>. 내 A-2 코드의 조건 순서도 함께 확인한다
</Callout>

<!--
강사용 원인(학생 자료에는 없음): 조건 순서. 넓은 조건(31 이상)이 먼저 걸려 33 이상이 검사되지 않는다. 좁은 조건을 먼저 쓴다. A-2를 이 순서로 쓴 학생은 자기 코드에서도 같은 버그를 찾게 한다.
-->

---
layout: section
---

# C. 에러 수정

25분. 에러 원문을 그대로 보내 원인을 받고, 고치는 건 내가 한다

---

## #11. C-1 · C-2 — 비교 기호와 input

<Grid cols="2" align="start">
<div>

<div class="kicker">C-1 · 점수 비교</div>

```python
score = 90
if score = 90:
    print("90점")
```

<Output label="에러">SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?</Output>

</div>
<div>

<div class="kicker ai">C-2 · 기온 입력</div>

```python
t = input()
if t >= 33:
    print("폭염경보")
```

<Output label="에러">TypeError: '>=' not supported between instances of 'str' and 'int'</Output>

</div>
</Grid>

<Steps color="ai">
<li>코드를 그대로 쓰고 실행해 <b>에러 원문</b>을 확인한다</li>
<li>⑩ 에러 원문 보내기로 코드와 에러 메시지 전체를 보낸다</li>
<li>원인과 고치는 방향을 받고, 고친 뒤에는 ⑪로 같은 실수를 막는다</li>
</Steps>

<!--
강사용 원인(학생 자료에는 없음):
C-1 비교는 ==. =는 대입이다. 에러 메시지가 직접 '=='를 제안하므로 마지막 줄을 끝까지 읽는 습관을 잡는다.
C-2 input 결과는 문자열. float(input())으로 바꾼다. A-2에서 30.9를 넣어야 하므로 int가 아니라 float가 맞다.
-->

---

## #12. C-3 · C-4 — 들여쓰기와 끝나지 않는 반복

<Grid cols="2" align="start">
<div>

<div class="kicker">C-3 · <code>if</code> 아래 줄 들여쓰기 누락</div>

```python
t = 35
if t >= 33:
print("폭염경보")
```

<Output label="에러">IndentationError: expected an indented block after 'if' statement on line N</Output>

</div>
<div>

<div class="kicker ai">C-4 · <code>while</code> 안에서 증감식 누락</div>

```python
day = 1
tot = 0
while day <= 15:
    tot += 100
print(tot)
```

<Output label="증상">에러 없이 끝나지 않음</Output>

</div>
</Grid>

<Callout kind="danger" title="끝나지 않을 때">
주피터 노트북의 <b>중지 버튼</b>으로 실행을 멈춘 뒤, while 조건에 쓰인 변수가 반복문 안에서 바뀌는지 확인한다
</Callout>

<!--
강사용 원인(학생 자료에는 없음):
C-3 블록 들여쓰기. if 아래 실행할 줄은 들여 써야 한다. 메시지의 line N은 if가 있는 줄 번호다(이 코드에서는 2).
C-4 무한 반복. day가 바뀌지 않아 조건 day <= 15가 계속 참이다. 중지 버튼으로 멈추고 조건 변수 확인. day += 1을 넣는다.
C-4는 에러 메시지가 없으므로 ⑩ 대신 ⑦(확인할 곳 묻기)이나 ⑬(추적표)으로 보내게 한다.
-->

---
layout: section
---

# D. 정리

10분. 새 템플릿을 저장하고 오늘 고친 실수를 한 줄로 남긴다

---
layout: cards
cols: 3
---

## #13. 오늘의 결과물

<Tile kind="soft" color="py" tag="A-3" title="추적표">
회차별 day · v · tot · break 여부를 채우고, print 결과와 대조한 표
</Tile>

<Tile kind="soft" color="ai" tag="템플릿" title="⑬ 추적표 점검받기">
「내 프롬프트 템플릿.md」의 ⑫ 뒤에 추가한다
</Tile>

<Tile kind="soft" color="ok" tag="실수 기록" title="오늘 고친 실수 한 줄">
B · C에서 내가 실제로 고친 것 중 하나를 내 말로 적는다
</Tile>

<Callout kind="real" title="한 장으로 기억하기">
<b>A</b> 막히면 ⑤ · ⑨ · ⑬을 꺼낸다 · <b>B</b> 기대한 값과 실제 값을 적고 ⑦ · ⑧ · <b>C</b> 에러 원문을 그대로 ⑩ · ⑪<br>
<b>확인</b> AI의 답은 추측. 내 코드를 직접 실행한 결과가 정답이다
</Callout>

<!--
결과물은 걷지 않고 확인만 한다. 「내 프롬프트 템플릿.md」에 ⑬이 들어갔는지 본다.
데이터 분석 연결: 합계 · 누적은 모든 집계의 기본 동작이다. 다음 단원(리스트)에서 같은 누적을 리스트의 값으로 한다.
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-03] 프로그램 흐름제어 5 · ITWILL · {teacher} 강사</p>

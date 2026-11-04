---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 리스트 — 한 열의 값 다루기
layout: cover
---

# 한 열의 값 다루기 — 리스트

요일별 판매량 리스트 하나로 합계 · 평균 · 탐색 · 이동평균 · 2차원 합계까지 직접 구하는 연습

<p class="sub">[LAB-04] 리스트 7 · ITWILL · {teacher} 강사</p>

<!--
리스트 단원(리스트의 이해 · 인덱싱과 슬라이싱 · 원소 복사 · 리스트 탐색 · 리스트 관련 함수)을 마친 뒤 하는 실습. ① 조언 받기 단계라서 코드는 학생이 쓰고, ChatGPT는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 맡는다.
LAB-02의 ①~⑫, LAB-03의 ⑬에 이어 오늘 새 템플릿 ⑭ 두 방법 비교받기를 더한다.
-->

---

## #01. 오늘의 흐름 — 2교시 약 100분

<Grid cols="4">
<Tile kind="soft" color="py" tag="A 구현" value="40분">문제를 직접 푼다. 막히면 템플릿으로 조언을 받는다</Tile>
<Tile kind="soft" color="ai" tag="B 결과가 이상할 때" value="25분">강사가 준 코드의 틀린 값을 찾아 고친다</Tile>
<Tile kind="soft" color="danger" tag="C 에러 수정" value="25분">에러 코드의 원인을 찾아 고친다</Tile>
<Tile kind="soft" color="ok" tag="D 정리" value="10분">새 템플릿을 「내 프롬프트 템플릿.md」에 추가, 오늘 고친 실수 한 줄 기록</Tile>
</Grid>

<Callout kind="real" title="오늘의 규칙">

- 코드는 내가 쓰고, AI에게는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 묻는다
- 프롬프트는 다섯 섹션 `## 맥락` `## 상황` `## 질문` `## 제약` `## 출력 형식`. `## 제약`에는 #02 표의 범위를 적는다

</Callout>

<p><Chip color="ai">오늘 새로 더하는 템플릿</Chip> ⑭ 두 방법 비교받기 · 비슷한 두 방법의 차이를 표로 받고, 각 칸을 직접 실행해 확인한다</p>

<!--
B · C의 코드는 강사가 미리 준비해 나눠 준다. 시작 전에 ChatGPT 맞춤 지침이 들어 있는지, 템플릿마다 새 대화를 여는지 말로 확인한다.
-->

---

## #02. `## 제약`에 쓰는 범위 — 리스트 단원

| 단원 | 범위 |
|:--|:--|
| 1 리스트의 이해 | 리스트 정의, 인덱스 접근, 리스트 연산, 2차원 리스트 |
| 2 인덱싱과 슬라이싱 | 역방향 인덱스, 슬라이싱, 슬라이싱으로 교체 · 삭제 |
| 3 원소 복사 | 얕은 복사, 슬라이싱 · copy() 복사, 튜플, 구조분해 |
| 4 · 5 리스트 탐색 | in · not in, while · for 탐색, 인덱스와 원소 동시 탐색, 2차원 탐색 |
| 6 리스트 관련 함수 | len · del · sorted · max · min · sum, list · tuple 변환, range 수열, count · index · append · insert · pop · extend · remove · reverse · sort · split · join |

<Core color="ok">AI의 답이 이 범위를 벗어나면 메모만 하고 넘어간다.</Core>

<!--
6단원 범위가 길다. 프롬프트마다 전부 붙이지 말고 그 문제에 필요한 단원 줄만 골라 넣어도 된다.
-->

---

## #03. 연습 데이터

<div class="kicker">오늘 모든 문제는 이 세 리스트로 푼다. 노트북 맨 위 셀에 그대로 쓰고 실행해 둔다</div>

```python
days  = ["월", "화", "수", "목", "금", "토", "일"]
sales = [120, 95, 143, 88, 160, 132, 101]        # 요일별 판매량
branch = [[120, 135, 150, 140],                 # 지점 3곳 × 분기 4개 매출
          [90, 110, 105, 125],
          [200, 180, 210, 230]]
```

<Grid cols="3">
<Tile kind="surface" color="py" tag="days" title="요일 이름">sales와 같은 순서로 짝을 이룬다</Tile>
<Tile kind="surface" color="ai" tag="sales" title="요일별 판매량">A-1 ~ A-3, B, C에서 쓴다</Tile>
<Tile kind="surface" color="ok" tag="branch" title="지점 3곳 × 분기 4개">A-4 2차원 합계에서 쓴다</Tile>
</Grid>

<!--
days와 sales는 같은 인덱스가 같은 요일이다. 이 짝이 깨지는 것이 B-1의 버그다.
-->

---
layout: section
---

# A. 구현

40분. 문제를 직접 풀고, 막히면 템플릿으로 조언을 받는다

---
layout: infographic
---

## #04. A-1 기본 통계

<div class="kicker"><code>sales</code>의 합계, 평균(소수 첫째 자리), 최댓값과 그 요일</div>

<Grid cols="3">
<Stat value="839" label="합계" color="py" />
<Stat value="119.9" label="평균 (소수 첫째 자리)" color="ai" />
<Stat value="160" label="최댓값" color="ok">그 요일은 <b>금</b></Stat>
</Grid>

<Core color="py">최댓값의 요일은 days와 sales가 같은 인덱스로 짝을 이룬다는 점을 이용한다.</Core>

<!--
학생이 평균을 직접 반복문으로 누적해도, sum과 len을 써도 된다. 두 방법 모두 839와 119.9가 나오는지 본다.
최댓값의 요일은 sales에서 최댓값의 위치를 찾아 days의 같은 위치를 꺼낸다. 여기서 sort()를 쓰면 B-1 버그가 그대로 생긴다.
-->

---
layout: cards
cols: 2
---

## #05. A-2 조건 탐색 · A-3 3일 이동평균

<div class="py">

#### A-2 · 평균 이상인 요일 목록

- A-1에서 구한 평균과 각 요일의 판매량을 비교한다
- 평균 이상이면 그 요일 이름을 새 리스트에 모은다

<Output label="정답">['월', '수', '금', '토']</Output>

</div>
<div class="ai">

#### A-3 · 3일 이동평균

- **슬라이싱**으로 연속 3일을 잘라 평균을 구한다
- 결과를 새 리스트로 모으고, 소수 첫째 자리까지

<Output label="정답">[119.3, 108.7, 130.3, 126.7, 131.0]</Output>

<p><Chip kind="outline" color="ai">템플릿</Chip> ⑤ 단계로 쪼개기</p>

</div>

<!--
A-2: 평균을 반올림한 119.9와 비교하든, 반올림 전 값과 비교하든 결과는 같다.
A-3: 이동평균 개수는 7 - 3 + 1 = 5개. 반복 범위를 잘못 잡으면 C-1의 IndexError가 나거나 개수가 하나 모자란다. ⑤로 "슬라이스 하나 → 평균 하나 → 리스트에 추가 → 반복" 순서를 받게 한다.
-->

---

## #06. A-4 2차원 합계

<div class="kicker"><code>branch</code>에서 지점별(행) 합계와 분기별(열) 합계를 구한다</div>

<Grid cols="2" align="start">
<Tile kind="soft" color="py" tag="행 · 지점별 합계" title="지점 3곳">

`[545, 430, 820]`

</Tile>
<Tile kind="soft" color="ok" tag="열 · 분기별 합계" title="분기 4개">

`[410, 425, 465, 495]`

</Tile>
</Grid>

<Steps color="ok">
<li>행 합계: 바깥 리스트에서 <b>한 줄씩</b> 꺼내 더한다</li>
<li>열 합계: 같은 위치(분기)의 값을 <b>지점마다</b> 하나씩 모아 더한다</li>
<li>결과 리스트의 길이가 행은 3, 열은 4인지 확인한다</li>
</Steps>

<!--
행 합계는 sum(행)으로 바로 되지만 열 합계는 중첩 반복문(2차원 탐색)이 필요하다. 바깥 반복을 분기, 안쪽 반복을 지점으로 두는 순서가 헷갈리면 LAB-03의 ⑬ 추적표로 회차별 값을 먼저 적게 한다.
-->

---
layout: section
---

# B. 결과가 이상할 때

25분. 에러는 없는데 값이 틀린 코드에서 틀린 곳을 찾아 고친다

---

## #07. 버그 찾기 — 네 가지 코드

| | 코드 | 증상 |
|:--:|:--|:--|
| B-1 | `sales.sort()` 후 `days[sales.index(max(sales))]` | 최댓값의 요일이 `일` |
| B-2 | `backup = sales` 후 `sales[0] = 0` | backup도 0으로 바뀜 |
| B-3 | `for i in range(len(sales) - 1):` 로 합계 | 839가 아니라 738 |
| B-4 | `result = sales.append(150)` | result가 `None` |

<Grid cols="2" align="start">

<Steps>
<li>코드를 그대로 쓰고 실행해 <b>기대한 값과 실제 값</b>을 적는다</li>
<li>짐작이 없으면 <b>⑦</b>, 있으면 <b>⑧</b>로 보낸다</li>
<li>AI가 알려 준 곳을 <code>print()</code>로 찍어 보고 내가 고친다</li>
</Steps>

<Callout kind="warn" title="코드마다 데이터를 새로">
B 코드는 sales를 바꾼다. 하나를 실행한 뒤에는 #03 연습 데이터 셀을 다시 실행하고 다음 코드로 넘어간다
</Callout>

</Grid>

<!--
B-1은 ⑭ 두 방법 비교받기로 이어진다. B-1을 고친 뒤 ⑭로 sort와 sorted의 차이를 표로 받는다.
-->

---

## #08. B-1 · B-2 — 원본이 바뀌는 코드

<Grid cols="2" align="start">
<div>

<div class="kicker">B-1 · 정렬 후 최댓값의 요일</div>

```python
sales.sort()
print(days[sales.index(max(sales))])
```

<Output label="증상">최댓값의 요일이 일 (기대한 값: 금)</Output>

</div>
<div>

<div class="kicker ai">B-2 · 백업해 두고 값 바꾸기</div>

```python
backup = sales
sales[0] = 0
print(backup)
```

<Output label="증상">backup도 0으로 바뀜</Output>

</div>
</Grid>

<!--
강사용 원인(학생 자료에는 없음):
B-1 sort()가 원본 순서를 바꿈. 정렬 뒤에는 sales와 days의 짝이 깨진다. sorted()는 원본 유지. A-1처럼 정렬하지 않고 max와 index만 쓰면 된다.
B-2 얕은 복사. backup과 sales가 같은 리스트를 가리킴. 슬라이싱(sales[:])이나 copy()로 복사한다(원소 복사 단원).
-->

---

## #09. B-3 · B-4 — 하나 모자란 합계와 None

<Grid cols="2" align="start">
<div>

<div class="kicker">B-3 · 인덱스로 합계</div>

```python
total = 0
for i in range(len(sales) - 1):
    total += sales[i]
print(total)
```

<Output label="증상">839가 아니라 738</Output>

</div>
<div>

<div class="kicker ai">B-4 · 값 추가 결과 받기</div>

```python
result = sales.append(150)
print(result)
```

<Output label="증상">result가 None</Output>

</div>
</Grid>

<!--
강사용 원인(학생 자료에는 없음):
B-3 마지막 원소 누락. 738 = 839 - 101(일요일). range(len(sales))로 고친다. LAB-03 B-1(range 끝 값)과 같은 종류다.
B-4 append는 원본을 바꾸고 아무것도 돌려주지 않음. sales.append(150) 뒤에 sales를 출력한다. B-1의 sort()도 같은 성질이라는 점을 ⑭ 비교표에서 확인하게 한다.
-->

---
class: dense
---

## #10. ⑭ 두 방법 비교받기

<Callout icon="💡" title="비슷한 두 방법이 있는데 차이를 모르겠어서, 차이를 표로 받고 각 칸을 직접 실행해 확인하고 싶은 경우" color="pastel-2"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2">

````md
## 맥락
파이썬 리스트 관련 함수 단원을 배우는 중이야.

## 상황
요일별 판매량 리스트를 정렬하고 싶은데 sorted()와 sort()가 둘 다 있어.
내가 아는 차이: {내가 아는 것. 모르면 "모르겠음"}

## 질문
두 방법의 차이를 비교해 주고, 원본 리스트를 그대로 둬야 할 때는 어느 쪽인지 알려줘.

## 제약
- 리스트 단원 범위(len · sorted · sort · copy · 슬라이싱) 안에서 설명해
- 각 차이마다 내가 직접 실행해 확인할 방법을 말로 알려줘

## 출력 형식
| 비교 항목 | sorted() | sort() | 확인 방법 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 사용 방법</h3>

- 내가 아는 차이를 먼저 적는다. 몰라도 "모르겠음"
- "확인 방법" 칸을 하나씩 실행하고, 맞으면 ✔, 다르면 실제 결과를 적는다

</div>

<Callout kind="warn" title="주의">
표만 받고 끝내지 않는다. ✔ 표시가 붙은 비교표가 오늘의 결과물이다
</Callout>

</div>
</Grid>

<!--
새 템플릿 ⑭. B-1(sort 후 요일이 틀림)을 고친 직후에 쓰면 질문이 구체적이다. AI 답에서 기대하는 비교 항목: 원본을 바꾸는지, 돌려주는 값(sort()는 None — B-4의 append와 같은 성질), 쓰는 모양(함수 vs 리스트 뒤에 점).
확인 방법을 학생이 실행했을 때 AI 설명과 다르면 실행 결과가 정답이다. 같은 틀로 append와 extend, 대입과 copy()도 비교할 수 있다.
-->

---
layout: section
---

# C. 에러 수정

25분. 에러 원문을 그대로 보내 원인을 받고, 고치는 건 내가 한다

---

## #11. C-1 · C-2 — 없는 위치, 없는 값

<Grid cols="2" align="start">
<div>

<div class="kicker">C-1 · 인덱스로 전부 출력</div>

```python
for i in range(len(sales) + 1):
    print(sales[i])
```

<Output label="에러">IndexError: list index out of range</Output>

</div>
<div>

<div class="kicker ai">C-2 · 값의 위치 찾기</div>

```python
print(sales.index(200))
```

<Output label="에러">ValueError: 200 is not in list</Output>

</div>
</Grid>

<Flow color="pastel">
<li><carbon:play /><b>실행</b>에러 원문 확인</li>
<li><carbon:chat /><b>⑩</b>코드와 에러 전체를 보낸다</li>
<li><carbon:edit /><b>수정</b>가리킨 줄을 내가 고친다</li>
<li><carbon:renew /><b>⑪</b>같은 실수가 나는 다른 경우</li>
</Flow>

<!--
강사용 원인(학생 자료에는 없음):
C-1 마지막 인덱스는 len - 1. sales는 7개라 인덱스 7은 없다. 출력이 7개 찍힌 뒤 에러가 난다는 점을 짚는다.
C-2 없는 값 검색. in으로 먼저 확인하고 index를 부른다.
-->

---
layout: magazine
---

## #12. C-3 — 문자열 숫자의 합계

문자열로 된 숫자를 그대로 sum에 넣었다.

```python
print(sum(["120", "95"]))
```

<Output label="에러">TypeError: unsupported operand type(s) for +: 'int' and 'str'</Output>

::right::

<Callout kind="ai" title="에러 원문 읽기">
마지막 줄에 <b>어떤 연산</b>(+)이 <b>어떤 두 자료형</b>('int'와 'str') 사이에서 막혔는지가 적혀 있다. 이 줄을 그대로 ⑩에 붙인다
</Callout>

<Callout kind="tip" title="고친 뒤">
⑪로 같은 에러가 나는 다른 경우를 받고, 하나를 직접 만들어 실행해 본다
</Callout>

<!--
강사용 원인(학생 자료에는 없음): 문자열 숫자는 int로 바꿔야 함. 반복문으로 하나씩 int로 바꿔 새 리스트를 만든 뒤 sum한다.
에러 메시지에 'int'가 먼저 나오는 이유: sum은 0에서 시작해 첫 원소를 더한다. 학생이 물으면 설명하되 길게 끌지 않는다. LAB-08에서 CSV를 읽으면 모든 값이 문자열이라 같은 에러를 다시 만난다.
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

<Tile kind="fill" color="py" tag="A" title="A-1 ~ A-4 풀이">
기본 통계 · 조건 탐색 · 3일 이동평균 · 2차원 합계. 정답과 같은 값이 나온 코드
</Tile>

<Tile kind="fill" color="ai" tag="B · ⑭" title="sort · sorted 비교표">
"확인 방법" 칸을 직접 실행해 ✔ 또는 실제 결과를 적은 표
</Tile>

<Tile kind="fill" color="ok" tag="템플릿" title="⑭ 두 방법 비교받기">
「내 프롬프트 템플릿.md」의 ⑬ 뒤에 추가하고, 오늘 고친 실수 한 줄을 함께 기록한다
</Tile>

<Core color="ai">AI의 답은 추측. 내 코드를 직접 실행한 결과가 정답이다.</Core>

<!--
결과물은 걷지 않고 확인만 한다. 비교표에 ✔만 있고 실행 흔적이 없으면 한 칸을 골라 그 자리에서 실행해 보게 한다.
데이터 분석 연결: 리스트 하나는 표의 한 열이다. LAB-08에서 CSV의 열을 꺼내 같은 계산을 한다.
LAB-04-3 · 6은 교안에 연습문제가 없다. A · B가 그 역할을 한다.
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-04] 리스트 7 · ITWILL · {teacher} 강사</p>

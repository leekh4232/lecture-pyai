---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 딕셔너리 — 그룹별로 모아 세기
layout: cover
---

# 그룹별로 모아 세기 — 딕셔너리

주문 기록을 지점별 · 품목별로 모아 더하고, 중첩 구조에서 원하는 값까지 가는 경로를 점검받는 연습

<p class="sub">[LAB-06] 딕셔너리 3 · ITWILL · {teacher} 강사</p>

<!--
딕셔너리 단원 1~2(딕셔너리의 이해 · 딕셔너리 관련 함수)를 마친 뒤 하는 ChatGPT 학습활동. ① 조언 받기 단계(LAB-02 ~ 06)의 마지막 실습이다. 코드는 학생이 쓰고, ChatGPT는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 맡는다(「ChatGPT 지침.md」 그대로).
오늘 새로 만드는 템플릿은 ⑯ 값까지 가는 경로 묻기. 다음 LAB-07부터는 AI에게 코드를 직접 받는 단계로 넘어가므로, 조언 받기 단계를 마무리하는 시간이기도 하다.
-->

---
layout: infographic
---

## #01. 오늘의 진행 — 2교시 약 100분

<Grid cols="4" gap="16">
<Stat value="40" unit="분" label="A 구현" color="py">문제를 직접 푼다. 막히면 템플릿으로 조언을 받는다</Stat>
<Stat value="25" unit="분" label="B 결과가 이상할 때" color="ai">나눠 준 코드의 틀린 값을 찾아 고친다</Stat>
<Stat value="25" unit="분" label="C 에러 수정" color="ok">에러 코드의 원인을 찾아 고친다</Stat>
<Stat value="10" unit="분" label="D 정리" color="py">새 템플릿 ⑯ 추가, 오늘 고친 실수 한 줄 기록</Stat>
</Grid>

<Core color="ai">코드는 내가 쓰고, AI는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 맡는다</Core>

<!--
진행은 ① 조언 받기 단계 공통 진행 그대로다. B · C의 코드는 미리 준비해 나눠 준다. 강사용 원인은 각 쪽 발표자 노트에만 있다.
시간이 모자라도 A-4와 템플릿 ⑯은 빼지 않는다.
-->

---

## #02. 오늘의 규칙과 `## 제약` 범위

<Callout kind="real" title="오늘의 규칙">

- 코드는 내가 쓰고, AI에게는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 묻는다
- 프롬프트는 다섯 섹션 `## 맥락` `## 상황` `## 질문` `## 제약` `## 출력 형식`
- `## 제약`에는 아래 표의 배운 범위를 적는다

</Callout>

<div class="kicker">딕셔너리 단원 · <code>## 제약</code>에 쓰는 범위</div>

| 단원 | 범위 |
|:--|:--|
| 1 딕셔너리의 이해 | 키 · 값, 확장, key 중복, 딕셔너리를 원소로 갖는 리스트 등 복합 구조 |
| 2 딕셔너리 관련 함수 | len · del, get · keys · values · items · update · copy · clear |

<!--
시작 전에 ChatGPT 맞춤 지침이 「ChatGPT 지침.md」로 들어 있는지 말로 확인한다. AI가 코드를 통째로 주면 지침이 빠진 것이므로 설정을 확인하고 새 대화에서 다시 시작하게 한다.
오늘 쓰는 모든 프롬프트의 ## 제약은 이 표에서 가져온다.
-->

---

## #03. 연습 데이터

<Grid cols="3fr 2fr" align="start">
<div>

<div class="kicker">orders · 주문 기록 여섯 건</div>

```python
orders = [
    {"store": "강남", "item": "커피",   "qty": 3, "price": 4500},
    {"store": "홍대", "item": "커피",   "qty": 2, "price": 4500},
    {"store": "강남", "item": "케이크", "qty": 1, "price": 6000},
    {"store": "홍대", "item": "티",     "qty": 4, "price": 4000},
    {"store": "강남", "item": "티",     "qty": 2, "price": 4000},
    {"store": "잠실", "item": "커피",   "qty": 5, "price": 4500},
]
```

</div>
<div>

<div class="kicker">report · 지점별 판매 보고</div>

```python
report = {"date": "2024-01-05",
          "stores": [{"name": "강남", "sales": {"coffee": 12, "tea": 5}},
                     {"name": "홍대", "sales": {"coffee": 8,  "tea": 9}}]}
```

<Callout kind="tip" title="쓰는 곳">
orders는 A-1 ~ A-3, report는 A-4와 템플릿 ⑯
</Callout>

</div>
</Grid>

<!--
두 데이터를 노트북 첫 셀에 그대로 붙여 넣고 시작하게 한다. orders는 "딕셔너리를 원소로 갖는 리스트", report는 딕셔너리 안에 리스트, 그 안에 다시 딕셔너리가 든 복합 구조다.
-->

---
layout: section
---

# A. 구현

문제를 직접 푼다. 막히면 「내 프롬프트 템플릿.md」에서 템플릿을 꺼내 조언을 받는다 · 40분

---

## #04. A-1 지점별 매출 합계

<div class="kicker">orders에서 지점별 매출 합계(수량 × 가격)를 딕셔너리로 만든다</div>

<Flow color="pastel">
<li><b>주문 한 건</b>지점 · 수량 · 가격 꺼내기</li>
<li><b>매출</b>수량 × 가격</li>
<li><b>지점별 누적</b>그 지점의 합계에 더한다</li>
<li><b>결과</b>지점이 key인 딕셔너리</li>
</Flow>

<Output label="정답">

```text
{'강남': 27500, '홍대': 25000, '잠실': 22500}
```

</Output>

<Callout kind="ai" title="막히면 ⑤ 단계로 쪼개기">
LAB-02의 ⑤를 꺼내 처음부터 끝까지 해야 할 일을 단계 순서로 받고, 한 단계씩 쓰고 실행해 확인한다
</Callout>

<!--
처음 나온 지점은 key를 새로 만들고, 이미 있는 지점은 기존 값에 더한다. get()이나 in으로 처리할 수 있다. 강남 = 3×4500 + 1×6000 + 2×4000 = 27500.
여기서 "="로 덮어쓰는 실수가 B-1이다.
-->

---

## #05. A-2 품목별 판매 수량 · A-3 매출 1위 지점

<Grid cols="2" align="start">
<div>

<Tile kind="soft" color="py" tag="A-2" title="품목별 판매 수량">

orders에서 품목(item)별로 수량(qty)을 모아 더한다

</Tile>

<Output label="정답">

```text
{'커피': 10, '케이크': 1, '티': 6}
```

</Output>

</div>
<div>

<Tile kind="soft" color="ai" tag="A-3" title="매출 1위 지점">

A-1 결과에서 가장 큰 값의 지점을 찾는다

</Tile>

<Stat value="강남" label="정답" color="ai" />

</div>
</Grid>

<Core color="ok">A-2는 A-1과 같은 모양. 묶는 기준(key)과 더하는 값만 바뀐다</Core>

<!--
A-2: key가 store에서 item으로, 더하는 값이 qty × price에서 qty로 바뀔 뿐 A-1과 같은 구조다. 커피 3 + 2 + 5 = 10.
A-3: items()로 key와 value를 함께 돌며 가장 큰 값을 기억해 두는 방식이 배운 범위 안에서 자연스럽다.
-->

---

## #06. A-4 중첩 구조 꺼내기

<Grid cols="3fr 2fr" align="center">
<div>

<div class="kicker">report에서 전체 지점의 coffee 판매량 합계를 구한다</div>

```python
report = {"date": "2024-01-05",
          "stores": [{"name": "강남", "sales": {"coffee": 12, "tea": 5}},
                     {"name": "홍대", "sales": {"coffee": 8,  "tea": 9}}]}
```

<p>들어가는 순서 <Chip>report</Chip> → <Chip color="ai">"stores"</Chip> → <Chip kind="dashed" color="muted">?</Chip> → <Chip kind="dashed" color="muted">?</Chip> → <Chip color="ok">"coffee"</Chip></p>

</div>
<div>

<Stat value="20" label="정답 · coffee 합계" color="ok" />

<Callout kind="ai" title="막히면 새 템플릿 ⑯">
값까지 가는 경로를 내가 먼저 적고 점검받는다. 다음 쪽에서 만든다
</Callout>

</div>
</Grid>

<!--
report["stores"]는 리스트, 그 원소는 딕셔너리, 그 안의 "sales"가 다시 딕셔너리다. 지점마다 sales의 coffee를 꺼내 더하면 12 + 8 = 20.
물음표 두 칸은 학생이 채우는 자리다(리스트의 원소 → "sales"). 이 구조는 LAB-12 OpenAPI의 JSON 응답과 같은 모양이다.
-->

---
class: dense
---

## #07. 새 템플릿 ⑯ 값까지 가는 경로 묻기

<Callout icon="💡" title="중첩 구조에서 원하는 값까지 몇 단계로 들어가는지 내가 먼저 적고 점검받고 싶은 경우" color="pastel-2"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2">

````md
## 맥락
파이썬 딕셔너리 단원을 배우는 중이야.

## 상황
아래 구조에서 홍대 지점의 tea 판매량(9)을 꺼내고 싶어.
{report 구조 붙여 넣기}
내가 생각한 경로: report → "stores" → {내 생각} → ...

## 질문
내 경로가 맞는지, 틀렸다면 몇 번째 단계에서 무엇이 틀렸는지 알려줘. 단계마다 그 단계의 값이 딕셔너리인지 리스트인지도 알려줘.

## 제약
- 코드 대신 단계와 자료형으로 설명해
- 딕셔너리 · 리스트 범위 안에서 설명해

## 출력 형식
| 단계 | 들어가는 방법(key 또는 인덱스) | 그 단계 값의 자료형 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 사용 방법</h3>

- 받은 단계를 한 단계씩 `print(type(...))`로 확인하며 코드를 쓴다

</div>

<Callout kind="warn" title="주의">
{내 생각}을 비워 두고 보내지 않는다. 경로를 먼저 적어야 점검을 받는다
</Callout>

</div>
</Grid>

<!--
템플릿 ⑯은 "내가 먼저 적고 점검받는" 조언 받기 단계의 마지막 새 템플릿이다. 지침 때문에 코드는 오지 않고 단계와 자료형이 표로 온다.
학생이 자주 막히는 곳: report["stores"]가 리스트라서 "홍대"를 key로 넣으려는 경우. 그 단계에서 들어가는 방법은 인덱스(1)다. 단계마다 type()을 찍으면 dict → list → dict → dict 순서가 보인다.
-->

---
layout: section
---

# B. 결과가 이상할 때

에러는 안 나는데 값이 틀렸다. 나눠 준 코드의 틀린 값을 찾아 고친다 · 25분

---

## #08. B-1 지점별 합계가 이상하다

<Grid cols="3fr 2fr" align="start">
<div>

```python
totals = {}
for o in orders:
    store = o["store"]
    qty = o["qty"]
    price = o["price"]
    totals[store] = qty * price
print(totals)
```

<Output label="실행 결과">

```text
{'강남': 8000, '홍대': 16000, '잠실': 22500}
```

</Output>

</div>
<div>

<Output label="기대한 값 · A-1 정답">

```text
{'강남': 27500, '홍대': 25000, '잠실': 22500}
```

</Output>

<Callout kind="tip" title="막히면">
짐작이 있으면 ⑧ 내 추측 확인 방법 묻기, 없으면 ⑦ 확인할 곳 묻기
</Callout>

</div>
</Grid>

<!--
강사용 원인: = 는 덮어쓰기다. 누적은 기존 값에 더해야 한다. 그래서 각 지점의 마지막 주문 매출만 남는다(강남 티 2 × 4000 = 8000, 홍대 티 4 × 4000 = 16000). 잠실은 주문이 한 건이라 우연히 맞는다.
⑦로 보내면 반복마다 totals를 찍어 보라는 답이 오는지 본다. 찍어 보면 강남 값이 13500 → 6000 → 8000으로 바뀌는 것이 보인다.
-->

---

## #09. B-2 앞의 값이 사라졌다

<Grid cols="2" align="center">
<div>

<div class="kicker">같은 key를 두 번 써서 딕셔너리를 만든다</div>

```python
prices = {"커피": 4500, "티": 4000, "커피": 5000}
print(prices)
```

<Output label="실행 결과">

```text
{'커피': 5000, '티': 4000}
```

</Output>

</div>
<div>

<Tile kind="fill" color="warn" tag="증상" title="앞의 값이 사라짐">

처음 넣은 `"커피": 4500`이 결과에 없다. 에러도 나지 않는다

</Tile>

</div>
</Grid>

<Core color="ai">에러 없이 값이 사라지는 경우는 실행 결과를 눈으로 대조해야 찾는다</Core>

<!--
강사용 원인: key는 중복될 수 없다. 같은 key를 두 번 쓰면 뒤의 값이 남는다. 딕셔너리의 이해 단원 "key 중복" 재료.
-->

---
layout: section
---

# C. 에러 수정

빨간 글씨가 떴다. 에러 코드의 원인을 찾아 고친다 · 25분

---

## #10. C 진행 방법과 C-1

<Steps color="ok">
<li>나눠 준 코드를 내 노트북에서 실행한다</li>
<li><b>⑩ 에러 원문 보내기</b>로 코드와 에러 메시지 전체를 그대로 붙인다</li>
<li>원인과 고치는 방향만 받고, 수정은 <b>내가</b> 한다</li>
<li><b>⑪ 같은 실수 막기</b>로 같은 에러가 나는 다른 경우를 받아 하나를 직접 만든다</li>
</Steps>

<Grid cols="2" align="center">
<div>

<div class="kicker">C-1 · totals는 A-1의 결과</div>

```python
totals["신촌"]
```

</div>
<div>

<Output label="에러">

```text
KeyError: '신촌'
```

</Output>

</div>
</Grid>

<!--
강사용 원인 C-1: 없는 key를 꺼냈다. get()으로 꺼내거나 in으로 먼저 확인한다.
get()은 없는 key면 None(또는 지정한 기본값)을 돌려준다는 점을 실행으로 확인하게 한다.
-->

---

### #10-1. C-2 · C-3 코드와 에러

<Grid cols="2" align="start">
<div>

<div class="kicker">C-2</div>

```python
{["강남", "커피"]: 3}
```

<Output label="에러">

```text
TypeError: unhashable type: 'list'
```

</Output>

</div>
<div>

<div class="kicker">C-3 · totals는 A-1의 결과</div>

```python
for k in totals:
    del totals[k]
```

<Output label="에러">

```text
RuntimeError: dictionary changed size during iteration
```

</Output>

</div>
</Grid>

<!--
강사용 원인
C-2: 리스트는 key가 될 수 없다. 튜플은 가능하다(("강남", "커피")).
C-3: 반복하는 도중에 딕셔너리의 크기를 바꾸면 안 된다. 첫 번째 del 직후 다음 반복에서 에러가 난다.
파이썬 버전에 따라 C-2의 메시지 문장이 조금 다를 수 있다. 학생 화면의 원문을 그대로 붙이게 한다.
-->

---
layout: section
---

# D. 정리

새 템플릿을 모으고 오늘 고친 실수를 기록한다 · 10분

---
layout: magazine
---

## #11. 오늘의 결과물

A-1 ~ A-4 풀이와 템플릿 ⑯. 「내 프롬프트 템플릿.md」에 ⑯을 추가하고 오늘 고친 실수를 한 줄 기록한다

<Steps color="py">
<li><b>A-1 ~ A-4 풀이</b> 지점별 합계 · 품목별 수량 · 1위 지점 · 중첩 구조</li>
<li><b>템플릿 ⑯</b> 값까지 가는 경로 묻기</li>
<li><b>실수 한 줄</b> 오늘 고친 실수 기록</li>
</Steps>

::right::

<Tile kind="soft" color="ai" tag="데이터 분석으로" title="key별로 더하기">

A-1의 "key별로 더하기"는 pandas `groupby`의 원리다

</Tile>

<Tile kind="soft" color="ok" tag="데이터 분석으로" title="중첩 구조">

A-4 구조는 LAB-12 OpenAPI의 JSON 응답과 같은 모양이다

</Tile>

<!--
결과물은 걷지 않고, 「내 프롬프트 템플릿.md」에 ⑯까지 들어갔는지만 둘러보며 확인한다. 이것으로 조언 받기 단계의 템플릿 ①~⑯이 모두 모인다.
-->

---

## #12. 다음 LAB 예고 — 조언 받기에서 답 받기로

<Timeline color="ai">
<li><b>LAB-02 ~ 06</b>조언 받기 · 코드는 내가 쓰고 AI는 개념 · 순서 · 원인</li>
<li class="now"><b>오늘 LAB-06</b>조언 받기 단계의 마지막 템플릿 ⑯</li>
<li><b>LAB-07 ~</b>답 받기 · AI에게 코드를 직접 받는다</li>
</Timeline>

<Core color="ai">LAB-07부터는 AI에게 코드를 직접 받는 단계로 넘어간다</Core>

<!--
다음 LAB 예고. 자세한 내용(지침 바꾸기, 받은 코드 4단 확인)은 LAB-07-2 「AI에게 답을 받는 법」 개요 덱에서 다룬다. 여기서는 단계가 바뀐다는 것만 알린다.
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-06] 딕셔너리 3 · ITWILL · {teacher} 강사</p>

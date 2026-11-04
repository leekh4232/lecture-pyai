---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 객체지향 — 클래스로 기록 관리하기
layout: cover
---

# 클래스로 기록 관리하기 — SalesBook 만들기

판매 기록 클래스를 답으로 받고, 줄마다 설명하고, 변형 문제를 AI 없이 푸는 연습

<p class="sub">[LAB-09] 객체지향 3 · ITWILL · {teacher} 강사</p>

<!--
「클래스와 객체」「self와 생성자」를 마친 뒤 하는 ② 답 받기 단계의 마지막 실습. 지침은 「ChatGPT 지침(답 받기).md」.
결과물: A-1 ~ A-3 코드(4단 확인 표시), 변형 문제 풀이, 템플릿 ⑳ · ㉑.
새 템플릿은 둘. ⑳은 4단 확인의 ③ 설명을, ㉑은 ④ 변형을 AI로 돕는 템플릿이다. ⑰ · ⑱ · ⑲는 다시 가르치지 않고 번호로만 부른다.
-->

---

## #01. 오늘의 진행 — 답 받기 단계의 마지막

<Timeline color="ok">
<li><b>A 구현 · 40분</b>15분 직접 시도 → 답 받기 → 4단 확인</li>
<li><b>B 결과가 이상할 때 · 25분</b>"AI 답"의 함정 찾기</li>
<li><b>C 에러 수정 · 25분</b>받은 코드를 고치다 나는 에러</li>
<li><b>D 정리 · 10분</b>템플릿 ⑳ · ㉑ 추가 · 오늘 고친 실수 한 줄</li>
</Timeline>

<Callout kind="real" title="오늘의 규칙">

- 지침은 「ChatGPT 지침(답 받기).md」. 코드를 받되, 받은 코드는 내가 검증한다
- 문제마다 **15분 직접 시도**. 막힌 코드를 `## 내 시도`에 붙여 답을 받는다
- 프롬프트는 여섯 섹션. `## 맥락` `## 상황` `## 내 시도` `## 질문` `## 제약` `## 출력 형식`
- 정답은 내 노트북 실행 결과

</Callout>

<!--
LAB-07 · 08과 같은 진행. 오늘은 두 새 템플릿이 4단 확인의 ③ · ④와 짝을 이룬다는 점을 처음에 말해 둔다.
-->

---

## #02. 4단 확인과 오늘의 새 템플릿

<Steps color="pastel">
<li><b>① 실행</b> 내 노트북에서 실행해 정답과 대조한다. 정답과 같은 값이면 통과</li>
<li><b>② 범위</b> 배우지 않은 문법이 있는지 본다. 모두 배운 문법이면 통과</li>
<li><b>③ 설명</b> 줄마다 무슨 일을 하는지 말로 설명한다. <Chip color="ai" kind="outline">⑳ 받은 코드 설명 점검받기</Chip></li>
<li><b>④ 변형</b> 조건 하나를 바꾼 변형 문제를 AI 없이 푼다. <Chip color="ok" kind="outline">㉑ 변형 문제 받기</Chip></li>
</Steps>

<Grid cols="2">
<Tile kind="soft" color="ai" tag="⑳" title="내 설명을 점검받는다">
받은 코드를 내가 줄마다 설명하고, 설명이 맞는지 점검받는다. ③을 AI로 점검하는 방법
</Tile>
<Tile kind="soft" color="ok" tag="㉑" title="정답 코드 없이 문제만">
받은 코드를 내가 쓸 수 있는지 확인하는 문제를 받는다. 정답 코드는 받지 않는다
</Tile>
</Grid>

<!--
⑳ · ㉑ 모두 "AI가 코드를 주는" 템플릿이 아니라 "내가 한 일을 점검받는" 템플릿이다. 답 받기 단계에서도 마지막 판단은 학생이 한다는 점을 다시 짚는다.
-->

---

## #03. `## 제약`에 적는 범위

| 단원 | 범위 |
|:--|:--|
| 1 클래스와 객체 | 클래스 정의, 멤버변수, 메서드, 객체 생성 · 사용 |
| 2 self와 생성자 | self, 메서드로 멤버변수 설정, 생성자(`__init__`) |
| 이전 LAB | 조건문 · 반복문 · 리스트 · 문자열 · 딕셔너리 · 함수 · 예외처리 · 파일입출력 |

<Callout kind="warn" title="범위 밖 문법이 나오면">
무엇인지 묻고, 배운 문법으로 다시 요청한다. 값이 맞아도 ② 범위는 따로 확인한다
</Callout>

<!--
클래스 단원은 AI가 타입 힌트 · 데코레이터 같은 범위 밖 문법을 섞기 쉬운 곳이다. B의 함정 ②가 그 예다.
-->

---
layout: section
---

# A. 구현

15분 직접 시도 → 답 받기 → 받은 코드 4단 확인

---
layout: magazine
---

## #04. A-1 판매 기록 클래스 `SalesBook`

지점 하나의 판매 기록을 담는 클래스를 만든다.

- **생성자**: 지점 이름을 받고, 판매 기록 리스트를 빈 리스트로 만든다
- `add(amount)`: 판매 금액 추가
- `total()`: 합계
- `average()`: 평균. 기록이 없으면 0

<p>템플릿 <Chip color="py">⑰ 코드 받기</Chip><Chip color="ai">⑳ 받은 코드 설명 점검받기</Chip></p>

::right::

<div class="kicker">확인 · 강남점에 120, 95, 143 추가</div>

<Grid cols="2" gap="8 16">
<Stat value="358" label="total()" />
<Stat value="119.3" label="average()" color="ai" />
</Grid>

<Callout kind="ai" title="④ 변형 — AI 없이 직접">
<code>max_sale()</code> 메서드를 추가한다. 가장 큰 금액, 기록이 없으면 <code>None</code>. 강남점이면 <code>143</code>
</Callout>

<!--
⑰로 받을 때 ## 상황에 위 요구 조건을 그대로 적고, ## 내 시도에 15분 동안 쓴 클래스를 붙인다.
119.3은 358 ÷ 3 = 119.333…을 소수 첫째 자리로 본 값이다.
④ 변형 max_sale()은 AI 없이 추가해야 한다. 기록이 없을 때 None을 돌려주는 조건을 빼먹는 학생이 많다. average()의 "기록이 없으면 0"과 같은 구조이므로 그 줄을 설명할 수 있었는지가 드러난다.
-->

---
class: dense
---

## #05. 템플릿 ⑳ 받은 코드 설명 점검받기

<Callout icon="💡" title="받은 코드를 내가 줄마다 설명하고, 설명이 맞는지 점검받는다. 4단 확인의 ③을 AI로 점검하는 방법" color="pastel-2"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2">

````md
## 맥락
파이썬 객체지향 단원을 배우는 중이야.

## 상황
아래는 네가 준 SalesBook 코드야.
{받은 코드}

내 설명:
| 줄 | 내가 이해한 내용 |
| def __init__(self, name): | 객체를 만들 때 지점 이름을 받는다 |
| ... | ... |

## 질문
내 설명에서 틀리거나 빠진 줄을 짚어 줘.

## 제약
- 코드를 다시 쓰지 마
- 맞은 줄은 "맞음"만 적어

## 출력 형식
| 줄 | 맞음/틀림 | 틀린 이유 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 사용 방법</h3>

- 받은 코드의 모든 줄에 내 설명을 먼저 채운다
- "틀림"이 나온 줄만 다시 공부하고 설명을 고친다
- 같은 대화에서 보내면 "네가 준 코드"가 이어진다

</div>

<Callout kind="warn" title="주의">
설명 칸을 비워 두고 보내면 점검이 아니라 해설을 받게 된다. 코드를 다시 쓰지 말라는 제약도 빼지 않는다
</Callout>

</div>
</Grid>

<!--
⑳은 LAB-02의 ② 내 설명 점검받기를 코드 한 줄 단위로 넓힌 것이다. 학생이 가장 많이 틀리는 줄: self.records = []가 "객체마다 따로 리스트를 만든다"는 점, self.records.append(amount)에서 self가 가리키는 대상. 이 두 줄을 설명하지 못하면 B의 함정 ①을 찾지 못한다.
-->

---
layout: infographic
---

## #06. A-2 객체 두 개

<Callout icon="🏬" title="강남점 · 홍대점 객체를 만들어 각각 기록하고, 기록이 섞이지 않는지 확인한다" color="pastel-3"></Callout>

<Grid cols="2">
<Tile color="py" tag="객체 1" title="강남점">
120, 95, 143을 추가한다. 합계 358, 평균 119.3
</Tile>
<Tile color="ai" tag="객체 2" title="홍대점">
다른 금액을 추가한다. 강남점의 금액이 보이면 안 된다
</Tile>
</Grid>

<Steps color="ok">
<li>두 객체의 판매 기록 리스트를 각각 출력한다</li>
<li>한쪽에만 <code>add()</code>를 한 뒤 다른 쪽이 그대로인지 본다</li>
</Steps>

<!--
A-2는 B의 함정 ①(클래스 본문의 records = [])을 미리 잡는 확인이다. 객체 하나로만 시험하면 그 함정은 드러나지 않는다.
홍대점 금액은 학생이 정한다. 원고에 지정된 값은 없다.
-->

---
layout: magazine
---

## #07. A-3 자기 점검

템플릿 ㉑ 변형 문제 받기로 LAB-07 ~ 09 범위의 변형 문제 **두 개**를 받아 AI 없이 푼다.

- 완성한 SalesBook 코드를 `{완성한 코드}`에 붙인다
- 정답 코드는 받지 않는다. 문제와 확인할 정답 값만
- 푼 뒤 내 노트북 결과를 정답 값과 대조한다

::right::

<Flow color="ok">
<li><b>㉑로 문제 받기</b>두 문제</li>
<li><b>AI 없이 풀기</b>내 노트북</li>
<li><b>정답 값 대조</b>같으면 통과</li>
</Flow>

<Core color="ok">변형을 AI 없이 풀 수 있어야 받은 코드가 내 코드다</Core>

<!--
LAB-07부터 가장 자주 건너뛰는 것이 ④ 변형이다. A-3은 그것을 문제 하나로 만든 것. 학생이 문제를 받고 다시 ⑰로 정답 코드를 받으면 의미가 없다. AI 없이 풀었는지 꼭 확인한다.
㉑의 정답 값도 AI가 계산한 것이라 틀릴 수 있다. 내 풀이와 다르면 둘 다 의심하고, 손 계산이나 다른 방법으로 확인한다.
-->

---
class: dense
---

## #08. 템플릿 ㉑ 변형 문제 받기

<Callout icon="💡" title="받은 코드를 내가 쓸 수 있는지 확인하는 문제를 받는다. 정답 코드는 받지 않는다" color="pastel-5"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2">

````md
## 맥락
파이썬 LAB-07 ~ 09(예외처리 · 파일입출력 · 클래스)를 배웠어.

## 상황
SalesBook 클래스를 AI 답으로 완성하고 4단 확인까지 했어.
{완성한 코드}

## 질문
이 코드를 조금 바꿔야 풀 수 있는 변형 문제 2개를 내 줘.

## 제약
- 정답 코드는 주지 마. 문제와 확인할 정답 값만 줘
- 배운 범위 안에서 풀 수 있는 문제만

## 출력 형식
| 번호 | 문제 | 확인할 정답 값 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 사용 방법</h3>

- 4단 확인 ①~③을 마친 코드를 붙인다
- 받은 두 문제를 AI 없이 푼다
- 막히면 ⑰이 아니라 ⑱로, 내 코드를 고쳐 받는다

</div>

<Callout kind="warn" title="주의">
"정답 코드는 주지 마"를 빼면 문제와 답이 함께 온다. 받은 답을 보는 순간 변형 확인은 끝난다
</Callout>

</div>
</Grid>

<!--
LAB-02의 ⑫ 거꾸로 질문과 같은 방향이다. 그때는 개념 문제였고 지금은 코드를 바꿔야 하는 문제다.
-->

---
layout: section
---

# B. "AI 답"의 함정

실행은 되지만 틀린 값, 또는 맞는 값이지만 범위 밖. 강사가 미리 받아 둔 AI 답을 검증한다

---

## #09. 함정 ① 기록 리스트의 자리

<Grid cols="3fr 2fr" align="start">
<div>

```python
class SalesBook:
    records = []

    def __init__(self, name):
        self.name = name

    def add(self, amount):
        self.records.append(amount)

gangnam = SalesBook("강남점")
gangnam.add(120)
gangnam.add(95)
gangnam.add(143)

hongdae = SalesBook("홍대점")
print(hongdae.records)
```

</div>
<div>

<Output>[120, 95, 143]</Output>

<Callout kind="danger" icon="🔍" title="증상">
홍대점에는 아무것도 추가하지 않았는데 <b>강남점 기록이 섞여</b> 나온다
</Callout>

<Callout kind="tip" title="확인할 곳">
A-2처럼 객체 <b>두 개</b>로 시험해야 드러난다. <code>records</code>가 만들어지는 줄을 찾는다
</Callout>

</div>
</Grid>

<!--
강사용 원인: 클래스 본문의 리스트는 모든 객체가 함께 쓴다. 생성자에서 self.records = []로 만들어야 객체마다 따로 생긴다. 교안 9-1의 멤버변수 방식을 리스트에 쓰면 생기는 일이다.
객체 하나로만 확인하면 합계 358 · 평균 119.3이 모두 맞게 나와 ① 실행을 통과한다. 그래서 A-2가 필요하다.
-->

---

## #10. 함정 ② · ③ 값은 맞는데, 빈 객체에서는

<Grid cols="2" align="start">
<div>

<div class="kicker">AI 답 ② · 메서드 정의</div>

```python
def add(self, amount: int) -> None:
    self.records.append(amount)
```

<Callout kind="tip" icon="✔️" title="① 실행은 통과">
합계 358 · 평균 119.3 모두 맞음
</Callout>

<Callout kind="warn" title="4단 확인 ② 범위">
<code>: int</code> · <code>-&gt; None</code>이 #03 표에 있는지 대조한다
</Callout>

</div>
<div>

<div class="kicker">AI 답 ③ · 평균 메서드</div>

```python
def average(self):
    return self.total() / len(self.records)
```

<Callout kind="danger" icon="🔍" title="증상">
강남점에서는 맞지만, 기록이 없는 <b>빈 객체</b>에서 <code>average()</code>를 부르면 에러
</Callout>

<Callout kind="tip" title="확인할 곳">
요구 조건 "기록이 없으면 0"을 정답 대조 목록에 넣었는지
</Callout>

</div>
</Grid>

<!--
강사용 원인
- ② 타입 힌트. 값은 맞지만 ② 범위 밖 문법이다. 무엇인지 묻고, 배운 문법으로 다시 요청한다.
- ③ average()에서 기록이 없을 때 처리 누락. 요구 조건(기록이 없으면 0)을 정답 대조로 확인하지 않았다. 확인 목록에 강남점 값만 넣으면 놓친다. 빈 객체 하나를 만들어 average()를 부르는 것까지가 ① 실행이다.
-->

---
layout: section
---

# C. 에러 수정

받은 코드를 고치다 나는 에러를 고친다

---

## #11. 에러 ① · ② 메서드와 멤버변수

<Grid cols="2" align="start">
<div>

<div class="kicker">받은 코드를 고치다</div>

```python
def add(amount):
    self.records.append(amount)
```

<Output label="에러">TypeError: SalesBook.add() takes 1 positional argument but 2 were given</Output>

</div>
<div>

<div class="kicker">멤버변수 이름</div>

```python
def total(self):
    return sum(self.record)
```

<Output label="에러">AttributeError: 'SalesBook' object has no attribute 'record'</Output>

</div>
</Grid>

<Callout kind="tip">
에러 원문의 맨 아래 줄부터 읽는다. 에러가 가리키는 이름(<code>add</code> · <code>record</code>)을 내 클래스 정의와 하나씩 맞춰 본다
</Callout>

<!--
강사용 원인
- TypeError: 메서드의 첫 파라미터는 self. gangnam.add(120)은 객체 자신과 120, 두 개를 넘긴다. 정의는 하나만 받으므로 "1개를 받는데 2개가 왔다".
- AttributeError: 생성자에서 만든 이름은 self.records인데 self.record로 씀. 멤버변수 이름을 확인한다.
-->

---

## #12. 에러 ③ · ④ 생성자와 빈 객체

<Grid cols="2" align="start">
<div>

<div class="kicker">생성자 이름</div>

```python
class SalesBook:
    def _init_(self, name):
        self.name = name
        self.records = []

gangnam = SalesBook("강남점")
```

<Output label="에러">TypeError: SalesBook() takes no arguments</Output>

</div>
<div>

<div class="kicker">빈 객체에서 <code>average()</code></div>

```python
empty = SalesBook("신촌점")
print(empty.average())
```

<Output label="에러">ZeroDivisionError: division by zero</Output>

</div>
</Grid>

<Steps color="ai">
<li>에러 원문과 내가 생각한 원인을 먼저 적는다</li>
<li>스스로 못 고치면 템플릿 ⑱ 내 코드 고쳐 받기. <code>## 내 시도</code>에 내 생각을 쓴다</li>
</Steps>

<!--
강사용 원인
- _init_(밑줄 하나): 생성자 이름은 __init__(앞뒤 밑줄 두 개). 생성자가 없는 클래스로 취급되어 "인자를 받지 않는다"는 에러가 난다. 화면에서 밑줄 개수가 잘 안 보이므로 직접 세어 보게 한다.
- ZeroDivisionError: LAB-07 예외처리 또는 if로 대비. B의 함정 ③과 같은 원인이다.
"신촌점"은 빈 객체 예시로 쓴 이름이다.
-->

---
layout: section
---

# D. 정리

새 템플릿을 내 파일에 추가하고, 답 받기 단계를 마무리한다

---
layout: cards
cols: 3
---

## #13. 오늘의 결과물

<div class="py">

#### <carbon:code /> A-1 ~ A-3 코드

- 문제마다 4단 확인 표시
- `SalesBook` · 객체 두 개 · 자기 점검

</div>
<div class="ai">

#### <carbon:education /> 변형 문제 풀이

- A-1의 `max_sale()`
- ㉑로 받은 두 문제

</div>
<div class="ok">

#### <carbon:template /> 템플릿 ⑳ · ㉑

- 「내 프롬프트 템플릿.md」에 추가
- 오늘 고친 실수 한 줄 기록

</div>

<Callout kind="real" title="답 받기 단계 한 장으로 기억하기">
<b>먼저 직접 시도</b> 문제마다 15분, 막힌 코드를 <code>## 내 시도</code>에<br>
<b>배운 범위만</b> <code>## 제약</code>에 범위를 적고, 범위 밖이면 다시 요청<br>
<b>4단 확인</b> 실행 · 범위 · 설명(⑳) · 변형(㉑)을 통과해야 내 코드<br>
<b>템플릿</b> ⑰ 코드 받기 · ⑱ 내 코드 고쳐 받기 · ⑲ 데이터 정보와 함께 받기 · ⑳ · ㉑
</Callout>

<!--
LAB-07 ~ 09의 답 받기 단계가 여기서 끝난다. 템플릿은 ⑰ ~ ㉑ 다섯 개가 「내 프롬프트 템플릿.md」에 모였는지 확인한다.
-->

---

## #14. 다음 단계 — LAB-10부터 에이전트

<Timeline color="ai">
<li><b>① 조언 받기 · LAB-02 ~ 06</b>AI는 개념 · 순서 · 원인, 코드는 내가</li>
<li class="now"><b>② 답 받기 · LAB-07 ~ 09</b>AI가 코드를 쓰고, 검증은 내가</li>
<li><b>③ 에이전트 · LAB-10 ~ 13</b>에이전트가 파일을 만들고 고치고 실행, 검토는 내가</li>
</Timeline>

| | 답 받기 (LAB-07 ~ 09) | 에이전트 (LAB-10 ~) |
|:--|:--|:--|
| AI가 주는 것 | 코드 + 줄별 설명 | 파일 작업 결과 |
| 내 일 | 실행 · 검증 · 설명 | 지시 · 검토 · 승인 |

<Callout kind="ai" title="이어지는 것">
에이전트는 받은 코드를 검증하는 일을 파일 단위로 넓힌 것. pandas의 <code>df.head()</code>, <code>df.shape</code>도 객체의 메서드와 속성이다
</Callout>

<!--
다음 LAB부터 에이전트 단계로 넘어간다. LAB-07 ~ 09에서 "받기 → 실행 → 검증"을 코드 조각 단위로 익혔고, 에이전트가 만드는 여러 파일 · 모듈 · 설치를 검토하려면 LAB-10의 모듈 · 패키지 · 파일 · 폴더 내용이 필요하다.
LAB-10 마지막에 개요 덱 「에이전틱 AI로 일하는 법」이 있다. 도구 이름과 사용법은 그때 다룬다.
오늘 배운 클래스 · 객체 · 메서드 · 속성이 LAB-10 이후 pandas를 읽는 기초가 된다.
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-09] 객체지향 3 · ITWILL · {teacher} 강사</p>

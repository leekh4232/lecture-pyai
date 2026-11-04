---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 문자열 — 텍스트 값 정제하기
layout: cover
---

# 텍스트 값 정제하기 — 문자열

쉼표 · 공백이 섞인 문자열을 숫자와 문장으로 바꾸고, AI가 알려 준 방법을 공식 문서에서 확인하는 연습

<p class="sub">[LAB-05] 문자열 4 · ITWILL · {teacher} 강사</p>

<!--
문자열 단원 1~3(문자열의 이해 · 문자열 포메팅 · 문자열 관련 함수)을 마친 뒤 하는 ChatGPT 학습활동. ① 조언 받기 단계(LAB-02 ~ 06)의 네 번째 실습이다. 코드는 학생이 쓰고, ChatGPT는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 맡는다(「ChatGPT 지침.md」 그대로).
오늘 새로 만드는 템플릿은 ⑮ 근거와 함께 묻기. AI가 알려 준 메서드 · 형식이 실제로 있는지 공식 문서에서 확인하는, 환각을 직접 잡아 보는 첫 활동이다.
-->

---

## #01. 오늘의 진행 — 2교시 약 100분

<Timeline color="ok">
<li><b>A 구현 · 40분</b>문제를 직접 푼다. 막히면 템플릿으로 조언을 받는다</li>
<li><b>B 결과가 이상할 때 · 25분</b>나눠 준 코드의 틀린 값을 찾아 고친다</li>
<li><b>C 에러 수정 · 25분</b>에러 코드의 원인을 찾아 고친다</li>
<li><b>D 정리 · 10분</b>새 템플릿 ⑮를 추가하고 오늘 고친 실수를 한 줄 기록한다</li>
</Timeline>

<Grid cols="3" align="start">
<Tile kind="soft" color="py" tag="오늘의 재료" title="텍스트 값 정제">

`"1,200"` · `" 950"`처럼 문자열로 들어온 값을 숫자와 보고 문장으로 바꾼다

</Tile>
<Tile kind="soft" color="ai" tag="새 템플릿" title="⑮ 근거와 함께 묻기">

AI가 알려 준 메서드 · 형식이 실제로 있는지 공식 문서에서 확인한다

</Tile>
<Tile kind="soft" color="ok" tag="AI의 역할" title="조언 받기 단계">

코드는 내가 쓰고, AI는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 맡는다

</Tile>
</Grid>

<!--
진행은 ① 조언 받기 단계 공통 진행 그대로다. B · C의 코드는 미리 준비해 나눠 준다. 강사용 원인은 각 쪽 발표자 노트에만 있다.
시간이 모자라면 B · C에서 한 문제씩 줄이고, D의 템플릿 ⑮ 추가는 빼지 않는다.
-->

---

## #02. 오늘의 규칙과 `## 제약` 범위

<Callout kind="real" title="오늘의 규칙">

- 코드는 내가 쓰고, AI에게는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 묻는다
- 프롬프트는 다섯 섹션 `## 맥락` `## 상황` `## 질문` `## 제약` `## 출력 형식`
- `## 제약`에는 아래 표의 배운 범위를 적는다

</Callout>

<div class="kicker">문자열 단원 · <code>## 제약</code>에 쓰는 범위</div>

| 단원 | 범위 |
|:--|:--|
| 1 문자열의 이해 | 문자열 연산, 이스케이프 문자, 인덱싱 · 슬라이싱 |
| 2 문자열 포메팅 | 형식 문자, format(), f-string, 자릿수 지정 |
| 3 문자열 관련 함수 | len · str, count · find · rfind · isupper · islower · upper · lower · swapcase · capitalize · title · strip · lstrip · rstrip · replace · split · isnumeric |

<!--
시작 전에 ChatGPT 맞춤 지침(설정 → 개인 맞춤 설정 → 사용자 지정 지침)이 「ChatGPT 지침.md」로 들어 있는지 말로 확인한다. AI가 코드를 통째로 주면 지침이 빠진 것이므로 설정을 확인하고 새 대화에서 다시 시작하게 한다.
오늘 쓰는 모든 프롬프트의 ## 제약은 이 표에서 가져온다.
-->

---
layout: section
---

# A. 구현

문제를 직접 푼다. 막히면 「내 프롬프트 템플릿.md」에서 템플릿을 꺼내 조언을 받는다 · 40분

---

## #03. A-1 한 줄 분리

<div class="kicker">아래 한 줄에서 날짜 · 지점 · 금액 · 결제수단을 꺼낸다</div>

```python
"2024-01-05|강남점|125000|card"
```

<Grid cols="5" gap="12">
<Tile color="pastel-1" tag="날짜" value="2024-01-05" />
<Tile color="pastel-2" tag="지점" value="강남점" />
<Tile color="pastel-3" tag="금액 · 정수" value="125000" />
<Tile color="pastel-4" tag="결제수단" value="card" />
<Tile color="pastel-5" tag="월" value='"01"' />
</Grid>

<Callout kind="tip" title="조건 두 가지">

- 금액은 문자열이 아니라 **정수**로 꺼낸다
- 월은 날짜에서 `"01"`로 꺼낸다

</Callout>

<!--
split("|")로 네 조각을 나누고, 금액은 int()로 바꾼다. 월은 날짜 문자열의 인덱싱 · 슬라이싱으로 꺼낸다. 금액을 type()으로 찍어 int인지 확인하게 한다.
-->

---

## #04. A-2 숫자 정제

<Grid cols="3fr 2fr" align="center">
<div>

<div class="kicker">쉼표와 공백을 지우고 정수로 바꿔 합계를 구한다</div>

```python
["1,200", " 950", "1,050 "]
```

<Flow color="ai">
<li><b>쉼표 · 공백</b>섞인 문자열</li>
<li><b>지우기</b>쉼표와 공백 제거</li>
<li><b>정수</b>int로 변환</li>
<li><b>합계</b>세 값을 더한다</li>
</Flow>

</div>
<div>

<Stat value="3200" label="정답 · 합계" color="ok" />

</div>
</Grid>

<!--
원소마다 앞뒤 공백 위치가 다르다(" 950"은 앞, "1,050 "은 뒤). 쉼표는 replace, 공백은 strip 또는 replace로 지운다. 합계가 3200이 아니면 원소 하나씩 정제 결과를 찍어 보게 한다.
-->

---

## #05. A-3 주소 분리

<div class="kicker">앞뒤 공백을 지우고 시 · 구를 꺼낸다</div>

```python
"  서울특별시 강남구 테헤란로 123  "
```

<Grid cols="2" align="start">
<Tile kind="soft" color="py" tag="정답 · 시" value="서울특별시" />
<Tile kind="soft" color="ai" tag="정답 · 구" value="강남구" />
</Grid>

<Core color="ok">앞뒤 공백 정리 → 공백으로 나누기 → 앞의 두 조각</Core>

<!--
strip()으로 앞뒤 공백을 지운 뒤 split()으로 나누고 0번 · 1번을 꺼낸다. 앞뒤 공백을 지우지 않고 split(" ")로 나누면 빈 문자열 조각이 생겨 인덱스가 밀리는 학생이 있다.
-->

---

## #06. A-4 마스킹

<div class="kicker">전화번호 가운데 네 자리를 별표로 바꾼다</div>

<Grid cols="2" align="center">
<div>

<Output label="원래 값">

```text
010-1234-5678
```

</Output>

</div>
<div>

<Output label="바꾼 값">

```text
010-****-5678
```

</Output>

</div>
</Grid>

<p>쓸 수 있는 방법 <Chip>인덱싱 · 슬라이싱</Chip> <Chip color="ai">split</Chip> <Chip color="ok">replace</Chip> <Chip kind="outline" color="muted">문자열 연산</Chip></p>

<!--
슬라이싱으로 앞 "010-"과 뒤 "-5678"을 잘라 "****"과 이어 붙이거나, split("-")로 세 조각을 나눈 뒤 가운데만 바꿔 다시 이어 붙인다. replace("1234", "****")는 이 값에서는 맞지만, 다른 번호에서는 쓸 수 없다는 점을 이야기해 볼 수 있다.
-->

---

## #07. A-5 보고 문장

<Grid cols="3" gap="16">
<Tile tag="지점" value="강남점" />
<Tile tag="매출" value="125000" color="ai" />
<Tile tag="전체" value="333333" color="ok" />
</Grid>

<div class="kicker">매출은 천 단위 쉼표, 비율(매출 ÷ 전체)은 소수 첫째 자리로 출력한다</div>

<Output label="정답">

```text
강남점 | 매출 125,000원 | 비율 37.5%
```

</Output>

<Callout kind="ai" title="막히면 새 템플릿 ⑮ 근거와 함께 묻기">
천 단위 쉼표를 넣는 형식 지정 방법과 그 방법이 공식 문서 어디에 나오는지 함께 받는다. 다음 쪽에서 만든다
</Callout>

<!--
f-string 자릿수 지정 재료. 천 단위 쉼표는 형식 지정 기호 ","로, 비율은 ".1f"로 맞춘다. 비율은 125000 / 333333 × 100 = 37.5%.
이 문제가 템플릿 ⑮로 이어진다. 형식 지정 기호는 AI가 그럴듯하게 틀리기 쉬운 곳이라 공식 문서 확인 연습에 알맞다.
-->

---
class: dense
---

## #08. 새 템플릿 ⑮ 근거와 함께 묻기

<Callout icon="💡" title="AI가 알려 준 메서드 · 형식이 실제로 있는지 공식 문서에서 확인하고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2">

````md
## 맥락
파이썬 문자열 단원을 배우는 중이야.

## 상황
숫자를 천 단위 쉼표가 들어간 문자열로 출력하고 싶어. 예: 125000 → 125,000

## 질문
f-string에서 이걸 하는 형식 지정 방법을 알려주고, 파이썬 공식 문서의 어느 부분에 나오는지 알려줘.

## 제약
- 코드 대신 형식 지정 기호의 의미를 말로 설명해
- 공식 문서(docs.python.org/ko)의 문서 이름과 절 이름을 적어. 확실하지 않으면 "확인 필요"라고 표시해

## 출력 형식
| 기호 | 의미 | 공식 문서 위치 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 사용 방법</h3>

- 알려 준 절을 공식 문서에서 직접 열어 본다
- 위치가 틀렸으면 기록한다

</div>

<Callout kind="warn" title="주의">
AI가 적은 문서 이름 · 절 이름도 추측. 직접 열어 봐야 근거가 된다
</Callout>

</div>
</Grid>

<!--
환각을 직접 잡아 보는 첫 활동이다. 지침 때문에 코드는 오지 않고 기호의 의미와 문서 위치가 표로 온다.
학생이 확인한 결과(위치가 맞음 / 틀림 / 확인 필요)를 「문자열 정제 메모.md」에 적게 한다. 위치가 틀린 답이 나오면 실패가 아니라 AI의 환각을 잡아낸 것으로 다룬다.
-->

---
layout: infographic
---

### #08-1. 덤 활동 — 없는 메서드 물어보기

<Flow color="pastel">
<li><carbon:help /><b>일부러 묻기</b>없는 메서드<br><code>str.reverse()</code>를 물어본다</li>
<li><carbon:chat /><b>답 기록</b>AI가 뭐라고 답했는지 그대로 적는다</li>
<li><carbon:document /><b>공식 문서 확인</b>문자열 메서드 목록에 있는지 직접 찾는다</li>
<li><carbon:edit /><b>메모</b>「문자열 정제 메모.md」에 결과를 남긴다</li>
</Flow>

<Callout kind="ai" title="기록할 것">
AI가 "없다"고 답했는지, 있는 것처럼 사용법을 지어냈는지
</Callout>

<!--
덤 활동. ⑮ 프롬프트의 상황 · 질문만 바꿔 str.reverse()를 묻는다. 문자열에는 reverse() 메서드가 없다(리스트에는 있다). AI가 있는 것처럼 설명하면 환각 사례로, 없다고 하면 그 근거로 제시한 문서 위치를 다시 확인하게 한다.
-->

---
layout: section
---

# B. 결과가 이상할 때

에러는 안 나는데 값이 틀렸다. 나눠 준 코드의 틀린 값을 찾아 고친다 · 25분

---

## #09. B 진행 방법

<Steps color="ai">
<li>나눠 준 코드를 <b>내 노트북에 그대로</b> 쓰고 실행해 증상을 확인한다</li>
<li>짐작이 있으면 <b>⑧ 내 추측 확인 방법 묻기</b>, 없으면 <b>⑦ 확인할 곳 묻기</b>를 꺼낸다</li>
<li>AI가 알려 준 곳을 <code>print()</code> · <code>type()</code>으로 <b>내가 찍어 보고</b> 원인을 찾는다</li>
<li>코드를 고쳐 기대한 값이 나오는지 직접 실행해 확인한다</li>
</Steps>

<Grid cols="3" gap="16">
<Tile kind="surface" color="pastel-1" tag="B-1" title="문자열 덧셈" />
<Tile kind="surface" color="pastel-2" tag="B-2" title="replace 뒤의 공백" />
<Tile kind="surface" color="pastel-3" tag="B-3" title="count 결과" />
</Grid>

<!--
LAB-02의 ⑦ · ⑧을 그대로 쓴다. ## 제약에는 #02 표의 범위를 적는다. AI가 원인을 바로 말해 주면 지침이 살아 있는지 확인한다.
-->

---

### #09-1. B-1 · B-2 코드와 증상

<Grid cols="2" align="start">
<div>

<div class="kicker">B-1</div>

```python
print("100" + "200")
```

<Output label="실행 결과">

```text
100200
```

</Output>

<Callout kind="warn" title="증상">
<code>300</code>이 아니라 <code>100200</code>
</Callout>

</div>
<div>

<div class="kicker">B-2</div>

```python
name = "홍 길 동"
name.replace(" ", "")
print(name)
```

<Output label="실행 결과">

```text
홍 길 동
```

</Output>

<Callout kind="warn" title="증상">
공백이 그대로 남아 있다
</Callout>

</div>
</Grid>

<!--
강사용 원인
B-1: 문자열 덧셈은 이어 붙이기다. 숫자로 더하려면 int()로 바꾼 뒤 더한다.
B-2: 문자열은 바뀌지 않는다. replace는 새 문자열을 돌려줄 뿐이므로 결과를 다시 대입한다(name = name.replace(" ", "")).
-->

---

### #09-2. B-3 코드와 증상

<Grid cols="2" align="center">
<div>

```python
print("Seoul,seoul,SEOUL".count("seoul"))
```

<Output label="실행 결과">

```text
1
```

</Output>

</div>
<div>

<Stat value="3" label="기대한 값" color="ok">세 번 나온 서울을 모두 세고 싶다</Stat>

</div>
</Grid>

<Callout kind="warn" title="증상">
<code>3</code>이 아니라 <code>1</code>
</Callout>

<!--
강사용 원인: count는 대소문자를 구분한다. lower()로 모두 소문자로 바꾼 뒤 세면 3이 나온다.
⑧에 "대소문자 때문인 것 같다"는 추측을 적어 보내면 확인 방법으로 upper · lower 결과를 찍어 보라는 답이 오는지 본다.
-->

---
layout: section
---

# C. 에러 수정

빨간 글씨가 떴다. 에러 코드의 원인을 찾아 고친다 · 25분

---

## #10. C 진행 방법

<Flow color="ok">
<li><carbon:play /><b>실행</b>나눠 준 코드를 내 노트북에서 실행한다</li>
<li><carbon:warning-alt /><b>⑩ 에러 원문 보내기</b>코드와 에러 메시지 전체를 그대로 붙인다</li>
<li><carbon:tools /><b>직접 고치기</b>원인과 고치는 방향만 받고 수정은 내가 한다</li>
<li><carbon:renew /><b>⑪ 같은 실수 막기</b>같은 에러가 나는 다른 경우를 받아 하나를 직접 만든다</li>
</Flow>

| | 코드 | 에러 |
|:--:|:--|:--|
| C-1 | `"매출: " + 125000` | `TypeError` |
| C-2 | `int("1,200")` | `ValueError` |
| C-3 | `"a b".split().strip()` | `AttributeError` |

<!--
LAB-02의 ⑩ · ⑪을 그대로 쓴다. 에러 메시지는 마지막 줄만이 아니라 전체를 붙이게 한다. 같은 종류의 에러를 반복해서 묻고 있다면 ⑪로 넘어가게 한다.
-->

---

### #10-1. C-1 · C-2 코드와 에러

<Grid cols="2" align="start">
<div>

<div class="kicker">C-1</div>

```python
print("매출: " + 125000)
```

<Output label="에러">

```text
TypeError: can only concatenate str (not "int") to str
```

</Output>

</div>
<div>

<div class="kicker">C-2</div>

```python
int("1,200")
```

<Output label="에러">

```text
ValueError: invalid literal for int() with base 10: '1,200'
```

</Output>

</div>
</Grid>

<Callout kind="tip" title="A와 이어진 곳">
C-1은 A-5 보고 문장, C-2는 A-2 숫자 정제에서 만날 수 있는 에러다
</Callout>

<!--
강사용 원인
C-1: 문자열과 정수는 + 로 이어 붙일 수 없다. str()로 바꾸거나 f-string을 쓴다.
C-2: 쉼표가 든 문자열은 int()로 바꿀 수 없다. 쉼표를 지운 뒤 변환한다(A-2와 같은 정제).
-->

---

### #10-2. C-3 코드와 에러

<Grid cols="2" align="center">
<div>

```python
"a b".split().strip()
```

<Output label="에러">

```text
AttributeError: 'list' object has no attribute 'strip'
```

</Output>

</div>
<div>

<Callout kind="eli5" title="에러 메시지 읽기">

- `'list' object` — strip을 부른 대상
- `has no attribute 'strip'` — 그 대상에는 strip이 없다

</Callout>

</div>
</Grid>

<Core color="warn">메서드를 이어 쓸 때는 앞 메서드가 돌려준 값의 자료형을 먼저 확인한다</Core>

<!--
강사용 원인: split의 결과는 리스트다. 리스트에는 strip이 없다. 순서를 바꿔 strip을 먼저 하거나, 나눈 조각마다 strip을 쓴다.
type("a b".split())을 찍어 보게 하면 <class 'list'>로 바로 확인된다.
-->

---
layout: section
---

# D. 정리

새 템플릿을 모으고 오늘 고친 실수를 기록한다 · 10분

---
layout: cards
cols: 3
---

## #11. 오늘의 결과물

<div class="py">

#### <carbon:code /> A-1 ~ A-5 풀이

- 한 줄 분리 · 숫자 정제 · 주소 분리 · 마스킹 · 보고 문장
- 정답과 직접 실행한 값을 대조한다

</div>
<div class="ai">

#### <carbon:document /> 문자열 정제 메모.md

- 오늘 쓴 메서드
- 그 메서드를 공식 문서에서 확인했는지 여부

</div>
<div class="ok">

#### <carbon:bookmark /> 템플릿 ⑮

- 「내 프롬프트 템플릿.md」에 추가
- 오늘 고친 실수 한 줄 기록

</div>

<Callout kind="real" title="데이터 분석으로 이어지는 곳">
실제 데이터의 숫자는 <code>"1,200"</code>, <code>" 950"</code>처럼 문자열로 들어온다. LAB-07 · 08에서 같은 정제를 파일 전체에 적용한다
</Callout>

<!--
결과물은 걷지 않고, 「문자열 정제 메모.md」에 공식 문서 확인 여부 칸이 채워졌는지만 둘러보며 확인한다. 덤 활동(str.reverse())을 한 학생은 그 결과도 메모에 있다.
템플릿은 ①~⑫(LAB-02), ⑬(LAB-03), ⑭(LAB-04)에 이어 ⑮까지 쌓인다.
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-05] 문자열 4 · ITWILL · {teacher} 강사</p>

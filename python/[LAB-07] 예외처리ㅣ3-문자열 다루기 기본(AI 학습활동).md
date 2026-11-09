---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 예외처리 — 문자열 다루기 기본
layout: cover
---

# 문자열 다루기 기본 — 예외처리 종합문제

AI에게 코드를 받아 검증하며 푸는 코딩 테스트 — 프로그래머스 「문자열 다루기 기본」

<p class="sub">[LAB-07] 예외처리 3 · ITWILL · {teacher} 강사</p>

<!--
「예외처리의 이해」 교안과 실습 코드를 마치고, LAB-07-2 「AI에게 답을 받는 법」에서 지침을 「ChatGPT 지침(답 받기).md」로 바꾼 학생이 하는 첫 답 받기 실습.
LAB-03 ~ 06과 같은 틀(문제 하나, 세 단계)이다. ② 답 받기 단계라서 2단계가 바뀐다: 직접 시도한 뒤 ⑰ 코드 받기로 코드를 받고, 받은 코드를 4단 확인(실행 · 범위 · 설명 · 변형)한다. 3단계는 틀렸을 때 ⑱ 내 코드 고쳐 받기. 마무리는 ⑫ 거꾸로 질문.
단계마다 프롬프트 하나만 쓴다: 1단계 ② + ⑤, 2단계 ⑰, 3단계 ⑱.
-->

---

## #01. 오늘의 흐름

<Timeline>
<li><b>문제 읽기</b>코딩 테스트 문제와 입출력 예를 본다</li>
<li><b>세 단계로 풀기</b>설계는 AI와 함께, 코드는 직접 시도한 뒤 받고, 틀리면 고쳐 받는다</li>
<li class="now"><b>마무리</b>⑫ 거꾸로 질문으로 받은 코드를 내 코드로 만들었는지 점검한다</li>
</Timeline>

<Grid cols="2" align="start">

<Callout kind="real" title="오늘의 규칙">

- **먼저 직접 시도**하고, 막힌 코드를 `## 내 시도`에 붙여 답을 받는다
- 받은 코드는 **4단 확인**(실행 · 범위 · 설명 · 변형)을 통과해야 내 코드다
- 첫 질문은 섹션을 갖춘 md로 자세히, 같은 대화의 후속 질문은 평서문으로

</Callout>

<Tile kind="soft" color="ai" tag="오늘 새 템플릿" title="⑰ 코드 받기 · ⑱ 내 코드 고쳐 받기">
LAB-06의 ⑯ 뒤로 이어 매긴다. 프롬프트는 <code>## 내 시도</code>를 더한 여섯 섹션
</Tile>

</Grid>

<!--
시작 전에 ChatGPT 맞춤 지침이 「ChatGPT 지침(답 받기).md」로 바뀌었는지 확인한다. ## 내 시도 없이 보냈는데 코드가 바로 오면 지침 2-1이 적용되지 않은 것이므로, 설정을 확인하고 새 대화로 간다.
오늘은 문제 하나를 끝까지 푸는 것이 목표다. 코드를 받는 것으로 끝내지 않고, 받은 코드가 4단 확인을 통과했는지가 오늘의 결과물이다.
-->

---

## #02. 문법 범위

<div class="kicker">받은 코드도 지금까지 배운 문법이어야 한다. 모든 프롬프트의 <code>## 제약</code>에 이 범위를 적는다</div>

| 단원 | 쓸 수 있는 것 |
|:--|:--|
| LAB-02 · 03 | 변수 · 연산자 · 함수 정의(파라미터 · return) · if · elif · else · while · for · range · 중첩 · break · continue |
| LAB-04 리스트 | 인덱스 · 슬라이싱 · 2차원 리스트 · 구조분해 · in · len · sorted · sort · append 등 |
| LAB-05 · 06 | 문자열 인덱싱 · 슬라이싱 · upper · lower · strip · replace · split · 딕셔너리 · get · items 등 |
| LAB-07 예외처리 | if로 대비하기 · try · except · 예외 종류별 except · `as` 로 메시지 받기 · finally · Exception |

<Callout kind="danger" title="아직 안 배운 것">
받은 코드에 있으면 범위 안으로 다시 요청한다: 리스트 컴프리헨션 · lambda · 모듈 import · <code>isdigit</code> · <code>isalpha</code> 같은 문자열 판별 함수
</Callout>

<Core color="ok">받은 코드에 안 배운 문법이 있으면 4단 확인의 ② 범위에서 걸린다.</Core>

<!--
LAB-07 실습코드에 나오는 것: if로 0 · 범위 초과 대비하기, try · except, except ValueError · ZeroDivisionError처럼 종류별 처리, except ... as 변수, finally, except Exception as e.
isdigit · isalpha는 LAB-02 ~ 07 실습코드 어디에도 나오지 않는다(직접 확인). 범위를 적지 않으면 ChatGPT는 이 문제를 거의 항상 s.isdigit() 한 줄로 푼다. 값은 맞지만 ② 범위에서 걸린다. 오늘은 int()로 바꿔 보고 실패하면 except로 받는 방법, 즉 오늘 배운 예외처리로 푼다.
-->

---
layout: section
---

# 문제

LAB-02 ~ LAB-07에서 배운 것으로 풀리는 문제 하나

---
class: dense
---

## #03. 문제 — 문자열 다루기 기본

<Grid cols="1fr 1fr" align="start">
<div>

문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

<div class="kicker">제한 사항</div>

- `s`는 길이 1 이상, 길이 8 이하인 문자열입니다.
- `s`는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.

| s | return |
|:--|:--|
| "a234" | false |
| "1234" | true |

<p class="small muted">출처: <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12918" target="_blank" rel="noopener">프로그래머스 코딩테스트 연습 「문자열 다루기 기본」</a></p>

</div>
<div>

<div class="kicker">기본 코드 템플릿</div>

```python
def solution(s):
    answer = True
    return answer

print(solution("a234"))  # False
print(solution("1234"))  # True
```

<Callout kind="tip" title="예외처리 연결">
<code>int("a234")</code>는 <b>ValueError</b>가 난다. 에러가 나는지가 곧 「숫자로만 구성됐는지」의 답이 된다
</Callout>

</div>
</Grid>

<!--
문제 원문은 프로그래머스 그대로다(2022년 7월 22일 제한 사항이 추가된 판). 입출력 예의 false · true는 원문 표기 그대로이고, 파이썬에서는 False · True를 돌려준다.
쓰는 문법: 함수 정의와 return(LAB-02), if · or(LAB-03), len(LAB-04 · 05), int()와 try · except ValueError(LAB-07).
조건이 두 개다: 길이가 4 또는 6, 그리고 숫자로만 구성. 하나만 검사한 코드도 입출력 예 두 줄은 통과한다. 그래서 4단 확인의 ① 실행에서 입출력 예 말고 더 넣어 볼 값이 필요하다(#07).
제한 사항 덕분에 int()로 판정해도 맞다. s에는 영문자와 숫자만 들어오기 때문이다. 제한이 없다면 int("-123") · int(" 123") · int("+123") · int("1_00")도 에러 없이 바뀌어 True가 된다(직접 실행해 확인). ⑫에서 이 점을 물어보면 좋다.
기본 코드 템플릿의 def 부분은 프로그래머스 Python3 편집기에 처음 들어 있는 코드와 같고, print 두 줄은 노트북에서 입출력 예를 확인하려고 덧붙인 것이다. 프로그래머스에 제출할 때는 solution 함수만 붙여 넣는다.
-->

---
layout: section
---

# 풀이 단계

설계 → 코드 받기 → 고쳐 받기, 세 단계로 푼다

---

## #04. 세 단계 풀이

<Steps color="pastel">
<li><b>문제 확인 · 함수 설계</b> — 내 정리를 점검받고, 처리 순서를 단계표로 받는다 <Chip color="ai">프롬프트 ② + ⑤</Chip></li>
<li><b>직접 시도 · 코드 받기 · 4단 확인</b> — 단계표대로 써 보고, 막힌 코드를 보내 이어서 완성한 코드를 받는다 <Chip color="ai">프롬프트 ⑰</Chip></li>
<li><b>수정 코드 받기</b> — 틀린 결과와 내가 짐작한 원인을 보내 바꾼 줄만 받는다 <Chip color="ai">프롬프트 ⑱</Chip></li>
</Steps>

<Core color="ai">코드를 쓰는 손은 AI로 넘어가도, 맞는지 판단하는 일은 내 몫이다.</Core>

<!--
LAB-03 ~ 06과 같은 세 단계다. 2단계만 "AI 없이 직접 쓴다"에서 "직접 시도한 뒤 받는다"로 바뀌었다.
1단계를 건너뛰면 받은 코드가 맞는지 판단할 기준이 없다. 조건이 두 개(길이, 숫자만)라는 것을 1단계에서 잡아 두어야 2단계 4단 확인에서 틀린 코드를 알아본다.
-->

---
class: dense
---

## #05. 1단계 — 문제 확인 · 함수 설계

<Callout icon="💡" title="문제를 제대로 이해했는지 확인하고, 어떤 순서로 코드를 쓸지 정하고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ② + ⑤번 패턴">

````md
## 맥락
파이썬 예외처리 단원을 배우는 중이야. 코딩 테스트 문제를 풀기 전에 문제를 내 말로 정리했어.

## 상황
문제: {문제 원문 붙여 넣기}

내 정리:
- 검사할 조건: {내가 이해한 내용}
- True가 되는 경우: {내가 이해한 내용}
- False가 되는 경우: {내가 이해한 내용}

## 질문
1. 내 정리에서 문제와 다르게 이해한 부분과 빠진 부분을 짚어 줘
2. 그다음 처음부터 끝까지 해야 할 일을 단계 순서로 나눠 줘

## 제약
- 아직 코드는 주지 말고 말로만
- 배운 범위(조건문 · 반복문 · 리스트 · 문자열 · 딕셔너리 · 함수 · try/except) 안에서. isdigit 같은 문자열 판별 함수는 쓰지 않는 방법으로

## 출력 형식
1은 | 내 정리 | 판정(맞음 / 보완) | 이유 | 표로
2는 | 단계 | 할 일 | 끝나면 확인할 것 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 문제를 다시 보지 않고 **세 줄**로 정리해 보낸다
- **보완** 판정을 받은 줄은 내 말로 고친다
- 받은 단계표를 노트북 **마크다운 셀**에 옮긴다

</div>

<Callout kind="warn" title="주의">
아직 <code>## 내 시도</code>가 없으므로 지침 2-1에 따라 코드 대신 처리 순서가 온다. 그게 정상이다
</Callout>

</div>
</Grid>

<!--
LAB-02의 ② 내 설명 점검받기와 ⑤ 단계로 쪼개기를 한 프롬프트로 묶었다(LAB-03 ~ 06과 같다). 아직 코드를 받지 않는 단계라 다섯 섹션 그대로 쓴다.
학생이 자주 빠뜨리는 정리: 길이 조건이 "4 이상 6 이하"가 아니라 "4 또는 6"이다(5는 False), 두 조건을 모두 만족해야 True다, 영문자가 하나라도 섞이면 False다.
기대하는 단계표: ① s의 길이가 4 또는 6인지 검사 ② 아니면 False를 돌려줌 ③ int(s)로 바꿔 봄 ④ ValueError가 나면 False를 돌려줌 ⑤ 에러 없이 바뀌면 True를 돌려줌.
-->

---
class: dense
---

## #06. 2단계 — 직접 시도 · 코드 받기

<Callout icon="💡" title="단계표대로 직접 써 봤는데 끝까지 못 풀어서, 내 시도를 이어서 완성한 코드를 받고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑰번 패턴 (오늘 새 패턴)">

````md
## 맥락
파이썬 예외처리 단원을 배우는 중이야. 배운 범위: 조건문 · 반복문 · 리스트 · 문자열 · 딕셔너리 · 함수 · try/except.

## 상황
문제: {문제 원문 붙여 넣기}
정답: solution("a234")는 False, solution("1234")는 True

## 내 시도
{내가 쓴 코드와 막힌 지점}

## 질문
내 시도를 이어서 완성한 코드를 줘.

## 제약
- 배운 범위의 문법만 써. 리스트 컴프리헨션 · lambda는 쓰지 마
- 변수 이름은 내 코드(s)를 그대로 써

## 출력 형식
1. 코드
2. 줄마다 무슨 일을 하는지 표로 | 줄 | 하는 일 |
3. 정답과 맞는지 내가 확인할 방법 2줄
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 단계표를 **주석**으로 옮겨 먼저 직접 쓴다
- `## 내 시도`에 막힌 코드와 지점을 그대로 붙인다
- 받은 코드는 바로 다음 쪽의 **4단 확인**으로 간다

</div>

<Callout kind="warn" title="주의">
직접 다 풀었으면 받지 않는다. 내 코드로 바로 4단 확인을 한다
</Callout>

</div>
</Grid>

<!--
LAB-07 새 템플릿 ⑰. LAB-07-2 #08-1의 예시와 같은 틀이고, ## 상황만 오늘 문제로 바뀌었다. 지침 3-1에 따라 AI는 학생 시도에서 맞은 부분과 막힌 지점을 먼저 짚고, 그 시도를 이어서 완성한다. 처음부터 다른 방식으로 새로 쓴 코드가 오면 지침이 바뀌었는지 확인한다.
## 상황에 정답을 적는 이유: 받은 코드를 ① 실행 단계에서 바로 대조하기 위해서다.
학생 시도에서 자주 막히는 곳: int(s)를 써 놓고 에러를 어떻게 False로 바꿀지(try · except의 위치), 길이 조건을 어떻게 쓸지.

강사용 정답 코드(학생 자료에는 없음):
def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except ValueError:
            return False
    return False

print(solution("a234"), solution("1234"))  # False True
try에서 먼저 int(s)를 검사하고, 통과한 뒤 return len(s) == 4 or len(s) == 6을 돌려주는 풀이도 맞다(같은 결과, 직접 실행해 확인).
-->

---
layout: infographic
---

## #07. 2단계 — 받은 코드 4단 확인

<Flow color="pastel">
<li><carbon:play /><b>① 실행</b>입출력 예 두 줄과 아래 값을 넣어 대조<span class="small muted">"12345" → False · "123456" → True · "1e34" → False</span></li>
<li><carbon:rule /><b>② 범위</b>#02 표에 없는 문법이 있는지<span class="small muted">isdigit · 컴프리헨션이 보이면 다시 요청</span></li>
<li><carbon:chat /><b>③ 설명</b>줄별 설명 표를 덮고 줄마다 말로 설명<span class="small muted">try 안에 무엇이 왜 들어갔는지</span></li>
<li><carbon:edit /><b>④ 변형</b>AI 없이 직접 풀기<span class="small muted">길이 조건을 「4 이상 6 이하」로 바꾸면?</span></li>
</Flow>

<Grid cols="2" gap="12">
<Tile kind="soft" color="ok" tag="① 실행 실패 시" title="3단계 ⑱ 고쳐 받기">입출력 예만 통과하고 더 넣은 값에서 틀리는 코드가 자주 온다</Tile>
<Tile kind="soft" color="ai" tag="④ 변형 정답" title="&quot;12345&quot; → True · &quot;1234567&quot; → False">받은 코드의 어느 줄을 바꾸면 되는지 설명할 수 있어야 풀린다</Tile>
</Grid>

<!--
2단계의 이어지는 활동이다. 프롬프트를 새로 쓰지 않고 받은 코드를 확인만 한다.
① 실행 확인 값(정답 코드로 직접 실행): "12345" → False, "123456" → True, "12" → False, "0000" → True, "1e34" → False.
ChatGPT가 자주 주는 코드와 4단 확인에서 걸리는 곳(모두 직접 실행해 확인):
s.isdigit() 한 줄: 값은 모두 맞다. ② 범위에서 걸린다(isdigit은 실습코드에 없다).
int(s) 대신 float(s)로 바꿔 봄: 입출력 예 두 줄은 통과하지만 "1e34" → True(정답 False). 1e34를 지수 표기 숫자로 읽기 때문이다. ① 실행에서 걸린다.
길이 검사를 빼먹음: "12345" → True, "12" → True. ① 실행에서 걸린다.
④ 변형 정답(직접 실행): 길이 조건을 4 <= len(s) <= 6으로 바꾸면 "12345" → True, "1234567" → False, "a234" → False.
-->

---
class: dense
---

## #08. 3단계 — 수정 코드 받기

<Callout icon="💡" title="받은 코드나 내 코드가 확인 값에서 틀리거나 에러가 났고, 원인을 짐작해 봤는데 어떻게 고칠지 막힌 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑱번 패턴 (오늘 새 패턴)">

````md
## 맥락
파이썬 예외처리 단원을 배우는 중이야.

## 상황
문자열 다루기 기본 solution 함수가 확인 값에서 틀렸어.
```python
{내 코드 또는 받은 코드}
```
넣은 값과 결과: {예: solution("1e34")가 True, 정답은 False · 에러면 에러 원문 그대로}

## 내 시도
내가 생각한 원인: {내 생각}

## 질문
내 코드를 고친 코드를 줘.

## 제약
- 내 코드에서 바꾼 줄만 바꿔. 나머지는 그대로 둬
- 배운 범위의 문법만 써

## 출력 형식
1. 고친 코드 (바꾼 줄 끝에 # 변경 표시)
2. | 바꾼 줄 | 바꾼 이유 | 표로
3. 내가 생각한 원인이 맞았는지 한 줄
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 넣은 값과 결과를 **그대로** 붙인다
- 내가 생각한 원인을 **한 줄로 먼저** 적는다
- 고친 코드도 받은 코드다. **① 실행부터** 다시 한다

</div>

<Callout kind="danger" title="에러 발생 시">
트레이스백은 줄이지 않고 전체를 붙인다. 맨 아래 줄부터 읽는다
</Callout>

</div>
</Grid>

<!--
LAB-07 새 템플릿 ⑱. 지침 2-6에 따라 AI는 바꾼 줄만 바꾸고 # 변경 주석과 이유 표를 붙인다. 코드 전체가 다른 모양으로 바뀌어 오면 제약의 "바꾼 줄만"을 다시 요청한다. 원인을 비워 두지 않는 것이 핵심이다. 출력 형식 3번에서 내 짐작이 맞았는지 확인받는다.
강사용 증상과 원인(모두 Python 3.13으로 직접 실행해 확인):
"1e34"가 True: int 대신 float로 바꿔 봄. float는 1e34를 지수 표기 숫자로 읽는다.
"12345" · "12"가 True: if len(s) == 4 or 6:처럼 씀. or 뒤의 6은 그 자체로 참이라 길이 검사가 항상 통과한다. 길이 검사를 아예 빼먹어도 같은 증상.
ValueError: invalid literal for int() with base 10: 'a234' — try · except 없이 int(s)만 씀. 입출력 예 첫 줄에서 바로 멈춘다.
모든 값이 False: try 안에서 int(S)처럼 변수 이름 오타를 내고 except:(종류 없이)로 받음. NameError: name 'S' is not defined가 삼켜져 "1234"도 False가 된다. except ValueError로 종류를 적으면 NameError가 그대로 드러난다.
"1234"가 None: 길이가 맞고 int(s)가 성공한 뒤 return True를 빠뜨림. 함수 끝까지 return을 만나지 못해 None이 돌아간다(길이가 안 맞는 "12345"도 None).
-->

---
class: dense
---

## #09. 마무리 — ⑫ 거꾸로 질문

<Callout icon="💡" title="문제는 풀었는데, 받은 코드를 정말 내 코드로 만들었는지 점검하고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑫번 패턴">

````md
## 맥락
파이썬 예외처리 단원을 배우는 중이야. 문자열 다루기 기본 문제를 4단 확인까지 마쳤어.

## 상황
최종 코드:
```python
{최종 코드}
```

## 질문
이 코드를 내가 이해했는지 점검하는 문제를 한 번에 하나씩 내 줘.
내가 답하면 맞았는지 알려 주고 다음 문제로 넘어가.
다섯 문제가 끝나면 내가 약한 부분을 정리해 줘.

## 제약
- 문제는 이 코드의 실행 결과를 예측하거나 줄의 역할을 설명하는 것으로. 코드를 작성하라는 문제는 내지 마
- 배운 범위(조건문 · 문자열 · 함수 · try/except) 안에서

## 출력 형식
문제는 아래 예시와 같은 모양으로, 한 번에 하나만.
- 예시: solution("12a4")를 부르면 어느 줄에서 함수가 끝날까?
다섯 문제가 끝나면 | 약한 부분 | 어느 단원 | 다시 볼 것 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 답은 **실행해 보기 전에** 먼저 적는다
- 답한 뒤 직접 실행해 맞는지 확인한다
- 약한 부분 표에서 다시 볼 교안 쪽을 찾아 둔다

</div>

<Callout kind="warn" title="주의">
⑫는 코드를 받지 않는다. 문제가 아니라 코드가 오면 <code>## 제약</code>을 가리키며 다시 요청한다
</Callout>

</div>
</Grid>

<!--
LAB-02의 ⑫를 최종 코드에 맞춰 쓴다. 4단 확인의 ③ 설명을 한 번 더 다지는 역할이다.
좋은 문제 예: solution("12a4")에서 except로 넘어가는 줄은? / solution("12345")에서 try가 실행되는가?(아니다. 길이 검사에서 먼저 False) / 제한 사항이 없다면 solution("-123")은?(True. int("-123")이 성공하므로 — 직접 실행해 확인).
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-07] 예외처리 3 · ITWILL · {teacher} 강사</p>

---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 문자열 — 문자열 종합문제
layout: cover
---

# 문자열 종합문제

AI에게 물으며 푸는 코딩 테스트 — 프로그래머스 「이상한 문자 만들기」

<p class="sub">[LAB-05] 문자열 4 · ITWILL · {teacher} 강사</p>

<!--
문자열 단원(문자열의 이해 · 문자열 포메팅 · 문자열 관련 함수)을 마친 뒤 하는 실습. ① 조언 받기 단계(LAB-02 ~ 06)라서 코드는 학생이 쓰고, ChatGPT는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 맡는다(「ChatGPT 지침.md」 그대로).
LAB-03 · 04와 같은 틀이다. LAB-02 ~ 05에서 배운 것을 모두 써야 풀리는 코딩 테스트 문제(프로그래머스 「이상한 문자 만들기」) 하나를 세 단계로 푼다. 단계마다 프롬프트 하나 또는 코드 작성 하나만 한다: 1단계 프롬프트(② + ⑤), 2단계 코드 작성, 3단계 프롬프트(⑬). 마무리는 오늘 새 템플릿 ⑮ 근거와 함께 묻기.
-->

---

## #01. 오늘의 흐름

<Timeline>
<li><b>문제 읽기</b>코딩 테스트 문제와 입출력 예를 본다</li>
<li><b>세 단계로 풀기</b>설계는 AI와 함께, 코드는 내가, 틀리면 다시 AI와 함께</li>
<li class="now"><b>마무리</b>⑮ 근거와 함께 묻기로 AI 설명의 근거를 공식 문서와 실행으로 확인한다</li>
</Timeline>

<Grid cols="2" align="start">

<Callout kind="real" title="오늘의 규칙">

- 코드는 내가 쓰고, AI에게는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 묻는다
- 첫 질문은 다섯 섹션 `## 맥락` `## 상황` `## 질문` `## 제약` `## 출력 형식`으로 자세히, 같은 대화의 후속 질문은 평서문으로

</Callout>

<Tile kind="soft" color="ai" tag="오늘 새로 더하는 템플릿" title="⑮ 근거와 함께 묻기">
LAB-04의 ⑭ 뒤로 이어 매긴다. AI 설명에 공식 문서 위치를 붙여 받고, 문서와 실행으로 직접 확인한다
</Tile>

</Grid>

<!--
시작 전에 ChatGPT 맞춤 지침이 들어 있는지, 템플릿마다 새 대화를 여는지 말로 확인한다.
오늘은 문제 하나를 끝까지 푸는 것이 목표다. 단계를 건너뛰고 바로 코드를 쓰는 학생이 있으면, 막혔을 때 어느 단계로 돌아가 템플릿을 꺼낼지 묻는다.
-->

---

## #02. 쓸 수 있는 문법 — 배운 것까지만

<div class="kicker">코딩 테스트 문제는 지금까지 배운 문법으로 푼다. 모든 프롬프트의 <code>## 제약</code>에 이 범위를 적는다</div>

| 단원 | 쓸 수 있는 것 |
|:--|:--|
| LAB-02 · 03 | 변수 · 연산자(`%` 포함) · `+=` · 함수 정의(파라미터 · return) · if · elif · else · while · for · range · break · continue |
| LAB-04 리스트 | 인덱스 · 슬라이싱 · in · len · append · join · split · sorted · sort |
| LAB-05 문자열 | 문자열 연산 · 인덱싱 · 슬라이싱 · format · f-string · count · find · upper · lower · swapcase · capitalize · title · strip · replace · split · isupper · islower · isnumeric |

<Callout kind="danger" title="아직 안 배운 것 — 쓰지 않는다">
딕셔너리 · 리스트 컴프리헨션(<code>[x for x in ...]</code>) · lambda · enumerate · ord · chr
</Callout>

<Core color="ok">AI가 안 배운 방법을 권하면 따르지 않고, 배운 범위 안의 방법으로 다시 묻는다.</Core>

<!--
범위를 적지 않으면 AI가 enumerate나 리스트 컴프리헨션 한 줄로 푸는 방법을 권한다. 오늘은 for와 인덱스 변수, += 로 결과 문자열을 한 글자씩 쌓는다.
문자열 단원 실습코드에 나오는 메서드만 범위에 넣었다(직접 확인). isdigit · isalpha는 실습코드에 없다.
-->

---
layout: section
---

# 문제

LAB-02 ~ LAB-05에서 배운 것을 모두 써야 풀리는 문제 하나

---
class: dense
---

## #03. 문제 — 이상한 문자 만들기

<Grid cols="1fr 1fr" align="start">
<div>

문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

<div class="kicker">제한 사항</div>

- 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
- 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

| s | return |
|:--|:--|
| "try hello world" | "TrY HeLlO WoRlD" |

<p class="small muted">출처: <a href="https://school.programmers.co.kr/learn/courses/30/lessons/12930" target="_blank" rel="noopener">프로그래머스 코딩테스트 연습 「이상한 문자 만들기」</a></p>

</div>
<div>

<div class="kicker">입출력 예 설명</div>

"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

<div class="kicker">기본 코드 템플릿</div>

```python
def solution(s):
    answer = ''
    return answer

s = "try hello world"
print(solution(s))  # TrY HeLlO WoRlD
```

<Callout kind="warn" title="공백은 하나 이상">
단어 사이 공백이 <b>두 개 이상</b>일 수도 있다. 공백은 그대로 둔다
</Callout>

</div>
</Grid>

<!--
문제 원문은 프로그래머스 그대로다.
쓰는 문법: 함수 정의와 return(LAB-02), for · if · else · %(LAB-03), 인덱스 · len · join(LAB-04), upper · lower · split · 문자열 인덱싱 · +=(LAB-05).
핵심 함정 두 가지. ① 인덱스는 단어마다 0부터 다시 센다. ② "하나 이상의 공백"이라 단어 사이에 공백이 여러 개일 수 있고, 그 공백은 그대로 남겨야 한다. 입출력 예는 공백이 하나뿐이라 두 함정을 모두 놓친 코드도 통과한다(3단계 증상 참고).
기본 코드 템플릿의 def 부분은 프로그래머스 Python3 편집기에 처음 들어 있는 코드와 같고, s · print 두 줄은 노트북에서 입출력 예를 확인하려고 덧붙인 것이다. 프로그래머스에 제출할 때는 solution 함수만 붙여 넣는다.
-->

---
layout: section
---

# 풀이 단계

설계 → 구현 → 원인 찾기, 세 단계로 푼다

---

## #04. AI와 함께 푸는 세 단계

<Steps color="pastel">
<li><b>AI에게 물어 문제를 확인하고 함수를 설계한다</b> — 내 정리를 점검받고, 처리 순서를 단계표로 받는다 <Chip color="ai">프롬프트 ② + ⑤</Chip></li>
<li><b>코드를 직접 쓴다</b> — 단계표를 주석으로 옮겨 채우고, 결과를 예측한 뒤 실행한다 <Chip color="ok">코드 작성 · AI 없이</Chip></li>
<li><b>틀리면 AI와 함께 원인을 찾아 고친다</b> — 예측과 실제 출력을 보내 갈라진 지점을 찾는다 <Chip color="ai">프롬프트 ⑬</Chip></li>
</Steps>

<Core color="ai">AI는 설계와 원인 찾기를 돕는다. 코드는 처음부터 끝까지 내가 쓴다.</Core>

<!--
LAB-03 · 04와 같은 세 단계다. 단계마다 쓸 템플릿을 붙였을 뿐이다.
1단계를 건너뛰면 2단계에서 "인덱스를 어디서 다시 0으로 만드는지"가 흔들린다. 문제 정리를 꼭 점검받게 한다.
-->

---
class: dense
---

## #05. 1단계 — AI에게 물어 문제를 확인하고 함수를 설계한다

<Callout icon="💡" title="문제를 제대로 이해했는지 확인하고, 어떤 순서로 코드를 쓸지 정하고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ② + ⑤번 패턴">

````md
## 맥락
파이썬 문자열 단원을 배우는 중이야. 코딩 테스트 문제를 풀기 전에 문제를 내 말로 정리했어.

## 상황
문제: {문제 원문 붙여 넣기}

내 정리:
- 글자 하나로 할 일: {내가 이해한 내용}
- 인덱스를 세는 기준: {내가 이해한 내용}
- 공백 처리: {내가 이해한 내용}

## 질문
1. 내 정리에서 문제와 다르게 이해한 부분과 빠진 부분을 짚어 줘
2. 그다음 처음부터 끝까지 해야 할 일을 단계 순서로 나눠 줘

## 제약
- 코드나 의사코드 없이 말로만
- 배운 범위(함수 정의 · 조건문 · for · 인덱스 · len · split · join · upper · lower · 문자열 연산) 안에서. 딕셔너리 · 리스트 컴프리헨션 · lambda · enumerate는 쓰지 않는 방법으로

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
문제 원문은 줄이지 않고 그대로 붙인다. 답에 enumerate · 컴프리헨션이 섞이면 <code>## 제약</code>을 가리키며 다시 묻는다
</Callout>

</div>
</Grid>

<!--
LAB-02의 ② 내 설명 점검받기와 ⑤ 단계로 쪼개기를 한 프롬프트로 묶었다(LAB-03 · 04와 같다).
학생이 자주 빠뜨리는 정리: 인덱스는 단어마다 0부터 다시 센다, 공백은 여러 개일 수 있고 그대로 남긴다, 홀수번째는 소문자로 "바꾼다"(원래 대문자인 글자도 소문자가 된다).
기대하는 단계표(글자를 하나씩 보는 방법): ① 결과 문자열을 빈 문자열로, 단어 안 인덱스를 0으로 준비 ② s에서 글자를 하나씩 꺼냄 ③ 공백이면 그대로 붙이고 인덱스를 0으로 되돌림 ④ 공백이 아니면 인덱스가 짝수면 대문자, 홀수면 소문자로 붙임 ⑤ 인덱스를 1 늘림 ⑥ 반복이 끝나면 결과를 돌려줌.
AI가 split(" ")으로 단어를 나눠 바꾼 뒤 " ".join으로 다시 붙이는 단계표를 줘도 맞다. split()처럼 괄호를 비우라고 하면 공백이 여러 개일 때 틀린다(3단계 · 마무리 ⑮로 이어짐).
-->

---
class: dense
---

## #06. 2단계 — 단계표를 보고 코드를 직접 쓴다

<Callout icon="💡" title="1단계에서 받은 단계표를 AI 없이 내 손으로 코드로 옮기는 단계" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<div class="kicker">단계표를 주석으로 옮긴 뼈대</div>

```python
def solution(s):
    # 1. {단계표 1번}
    # 2. {단계표 2번}
    #    ...
    # 6. {단계표 마지막 번}
    return answer

print(solution("try hello world"))  # 내 예측: ?
print(solution("try  hello"))       # 내 예측: ? (공백 두 칸)
```

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 주석 아래에 **한 줄씩** 코드를 채운다
- 실행하기 전에 두 print의 결과를 **예측**해 적는다
- 실행해서 예측 · 기대 결과와 맞춰 본다

</div>

<Callout kind="tip" title="문자열은 고쳐 쓸 수 없다">
<code>s[0] = "T"</code>는 에러다. 바꾼 글자를 새 문자열에 <code>+=</code>로 이어 붙인다
</Callout>

</div>
</Grid>

<!--
단계표의 각 줄이 코드 몇 줄이 되는지 직접 옮기는 것이 이 단계의 핵심이다. 주석은 지우지 말고 남겨 두게 한다. 3단계에서 어느 줄이 틀렸는지 찾을 때 쓴다.
예측은 결과 값만 적는다. 첫 줄은 TrY HeLlO WoRlD, 둘째 줄은 TrY  HeLlO(공백 두 칸 그대로). 자주 빗나가는 예측: 둘째 줄의 공백을 한 칸으로 봄.
결과를 볼 때 print(repr(solution("try  hello")))로 찍으면 따옴표 안의 공백 개수가 잘 보인다.
막힌 문법은 ④ 고르는 기준 묻기 정도만 허용하고 "코드로 써 줘"는 묻지 않게 한다.

강사용 정답 코드(학생 자료에는 없음):
def solution(s):
    answer = ''
    idx = 0
    for ch in s:
        if ch == ' ':
            answer += ch
            idx = 0
        else:
            if idx % 2 == 0:
                answer += ch.upper()
            else:
                answer += ch.lower()
            idx += 1
    return answer

print(solution("try hello world"))  # TrY HeLlO WoRlD
다른 풀이: words = s.split(' ')로 나눈 뒤 단어마다 for i in range(len(w))로 새 단어를 만들어 리스트에 append하고, ' '.join(리스트)로 돌려준다. split(' ')는 연속 공백 사이에 빈 문자열을 남기므로 공백 개수가 그대로 돌아온다.
더 확인할 값(직접 실행): "try  hello" → "TrY  HeLlO", " ab" → " Ab", "a" → "A".
-->

---
class: dense
---

## #07. 3단계 — 틀리면 AI와 함께 원인을 찾아 고친다

<Callout icon="💡" title="실행 결과가 기대 결과나 내 예측과 달라서, 어디서 왜 갈라졌는지 알고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑬번 패턴">

````md
## 맥락
파이썬 문자열 단원을 배우는 중이야.

## 상황
이상한 문자 만들기 solution 함수를 직접 썼는데 결과가 내 예측과 달랐어.
```python
{내가 쓴 코드}
```
입력: {예: "try  hello" (공백 두 칸)}
내 예측: {예: "TrY  HeLlO"}
실제 출력: {예: "TrY HeLlO" · 에러가 났으면 에러 원문 그대로}

## 질문
내 예측이 어느 지점에서 실제 실행과 갈라졌는지, 왜 그렇게 실행되는지 알려줘.

## 제약
- 코드를 고쳐 쓰지 마. 실행 순서와 이유만 설명해
- 문자열 인덱싱 · split · join · upper · lower · for 범위 안에서

## 출력 형식
| 갈라진 지점 | 내 예측 | 실제 | 이유 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 입력 · 예측 · 실제 출력을 **그대로** 붙인다
- 갈라진 지점과 이유만 받고, **고치는 건 내가** 한다
- 고친 뒤 두 print를 다시 실행해 확인한다

</div>

<Callout kind="danger" title="입출력 예만 맞았을 때">
입출력 예는 공백이 한 칸뿐이다. 공백 두 칸 입력이 틀리면 <b>통과한 게 아니다</b>
</Callout>

</div>
</Grid>

<!--
LAB-03에서 배운 ⑬을 그대로 쓴다. 입력이 두 가지라 ## 상황에 "입력" 줄을 더했다. AI 설명도 추측이므로, 고친 뒤 다른 입력으로 다시 예측 → 실행해 확인하게 한다.
강사용 증상과 원인(모두 Python 3.13으로 직접 실행해 확인):
"TrY HeLlO"(공백이 한 칸으로 줄어듦) — s.split()처럼 괄호를 비워 나눔. 연속 공백을 하나의 구분자로 보고 빈 문자열을 남기지 않는다. 입출력 예는 통과한다(마무리 ⑮로 이어짐).
"TrY  hElLo" — 문자열 전체의 인덱스 i로 짝홀을 판단함. 입출력 예는 단어 길이가 우연히 맞아 통과하지만 공백 두 칸에서 틀린다.
"TrY hElLo WoRlD" — 공백을 만났을 때 단어 안 인덱스를 0으로 되돌리지 않음. 입출력 예에서 바로 틀린다.
"TrY  hElLo  wOrLd" — 공백 처리 뒤에 else 없이 아래 if로 이어져 공백이 두 번 붙고 인덱스도 어긋남.
"try hello world"(아무것도 안 바뀜) — ch.upper()의 결과를 받지 않고 원래 ch를 붙임. 문자열 메서드는 원본을 바꾸지 않고 새 문자열을 돌려준다.
['TrY', 'HeLlO', 'WoRlD'] — split 풀이에서 ' '.join 없이 리스트를 그대로 돌려줌.
TypeError: 'str' object does not support item assignment — answer[i] = ...처럼 문자열의 글자를 바꾸려 함.
-->

---
class: dense
---

## #08. 마무리 — ⑮ 근거와 함께 묻기

<Callout icon="💡" title="AI가 알려 준 메서드의 동작이 정말 맞는지, 근거를 받아 직접 확인하고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑮번 패턴 (오늘 새 패턴)">

````md
## 맥락
파이썬 문자열 단원을 배우는 중이야. 이상한 문자 만들기 문제를 내가 풀었어.

## 상황
split()과 split(" ")이 공백이 여러 개인 문자열에서 다르게 나눈다고 들었어.
내가 아는 차이: {내가 아는 것. 모르면 "모르겠음"}

## 질문
두 방법이 "try  hello"(공백 두 칸)를 어떻게 나누는지, 그 근거가 파이썬 공식 문서 어디에 나오는지 알려줘.

## 제약
- 코드 대신 말로 설명하고, 각 설명마다 내가 직접 실행해 확인할 방법을 알려줘
- 공식 문서(docs.python.org/ko)의 문서 이름과 절 이름을 적어. 확실하지 않으면 "확인 필요"라고 표시해

## 출력 형식
| 항목 | split() | split(" ") | 근거 (문서 · 절) | 확인 방법 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 보내기 전에 **내가 아는 차이**를 먼저 적는다
- 알려 준 절을 공식 문서에서 **직접 열어** 본다
- 「확인 방법」을 실행해 맞으면 ✔, 다르면 실제 결과를 적는다

</div>

<Callout kind="warn" title="주의">
AI가 적은 문서 이름 · 절 이름도 추측이다. 직접 열어 봐야 근거가 된다
</Callout>

</div>
</Grid>

<!--
새 템플릿 ⑮. LAB-02의 ①~⑫, LAB-03의 ⑬, LAB-04의 ⑭ 뒤로 이어 매긴다. AI가 그럴듯하게 틀리기 쉬운 "메서드의 세부 동작"을 공식 문서와 실행 두 가지로 확인하는 첫 활동이다.
기대하는 답: split()은 sep을 주지 않으면 연속된 공백을 하나의 구분자로 보고 앞뒤 공백도 무시한다. split(" ")은 공백 한 칸마다 나누므로 연속 공백 사이에 빈 문자열이 생긴다. 근거는 공식 문서 「내장형」 → 「문자열 메서드」의 str.split 항목.
확인 방법 예(직접 실행): "try  hello".split() → ['try', 'hello'] / "try  hello".split(" ") → ['try', '', 'hello'].
문서 위치가 틀린 답이 나오면 실패가 아니라 AI의 환각을 잡아낸 것으로 다룬다. 학생이 split() 풀이로 3단계 증상을 겪었다면 이 표가 그 원인의 근거가 된다.
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-05] 문자열 4 · ITWILL · {teacher} 강사</p>

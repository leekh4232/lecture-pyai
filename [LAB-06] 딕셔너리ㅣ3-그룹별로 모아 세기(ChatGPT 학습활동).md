---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 딕셔너리 — 딕셔너리 종합문제
layout: cover
---

# 딕셔너리 종합문제

AI에게 물으며 푸는 코딩 테스트 — 프로그래머스 「완주하지 못한 선수」

<p class="sub">[LAB-06] 딕셔너리 3 · ITWILL · {teacher} 강사</p>

<!--
딕셔너리 단원 1~2(딕셔너리의 이해 · 딕셔너리 관련 함수)를 마친 뒤 하는 실습. ① 조언 받기 단계(LAB-02 ~ 06)의 마지막 실습이다. 코드는 학생이 쓰고, ChatGPT는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 맡는다(「ChatGPT 지침.md」 그대로).
LAB-03 · 04와 같은 틀이다. LAB-02 ~ 06에서 배운 것을 모두 써야 풀리는 코딩 테스트 문제(프로그래머스 「완주하지 못한 선수」) 하나를 세 단계로 푼다. 단계마다 프롬프트 하나 또는 코드 작성 하나만 한다: 1단계 프롬프트(② + ⑤), 2단계 코드 작성, 3단계 프롬프트(⑬). 마무리는 오늘 새 템플릿 ⑯ 값까지 가는 경로 묻기.
다음 LAB-07부터는 AI에게 코드를 직접 받는 단계로 넘어가므로, 조언 받기 단계를 마무리하는 시간이기도 하다.
-->

---

## #01. 오늘의 흐름

<Timeline>
<li><b>문제 읽기</b>코딩 테스트 문제와 입출력 예를 본다</li>
<li><b>세 단계로 풀기</b>설계는 AI와 함께, 코드는 내가, 틀리면 다시 AI와 함께</li>
<li class="now"><b>마무리</b>⑯ 값까지 가는 경로 묻기로 딕셔너리 값이 어떻게 바뀌는지 점검한다</li>
</Timeline>

<Grid cols="2" align="start">

<Callout kind="real" title="오늘의 규칙">

- 코드는 내가 쓰고, AI에게는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 묻는다
- 첫 질문은 다섯 섹션 `## 맥락` `## 상황` `## 질문` `## 제약` `## 출력 형식`으로 자세히, 같은 대화의 후속 질문은 평서문으로

</Callout>

<Tile kind="soft" color="ai" tag="오늘 새로 더하는 템플릿" title="⑯ 값까지 가는 경로 묻기">
LAB-05의 ⑮ 뒤로 이어 매긴다. 값 하나가 지금 모습이 되기까지 거친 단계를 내가 먼저 적고 점검받는다
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
| LAB-02 · 03 | 변수 · 연산자 · 함수 정의(파라미터 · return) · if · elif · else · while · for · range · 중첩 · break · continue |
| LAB-04 리스트 | 인덱스 · 슬라이싱 · 2차원 리스트 · 구조분해 · in · not in · len · sorted · sort · append · count · index 등 |
| LAB-05 문자열 | 문자열 연산 · 인덱싱 · 슬라이싱 · 포메팅 · f-string · upper · lower · strip · replace · split 등 |
| LAB-06 딕셔너리 | 키 · 값 · 추가 · 변경 · 복합 구조 · len · del · get(기본값 포함) · keys · values · items · update · copy · clear |

<Callout kind="danger" title="아직 안 배운 것 — 쓰지 않는다">
리스트 · 딕셔너리 컴프리헨션 · lambda · <code>collections</code>(Counter 등) 모듈 · try-except
</Callout>

<Core color="ok">AI가 안 배운 방법을 권하면 따르지 않고, 배운 범위 안의 방법으로 다시 묻는다.</Core>

<!--
범위를 적지 않으면 AI가 collections.Counter로 두 명단을 빼는 한 줄 풀이(return list((Counter(participant) - Counter(completion)).keys())[0])를 권한다. 모듈은 LAB-10에서 배운다. 오늘은 빈 딕셔너리와 get으로 직접 센다.
컴프리헨션 · lambda · Counter · try-except는 LAB-02 ~ 06 실습코드에 나오지 않는다(직접 확인).
-->

---
layout: section
---

# 문제

LAB-02 ~ LAB-06에서 배운 것을 모두 써야 풀리는 문제 하나

---
class: dense
---

## #03. 문제 — 완주하지 못한 선수

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

<div class="kicker">입출력 예</div>

| participant | completion | return |
|:--|:--|:--|
| ["leo", "kiki", "eden"] | ["eden", "kiki"] | "leo" |
| ["marina", "josipa", "nikola", "vinko", "filipa"] | ["josipa", "filipa", "marina", "nikola"] | "vinko" |
| ["mislav", "stanko", "mislav", "ana"] | ["stanko", "ana", "mislav"] | "mislav" |

<p class="small muted">출처: <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42576" target="_blank" rel="noopener">프로그래머스 코딩테스트 연습 「완주하지 못한 선수」</a></p>

<!--
문제 원문은 프로그래머스 그대로다(2023년 1월 25일 테스트케이스가 추가된 판).
쓰는 문법: 함수 정의와 return(LAB-02), for · if(LAB-03), 리스트 순회(LAB-04), 빈 딕셔너리 · 키로 값 바꾸기 · get(키, 기본값) · keys(LAB-06).
핵심 함정은 동명이인이다. 이름이 명단에 "있는지"만 보면 예제 #3에서 답을 못 찾는다. 이름마다 "몇 명인지"를 세어야 한다. 딕셔너리로 이름별 인원을 모아 세는 문제라 오늘 단원과 바로 이어진다.
-->

---

## #04. 제한사항 · 입출력 예 설명과 기본 코드

<Grid cols="1fr 1fr" align="start">
<div>

<div class="kicker">제한사항</div>

- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

<div class="kicker">입출력 예 설명</div>

<Steps>
<li>"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.</li>
<li>"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.</li>
<li>"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.</li>
</Steps>

</div>
<div>

<div class="kicker">기본 코드 템플릿</div>

```python
def solution(participant, completion):
    answer = ''
    return answer

participant = ["mislav", "stanko",
               "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# 기대 결과: mislav
print(solution(participant, completion))
```

<Callout kind="warn" title="동명이인">
이름이 명단에 <b>있는지</b>가 아니라, 이름마다 <b>몇 명인지</b>를 봐야 한다
</Callout>

</div>
</Grid>

<!--
제한사항과 입출력 예 설명은 프로그래머스 원문 그대로다(예제 #1 ~ #3). 원문은 문제 설명 · 제한사항 · 입출력 예 · 설명 순이지만, 한 쪽에 들어가지 않아 제한사항을 이 쪽으로 옮겼다.
기본 코드 템플릿의 def 부분은 프로그래머스 Python3 편집기에 처음 들어 있는 코드와 같고, participant · completion · print 줄은 노트북에서 입출력 예를 확인하려고 덧붙인 것이다. 일부러 동명이인이 있는 예제 #3을 넣었다. 프로그래머스에 제출할 때는 solution 함수만 붙여 넣는다.
-->

---
layout: section
---

# 풀이 단계

설계 → 구현 → 원인 찾기, 세 단계로 푼다

---

## #05. AI와 함께 푸는 세 단계

<Steps color="pastel">
<li><b>AI에게 물어 문제를 확인하고 함수를 설계한다</b> — 내 정리를 점검받고, 처리 순서를 단계표로 받는다 <Chip color="ai">프롬프트 ② + ⑤</Chip></li>
<li><b>코드를 직접 쓴다</b> — 단계표를 주석으로 옮겨 채우고, 결과를 예측한 뒤 실행한다 <Chip color="ok">코드 작성 · AI 없이</Chip></li>
<li><b>틀리면 AI와 함께 원인을 찾아 고친다</b> — 예측과 실제 출력을 보내 갈라진 지점을 찾는다 <Chip color="ai">프롬프트 ⑬</Chip></li>
</Steps>

<Core color="ai">AI는 설계와 원인 찾기를 돕는다. 코드는 처음부터 끝까지 내가 쓴다.</Core>

<!--
LAB-03 · 04와 같은 세 단계다. 단계마다 쓸 템플릿을 붙였을 뿐이다.
1단계를 건너뛰면 2단계에서 "이름이 있는지"만 보는 코드를 쓰기 쉽다. 동명이인을 정리에 넣었는지 꼭 점검받게 한다.
-->

---
class: dense
---

## #06. 1단계 — AI에게 물어 문제를 확인하고 함수를 설계한다

<Callout icon="💡" title="문제를 제대로 이해했는지 확인하고, 어떤 순서로 코드를 쓸지 정하고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ② + ⑤번 패턴">

````md
## 맥락
파이썬 딕셔너리 단원을 배우는 중이야. 코딩 테스트 문제를 풀기 전에 문제를 내 말로 정리했어.

## 상황
문제: {문제 원문 붙여 넣기}

내 정리:
- 세어야 할 것: {내가 이해한 내용}
- 두 명단을 쓰는 방법: {내가 이해한 내용}
- 돌려줄 값: {내가 이해한 내용}

## 질문
1. 내 정리에서 문제와 다르게 이해한 부분과 빠진 부분을 짚어 줘
2. 그다음 처음부터 끝까지 해야 할 일을 단계 순서로 나눠 줘

## 제약
- 코드나 의사코드 없이 말로만
- 배운 범위(함수 정의 · 조건문 · for · 리스트 · 딕셔너리 · get · keys · values · items) 안에서. 컴프리헨션 · lambda · collections 모듈은 쓰지 않는 방법으로

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
문제 원문은 줄이지 않고 그대로 붙인다. 답에 Counter · 컴프리헨션이 섞이면 <code>## 제약</code>을 가리키며 다시 묻는다
</Callout>

</div>
</Grid>

<!--
LAB-02의 ② 내 설명 점검받기와 ⑤ 단계로 쪼개기를 한 프롬프트로 묶었다(LAB-03 · 04와 같다).
학생이 자주 빠뜨리는 정리: 동명이인이 있으니 이름별 인원을 센다, 완주자 명단으로 그 인원을 하나씩 줄인다, 남은 인원이 0보다 큰 이름 하나가 답이다, 답은 리스트가 아니라 이름 문자열 하나다.
기대하는 단계표: ① 이름별 인원을 담을 빈 딕셔너리 준비 ② 참가자 명단을 하나씩 보며 그 이름의 인원을 1 늘림(처음 나온 이름은 0에서 시작) ③ 완주자 명단을 하나씩 보며 그 이름의 인원을 1 줄임 ④ 딕셔너리의 이름을 하나씩 보며 인원이 0보다 큰 이름을 찾음 ⑤ 그 이름을 돌려줌.
AI가 "두 명단을 정렬해서 앞에서부터 비교"하는 방법을 내놓아도 배운 범위(sort · sorted)라 틀린 답은 아니다. 오늘은 딕셔너리 단원이므로 1의 방법으로 단계표를 다시 받게 한다.
-->

---
class: dense
---

## #07. 2단계 — 단계표를 보고 코드를 직접 쓴다

<Callout icon="💡" title="1단계에서 받은 단계표를 AI 없이 내 손으로 코드로 옮기는 단계" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<div class="kicker">단계표를 주석으로 옮긴 뼈대</div>

```python
def solution(participant, completion):
    # 1. {단계표 1번}
    # 2. {단계표 2번}
    #    ...
    # 5. {단계표 마지막 번}
    return answer

# 내 예측: ?
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# 내 예측: ?
print(solution(participant, completion))
```

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 주석 아래에 **한 줄씩** 코드를 채운다
- 실행하기 전에 두 print의 결과를 **예측**해 적는다
- 실행해서 예측 · 기대 결과와 맞춰 본다

</div>

<Callout kind="tip" title="처음 나온 키를 세려면">
<code>get(키, 0)</code>은 키가 없으면 0을 돌려준다. 없는 키를 <code>[키]</code>로 꺼내면 에러가 난다
</Callout>

</div>
</Grid>

<!--
단계표의 각 줄이 코드 몇 줄이 되는지 직접 옮기는 것이 이 단계의 핵심이다. 주석은 지우지 말고 남겨 두게 한다. 3단계에서 어느 줄이 틀렸는지 찾을 때 쓴다.
예측은 결과 값만 적는다. 첫 줄은 leo, 둘째 줄은 mislav. 자주 빗나가는 예측: 둘째 줄을 "없음"으로 봄(mislav가 완주자 명단에도 있으니 완주했다고 생각함).
값이 다르면 반복문 안에 print(name, count)를 넣어 딕셔너리가 한 줄씩 어떻게 바뀌는지 본다(마무리 ⑯으로 이어짐).
막힌 문법은 ④ 고르는 기준 묻기 정도만 허용하고 "코드로 써 줘"는 묻지 않게 한다.

강사용 정답 코드(학생 자료에는 없음):
def solution(participant, completion):
    count = {}
    for name in participant:
        count[name] = count.get(name, 0) + 1
    for name in completion:
        count[name] = count[name] - 1
    for name in count.keys():
        if count[name] > 0:
            return name

입출력 예 세 개 → leo / vinko / mislav (직접 실행).
완주자는 모두 참가자이므로 두 번째 반복에서는 count[name]으로 꺼내도 에러가 나지 않는다. count[name] -= 1로 써도 된다.
정렬로 푸는 방법도 배운 범위 안이다: participant와 completion을 정렬한 뒤 같은 인덱스끼리 비교해 처음 다른 참가자를 돌려주고, 끝까지 같으면 participant의 마지막 이름을 돌려준다(직접 실행: leo, mislav).
-->

---
class: dense
---

## #08. 3단계 — 틀리면 AI와 함께 원인을 찾아 고친다

<Callout icon="💡" title="실행 결과가 기대 결과나 내 예측과 달라서, 어디서 왜 갈라졌는지 알고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑬번 패턴">

````md
## 맥락
파이썬 딕셔너리 단원을 배우는 중이야.

## 상황
완주하지 못한 선수 solution 함수를 직접 썼는데 결과가 내 예측과 달랐어.
```python
{내가 쓴 코드}
```
내 예측: {예: mislav}
실제 출력: {예: None · 에러가 났으면 에러 원문 그대로}

## 질문
내 예측이 어느 지점에서 실제 실행과 갈라졌는지, 왜 그렇게 실행되는지 알려줘.

## 제약
- 코드를 고쳐 쓰지 마. 실행 순서와 이유만 설명해
- 리스트 · 딕셔너리 · get · keys 범위 안에서

## 출력 형식
| 갈라진 지점 | 내 예측 | 실제 | 이유 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 예측과 실제 출력을 **그대로** 붙인다
- 갈라진 지점과 이유만 받고, **고치는 건 내가** 한다
- 고친 뒤 두 print를 다시 실행해 확인한다

</div>

<Callout kind="danger" title="에러가 났을 때">
에러 메시지는 마지막 줄만이 아니라 <b>몇 번째 줄</b>에서 났는지까지 함께 붙인다
</Callout>

</div>
</Grid>

<!--
LAB-03에서 배운 ⑬을 그대로 쓴다. AI 설명도 추측이므로, 고친 뒤 다른 입력으로 다시 예측 → 실행해 확인하게 한다.
강사용 증상과 원인(모두 Python 3.13으로 직접 실행해 확인, 입출력 예 #1 / #2 / #3 순):
KeyError: 'leo' — count[name] += 1처럼 처음 나온 이름을 get 없이 늘림. 빈 딕셔너리에 없는 키를 꺼내려 해서 첫 이름에서 바로 에러가 난다.
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int' — count.get(name) + 1처럼 기본값 0을 빼먹음. 없는 키의 get은 None을 돌려준다.
leo / vinko / None — count[name] = 1처럼 늘리지 않고 1을 넣음. 동명이인 mislav가 1명으로 세어져 완주자 명단에서 0이 된다. 딕셔너리 없이 if name not in completion으로 찾아도 같은 결과(mislav는 완주자 명단에 있으므로)가 나온다.
leo / '' / mislav — 마지막 반복의 if 아래에 else: return ""을 둠. 첫 이름(marina)이 0이라 바로 빈 문자열을 돌려주고 끝난다.
leo / marina / mislav — 완주자 반복에서도 count.get(name, 0) + 1로 늘림(복사해 붙이고 - 로 안 바꿈). 모든 인원이 0보다 커서 첫 이름이 답이 된다.
-->

---
class: dense
---

## #09. 마무리 — ⑯ 값까지 가는 경로 묻기

<Callout icon="💡" title="정답은 나왔는데, 딕셔너리의 값 하나가 어떤 순서로 그 값이 됐는지 확실히 알고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑯번 패턴 (오늘 새 패턴)">

````md
## 맥락
파이썬 딕셔너리 단원을 배우는 중이야. 완주하지 못한 선수 문제를 내가 풀었어.

## 상황
내가 쓴 코드:
```python
{내가 쓴 코드}
```
입력: 입출력 예 #3 (participant에 mislav가 두 명)
"mislav"의 값이 마지막에 1이 되기까지 내가 생각한 경로:
없음 → {내 생각} → ... → 1

## 질문
내 경로가 맞는지, 틀렸다면 몇 번째 단계에서 무엇이 틀렸는지 알려줘. 단계마다 어느 줄이 실행되어 값이 어떻게 바뀌는지도 알려줘.

## 제약
- 코드를 고쳐 쓰지 마. 단계와 값으로만 설명해
- 리스트 · 딕셔너리 · get 범위 안에서

## 출력 형식
| 단계 | 실행된 줄 | 그때 꺼낸 이름 | "mislav"의 값 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 보내기 전에 **내 경로**를 먼저 적는다
- 반복문마다 `print(name, count)`를 넣어 실행한다
- 찍힌 값과 받은 표를 단계마다 맞춰 본다

</div>

<Callout kind="warn" title="주의">
{내 생각}을 비워 두고 보내지 않는다. 경로를 먼저 적어야 점검을 받는다
</Callout>

</div>
</Grid>

<!--
새 템플릿 ⑯. LAB-02의 ①~⑫, LAB-03의 ⑬, LAB-04의 ⑭, LAB-05의 ⑮ 뒤로 이어 매긴다. 값 하나가 지금 모습이 되기까지 거친 단계(중첩 구조라면 들어가는 key · 인덱스, 반복이라면 값이 바뀐 순서)를 내가 먼저 적고 점검받는 템플릿이다. 조언 받기 단계의 마지막 새 템플릿이다.
기대하는 경로: 없음 → 1(참가자 첫 번째 mislav, get 기본값 0에 1을 더함) → 2(참가자 세 번째 mislav) → 1(완주자 세 번째 mislav에서 1을 뺌).
print(name, count)를 두 반복에 넣으면 찍히는 값(직접 실행):
mislav {'mislav': 1}
stanko {'mislav': 1, 'stanko': 1}
mislav {'mislav': 2, 'stanko': 1}
ana {'mislav': 2, 'stanko': 1, 'ana': 1}
stanko {'mislav': 2, 'stanko': 0, 'ana': 1}
ana {'mislav': 2, 'stanko': 0, 'ana': 0}
mislav {'mislav': 1, 'stanko': 0, 'ana': 0}
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-06] 딕셔너리 3 · ITWILL · {teacher} 강사</p>

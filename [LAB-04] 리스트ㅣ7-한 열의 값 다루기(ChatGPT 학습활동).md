---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 리스트 — 리스트 종합문제
layout: cover
---

# 리스트 종합문제

AI에게 물으며 푸는 코딩 테스트 — 프로그래머스 「K번째수」

<p class="sub">[LAB-04] 리스트 7 · ITWILL · {teacher} 강사</p>

<!--
리스트 단원(리스트의 이해 · 인덱싱과 슬라이싱 · 원소 복사 · 리스트 탐색 · 리스트 관련 함수)을 마친 뒤 하는 실습. ① 조언 받기 단계(LAB-02 ~ 06)라서 코드는 학생이 쓰고, ChatGPT는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 맡는다(「ChatGPT 지침.md」 그대로).
LAB-03과 같은 틀이다. LAB-02 ~ 04에서 배운 것을 모두 써야 풀리는 코딩 테스트 문제(프로그래머스 「K번째수」) 하나를 세 단계로 푼다. 단계마다 프롬프트 하나 또는 코드 작성 하나만 한다: 1단계 프롬프트(② + ⑤), 2단계 코드 작성, 3단계 프롬프트(⑬). 마무리는 오늘 새 템플릿 ⑭ 두 방법 비교받기.
-->

---

## #01. 오늘의 흐름

<Timeline>
<li><b>문제 읽기</b>코딩 테스트 문제와 입출력 예를 본다</li>
<li><b>세 단계로 풀기</b>설계는 AI와 함께, 코드는 내가, 틀리면 다시 AI와 함께</li>
<li class="now"><b>마무리</b>⑭ 두 방법 비교받기로 내가 쓴 정렬 방법을 이해했는지 점검한다</li>
</Timeline>

<Grid cols="2" align="start">

<Callout kind="real" title="오늘의 규칙">

- 코드는 내가 쓰고, AI에게는 개념 · 처리 순서 · 결과 해석 · 에러 원인만 묻는다
- 첫 질문은 다섯 섹션 `## 맥락` `## 상황` `## 질문` `## 제약` `## 출력 형식`으로 자세히, 같은 대화의 후속 질문은 평서문으로

</Callout>

<Tile kind="soft" color="ai" tag="오늘 새로 더하는 템플릿" title="⑭ 두 방법 비교받기">
LAB-03의 ⑬ 뒤로 이어 매긴다. 비슷한 두 방법의 차이를 표로 받고, 각 칸을 직접 실행해 확인한다
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
| LAB-02 변수 · 함수 | 변수 · 산술 · 비교 · 논리 연산자 · `+=` · print · int · str · 함수 정의(파라미터 · return) |
| LAB-03 흐름제어 | if · elif · else · while · for · range · 중첩 조건문 · 중첩 반복문 · break · continue |
| LAB-04 리스트 | 인덱스(역방향 포함) · 슬라이싱 · 2차원 리스트 · 복사 · 구조분해 · in · len · sorted · max · min · sum · append · insert · pop · remove · sort · reverse · count · index |

<Callout kind="danger" title="아직 안 배운 것 — 쓰지 않는다">
리스트 컴프리헨션(<code>[x for x in ...]</code>) · lambda · 딕셔너리 · 문자열 함수
</Callout>

<Core color="ok">AI가 안 배운 방법을 권하면 따르지 않고, 배운 범위 안의 방법으로 다시 묻는다.</Core>

<!--
범위를 적지 않으면 AI가 리스트 컴프리헨션 한 줄(return [sorted(array[i-1:j])[k-1] for i, j, k in commands])로 푸는 방법을 권한다. 오늘은 for와 append로 결과를 하나씩 쌓는다.
리스트 컴프리헨션 · lambda는 리스트 단원 실습코드에 나오지 않는다(직접 확인).
-->

---
layout: section
---

# 문제

LAB-02 ~ LAB-04에서 배운 것을 모두 써야 풀리는 문제 하나

---
class: dense
---

## #03. 문제 — K번째수

<Grid cols="1fr 1fr" align="start">
<div>

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

```text
1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
3. 2에서 나온 배열의 3번째 숫자는 5입니다.
```

배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

<p><Chip color="py">제한 사항</Chip> array의 길이와 각 원소는 1 이상 100 이하. commands의 길이는 1 이상 50 이하, 각 원소는 길이가 3</p>

</div>
<div>

| array | commands | return |
|:--|:--|:--|
| [1, 5, 2, 6, 3, 7, 4] | [[2, 5, 3], [4, 4, 1], [1, 7, 3]] | [5, 6, 3] |

<p class="small muted">출처: <a href="https://school.programmers.co.kr/learn/courses/30/lessons/42748" target="_blank" rel="noopener">프로그래머스 코딩테스트 연습 「K번째수」</a></p>

</div>
</Grid>

<!--
문제 원문은 프로그래머스 그대로다. 제한 사항 네 줄만 한 줄로 묶었다.
쓰는 문법: 함수 정의와 return(LAB-02), for(LAB-03), 2차원 리스트 · 구조분해 · 슬라이싱 · 인덱스 · sorted 또는 sort · append(LAB-04).
핵심 함정은 "번째"와 인덱스의 차이다. 문제의 i번째 · k번째는 1부터 세고, 파이썬 인덱스는 0부터 센다. 슬라이싱 끝 위치는 포함되지 않는다. 그래서 i번째부터 j번째까지는 array[i-1:j], k번째는 [k-1]이다.
-->

---

## #04. 입출력 예 설명과 기본 코드

<Grid cols="1fr 1fr" align="start">
<div>

<div class="kicker">입출력 예 설명</div>

<Steps>
<li>[1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.</li>
<li>[1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.</li>
<li>[1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.</li>
</Steps>

</div>
<div>

<div class="kicker">기본 코드 템플릿</div>

```python
def solution(array, commands):
    answer = []
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))  # [5, 6, 3]
```

<Callout kind="warn" title="번째와 인덱스">
문제의 i번째 · k번째는 <b>1부터</b> 센다. 파이썬 인덱스는 0부터 센다
</Callout>

</div>
</Grid>

<!--
입출력 예 설명은 프로그래머스 원문 그대로다. 둘째 명령 [4, 4, 1]처럼 i와 j가 같으면 원소 하나만 잘린다. 인덱스를 1부터 세면 여기서 빈 리스트가 되어 IndexError가 난다(3단계).
기본 코드 템플릿의 def 부분은 프로그래머스 Python3 편집기에 처음 들어 있는 코드와 같고, array · commands · print 세 줄은 노트북에서 입출력 예를 확인하려고 덧붙인 것이다. 프로그래머스에 제출할 때는 solution 함수만 붙여 넣는다.
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
LAB-03과 같은 세 단계다. 단계마다 쓸 템플릿을 붙였을 뿐이다.
1단계를 건너뛰면 2단계에서 "몇 번째가 어느 인덱스인지"가 흔들린다. 문제 정리를 꼭 점검받게 한다.
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
파이썬 리스트 단원을 배우는 중이야. 코딩 테스트 문제를 풀기 전에 문제를 내 말로 정리했어.

## 상황
문제: {문제 원문 붙여 넣기}

내 정리:
- 명령 하나로 할 일: {내가 이해한 내용}
- 반복할 범위: {내가 이해한 내용}
- 돌려줄 값: {내가 이해한 내용}

## 질문
1. 내 정리에서 문제와 다르게 이해한 부분과 빠진 부분을 짚어 줘
2. 그다음 처음부터 끝까지 해야 할 일을 단계 순서로 나눠 줘

## 제약
- 코드나 의사코드 없이 말로만
- 배운 범위(함수 정의 · 조건문 · for · while · 인덱스 · 슬라이싱 · 2차원 리스트 · 구조분해 · sorted · sort · append) 안에서. 리스트 컴프리헨션 · lambda는 쓰지 않는 방법으로

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
문제 원문은 줄이지 않고 그대로 붙인다. 답에 리스트 컴프리헨션 · lambda가 섞이면 <code>## 제약</code>을 가리키며 다시 묻는다
</Callout>

</div>
</Grid>

<!--
LAB-02의 ② 내 설명 점검받기와 ⑤ 단계로 쪼개기를 한 프롬프트로 묶었다(LAB-03과 같다).
학생이 자주 빠뜨리는 정리: "번째"는 1부터 세고 인덱스는 0부터 센다, j번째까지 포함한다, 정렬하는 것은 잘라 낸 부분이지 array 전체가 아니다, 결과는 commands 개수만큼 담긴 리스트다.
기대하는 단계표: ① 결과를 담을 빈 리스트 준비 ② commands에서 명령을 하나씩 꺼냄 ③ 명령을 i, j, k로 나눔 ④ array의 i번째부터 j번째까지 잘라 냄(인덱스 i-1부터 j-1까지) ⑤ 잘라 낸 리스트를 정렬 ⑥ k번째(인덱스 k-1) 수를 결과에 추가 ⑦ 반복이 끝나면 결과를 돌려줌.
AI가 "array를 정렬한 뒤 자른다"로 단계를 바꿔 주면 문제와 다르다. 순서가 바뀌면 답이 달라진다는 것을 학생이 찾게 한다(3단계 증상 참고).
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
def solution(array, commands):
    # 1. {단계표 1번}
    # 2. {단계표 2번}
    #    ...
    # 7. {단계표 마지막 번}
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))               # 내 예측: ?
print(solution([5, 4, 3, 2, 1], [[2, 4, 1]]))  # 내 예측: ?
```

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 주석 아래에 **한 줄씩** 코드를 채운다
- 실행하기 전에 두 print의 결과를 **예측**해 적는다
- 실행해서 예측 · 기대 결과와 맞춰 본다

</div>

<Callout kind="tip" title="명령 하나를 세 변수로 나누려면">
구조분해로 <code>i, j, k = command</code>처럼 한 줄에 나눠 담을 수 있다
</Callout>

</div>
</Grid>

<!--
단계표의 각 줄이 코드 몇 줄이 되는지 직접 옮기는 것이 이 단계의 핵심이다. 주석은 지우지 말고 남겨 두게 한다. 3단계에서 어느 줄이 틀렸는지 찾을 때 쓴다.
예측은 결과 값만 적는다. 첫 줄은 [5, 6, 3]. 둘째 줄은 [5, 4, 3, 2, 1]의 2번째부터 4번째까지 [4, 3, 2]를 정렬한 [2, 3, 4]의 1번째라서 [2]. 자주 빗나가는 예측: 둘째 줄을 [3]으로(인덱스 1부터 자름), [4]로(정렬을 빼먹음).
값이 다르면 for 안에 print(i, j, k, 잘라 낸 리스트)를 넣어 명령마다 무엇을 잘랐는지 본다.
막힌 문법은 ④ 고르는 기준 묻기 정도만 허용하고 "코드로 써 줘"는 묻지 않게 한다.

강사용 정답 코드(학생 자료에는 없음):
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        part = sorted(array[i-1:j])
        answer.append(part[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # [5, 6, 3]
part = array[i-1:j] 다음 줄에 part.sort()를 쓰는 풀이도 맞다(슬라이싱 결과는 새 리스트라 array는 그대로다). for i, j, k in commands:로 바로 나눠 꺼내도 된다.
더 확인할 값(직접 실행): solution([3, 1, 2], [[1, 3, 1], [2, 2, 1], [1, 2, 2]]) → [1, 1, 3], solution([5, 4, 3, 2, 1], [[1, 5, 5], [2, 4, 1]]) → [5, 2]. 실행 뒤 array를 print해서 원본이 그대로인지도 본다.
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
파이썬 리스트 단원을 배우는 중이야.

## 상황
K번째수 solution 함수를 직접 썼는데 결과가 내 예측과 달랐어.
```python
{내가 쓴 코드}
```
내 예측: {예: [5, 6, 3]}
실제 출력: {예: [4, 4, 3] · 에러가 났으면 에러 원문 그대로}

## 질문
내 예측이 어느 지점에서 실제 실행과 갈라졌는지, 왜 그렇게 실행되는지 알려줘.

## 제약
- 코드를 고쳐 쓰지 마. 실행 순서와 이유만 설명해
- 인덱스 · 슬라이싱 · 2차원 리스트 · sorted · sort · append 범위 안에서

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
강사용 증상과 원인(모두 Python 3.13으로 직접 실행해 확인):
IndexError: list index out of range — array[i:j]처럼 인덱스를 1부터 셈. [4, 4, 1]에서 array[4:4]가 빈 리스트가 된다. 또는 part[k]처럼 k에서 1을 빼지 않음. [4, 4, 1]에서 [6][1]을 찾는다.
TypeError: 'NoneType' object is not subscriptable — part = array[i-1:j].sort()처럼 sort()의 결과를 변수에 담음. sort()는 리스트를 제자리에서 바꾸고 None을 돌려준다(마무리 ⑭로 이어짐).
[4, 4, 3] — array.sort()로 원본 전체를 먼저 정렬한 뒤 자름. 첫 명령부터 array가 [1, 2, 3, 4, 5, 6, 7]로 바뀐다. 실행 뒤 array를 print해 보면 원본이 바뀐 것이 보인다.
[3] — answer = []를 for 안에 둠. 명령마다 결과가 새로 비워져 마지막 결과 하나만 남는다.
[5] — return answer를 for 안에 둠. 첫 명령만 처리하고 함수가 끝난다.
-->

---
class: dense
---

## #09. 마무리 — ⑭ 두 방법 비교받기

<Callout icon="💡" title="문제는 풀었는데, 내가 쓴 정렬 방법과 다른 방법의 차이를 정확히 알고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑭번 패턴 (오늘 새 패턴)">

````md
## 맥락
파이썬 리스트 단원을 배우는 중이야. K번째수 문제를 내가 풀었어.

## 상황
내가 쓴 코드:
```python
{내가 쓴 코드}
```
잘라 낸 리스트를 정렬할 때 sorted()와 sort()가 둘 다 있다는 걸 알았어.
내가 아는 차이: {내가 아는 것. 모르면 "모르겠음"}

## 질문
두 방법의 차이를 비교해 주고, 내 코드에서 다른 쪽으로 바꾸면 무엇이 달라지는지 알려줘.

## 제약
- 코드를 고쳐 쓰지 마. 각 차이마다 내가 직접 실행해 확인할 방법을 말로 알려줘
- 리스트 단원 범위(슬라이싱 · 복사 · sorted · sort) 안에서

## 출력 형식
| 비교 항목 | sorted() | sort() | 확인 방법 | 표로
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 학생 활동</h3>

- 보내기 전에 **내가 아는 차이**를 먼저 적는다
- 「확인 방법」 칸을 하나씩 **직접 실행**한다
- 맞으면 ✔, 다르면 실제 결과를 표에 적는다

</div>

<Callout kind="warn" title="주의">
표만 읽고 넘기지 않는다. 확인하지 않은 칸은 아직 내 지식이 아니다
</Callout>

</div>
</Grid>

<!--
새 템플릿 ⑭. LAB-02의 ①~⑫, LAB-03의 ⑬ 뒤로 이어 매긴다.
기대하는 비교: sorted()는 새 리스트를 돌려주고 원본은 그대로, sort()는 원본을 제자리에서 바꾸고 None을 돌려준다. sorted()는 튜플 등에도 쓸 수 있고 sort()는 리스트에만 있다.
K번째수에서는 잘라 낸 부분(새 리스트)을 정렬하므로 둘 다 답이 맞는다. 단, part = array[i-1:j].sort()처럼 쓰면 None이 담기고(3단계 TypeError), array.sort()처럼 원본을 정렬하면 다음 명령의 결과가 틀어진다(3단계 [4, 4, 3]).
확인 방법 예: x = [3, 1, 2]; y = sorted(x); print(x, y) → [3, 1, 2] [1, 2, 3] / z = x.sort(); print(x, z) → [1, 2, 3] None.
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-04] 리스트 7 · ITWILL · {teacher} 강사</p>

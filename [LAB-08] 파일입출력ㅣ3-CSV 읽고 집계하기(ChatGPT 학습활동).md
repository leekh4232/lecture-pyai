---
theme: ./slidev-themes/hossam
manuscript: true
colorMode: dark
fontScale: 1
title: 파이썬 기초 · 파일입출력 — 파일입출력 종합문제
layout: cover
---

# 파일입출력 종합문제

AI에게 코드를 받아 검증하며 푸는 코딩 테스트 — 프로그래머스 「신고 결과 받기」

<p class="sub">[LAB-08] 파일입출력 3 · ITWILL · {teacher} 강사</p>

<!--
「open함수의 사용」「CSV파일 다루기」를 마친 뒤 하는 실습. ② 답 받기 단계(LAB-07 ~ 09)라서 ChatGPT가 코드를 주고, 학생은 받은 코드를 4단 확인(실행 · 범위 · 설명 · 변형)으로 검증한다. 지침은 「ChatGPT 지침(답 받기).md」가 들어가 있다고 전제한다.
LAB-02 ~ 08에서 배운 것을 모두 써야 풀리는 코딩 테스트 문제(프로그래머스 「신고 결과 받기」) 하나를 세 단계로 푼다. 단계마다 프롬프트 하나만 한다: 1단계 프롬프트(② + ⑤), 2단계 프롬프트(오늘 새 템플릿 ⑲ 데이터 정보와 함께 받기) + 4단 확인, 3단계 프롬프트(⑱ 내 코드 고쳐 받기). 마무리는 ⑫ 거꾸로 질문.
원래 문제는 입력을 리스트로 받는다. 오늘은 신고 기록을 CSV 파일로 저장해 두고 파일에서 읽어 오는 부분을 더했다(파일입출력 단원 연결).
-->

---

## #01. 오늘의 흐름

<Timeline>
<li><b>문제 읽기</b>코딩 테스트 문제와 입출력 예, 오늘 더하는 CSV 파일을 본다</li>
<li><b>세 단계로 풀기</b>설계는 AI와 함께, 코드는 AI에게 받아 내가 검증, 틀리면 고쳐 받기</li>
<li class="now"><b>마무리</b>⑫ 거꾸로 질문으로 받은 코드를 이해했는지 점검한다</li>
</Timeline>

<Grid cols="2" align="start">

<Callout kind="real" title="오늘의 규칙">

- 지침은 「ChatGPT 지침(답 받기).md」. 먼저 직접 시도하고, 막힌 코드를 `## 내 시도`에 붙여 받는다
- 프롬프트는 여섯 섹션. 받은 코드는 **4단 확인**(실행 · 범위 · 설명 · 변형)을 통과해야 내 코드
- 첫 질문은 섹션을 갖춘 md로 자세히, 같은 대화의 후속 질문은 평서문으로

</Callout>

<Tile kind="soft" color="ai" tag="오늘 새로 더하는 템플릿" title="⑲ 데이터 정보와 함께 받기">
LAB-07의 ⑰ · ⑱ 뒤로 이어 매긴다. AI는 내 파일을 모른다. 위치 · 인코딩 · 첫 몇 줄을 함께 보낸다
</Tile>

</Grid>

<!--
시작 전에 개인 맞춤 설정의 지침이 「ChatGPT 지침(답 받기).md」인지, 템플릿마다 새 대화를 여는지 말로 확인한다.
⑰ 코드 받기 · ⑱ 내 코드 고쳐 받기는 LAB-07에서 만들었으므로 다시 가르치지 않고 번호로만 부른다.
-->

---

## #02. 쓸 수 있는 문법 — 배운 것까지만

<div class="kicker">받은 코드도 지금까지 배운 문법이어야 한다. 모든 프롬프트의 <code>## 제약</code>에 이 범위를 적는다</div>

| 단원 | 쓸 수 있는 것 |
|:--|:--|
| LAB-02 ~ 04 | 변수 · 연산자 · 함수 정의 · 조건문 · 반복문 · 리스트(인덱스 · 슬라이싱 · 구조분해 · in · not in · len · append · enumerate 등) |
| LAB-05 · 06 | 문자열(strip · split · join · format · isnumeric 등) · 딕셔너리(키 · 값 · get · keys · values · items) |
| LAB-07 예외처리 | try · except · finally |
| LAB-08 파일입출력 | open · close · with · read · readlines · write · 모드(r · w · a) · encoding(utf-8 · euc-kr) · CSV를 split으로 읽기 |

<Callout kind="danger" title="아직 안 배운 것 — 쓰지 않는다">
<code>csv</code> 모듈 · <code>pandas</code> · <code>set</code> · 리스트 · 딕셔너리 컴프리헨션 · lambda · <code>collections</code>(Counter 등)
</Callout>

<!--
범위는 LAB-02 ~ 08 교안 실습코드에서 확인했다. enumerate는 LAB-04 리스트의 탐색(2)와 LAB-08 CSV파일 다루기에, isnumeric은 LAB-05와 LAB-08에 나온다. set은 어느 실습코드에도 없다.
이 문제에서 AI는 중복 신고를 지우려고 set을, CSV를 읽으려고 csv 모듈을 거의 꼭 꺼낸다. 4단 확인의 ② 범위에서 걸러 낸다.
-->

---
layout: section
---

# 문제

LAB-02 ~ LAB-08에서 배운 것을 모두 써야 풀리는 문제 하나

---
class: dense
---

## #03. 문제 — 신고 결과 받기 (1)

<Grid cols="1fr 1fr" align="start">
<div>

신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

- 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
  - 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
  - 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
- k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
  - 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

</div>
<div>

다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.

| 유저 ID | 유저가 신고한 ID | 설명 |
|:--|:--|:--|
| "muzi" | "frodo" | "muzi"가 "frodo"를 신고했습니다. |
| "apeach" | "frodo" | "apeach"가 "frodo"를 신고했습니다. |
| "frodo" | "neo" | "frodo"가 "neo"를 신고했습니다. |
| "muzi" | "neo" | "muzi"가 "neo"를 신고했습니다. |
| "apeach" | "muzi" | "apeach"가 "muzi"를 신고했습니다. |

</div>
</Grid>

<!--
문제 원문은 프로그래머스 그대로다(2022 KAKAO BLIND RECRUITMENT). 원문이 길어 세 쪽으로 나눴다.
핵심 함정은 "동일한 유저에 대한 신고 횟수는 1회로 처리"다. 입출력 예 #1에는 중복 신고가 없어서, 중복을 지우지 않은 코드도 #1은 통과한다. #2에서만 드러난다.
-->

---
class: dense
---

## #04. 문제 — 신고 결과 받기 (2)

<Grid cols="2fr 3fr" align="start">
<div>

각 유저별로 신고당한 횟수는 다음과 같습니다.

| 유저 ID | 신고당한 횟수 |
|:--|:--:|
| "muzi" | 1 |
| "frodo" | 2 |
| "apeach" | 0 |
| "neo" | 2 |

</div>
<div>

위 예시에서는 2번 이상 신고당한 "frodo"와 "neo"의 게시판 이용이 정지됩니다. 이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.

| 유저 ID | 유저가 신고한 ID | 정지된 ID |
|:--|:--|:--|
| "muzi" | ["frodo", "neo"] | ["frodo", "neo"] |
| "frodo" | ["neo"] | ["neo"] |
| "apeach" | ["muzi", "frodo"] | ["frodo"] |
| "neo" | 없음 | 없음 |

</div>
</Grid>

따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 각각 처리 결과 메일을 1회 받게 됩니다.

이용자의 ID가 담긴 문자열 배열 `id_list`, 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 `report`, 정지 기준이 되는 신고 횟수 `k`가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 하도록 solution 함수를 완성해주세요.

<!--
메일은 "정지된 사람"이 아니라 "정지된 사람을 신고한 사람"이 받는다. 이것을 거꾸로 이해하면 결과가 [0, 1, 0, 1]이 된다(3단계 증상 참고).
-->

---
class: dense
---

## #05. 문제 — 제한사항

<Grid cols="1fr 1fr" align="start">
<div>

- 2 ≤ `id_list`의 길이 ≤ 1,000
  - 1 ≤ `id_list`의 원소 길이 ≤ 10
  - `id_list`의 원소는 이용자의 id를 나타내는 문자열이며 알파벳 소문자로만 이루어져 있습니다.
  - `id_list`에는 같은 아이디가 중복해서 들어있지 않습니다.
- 1 ≤ `k` ≤ 200, `k`는 자연수입니다.
- return 하는 배열은 `id_list`에 담긴 id 순서대로 각 유저가 받은 결과 메일 수를 담으면 됩니다.

</div>
<div>

- 1 ≤ `report`의 길이 ≤ 200,000
  - 3 ≤ `report`의 원소 길이 ≤ 21
  - `report`의 원소는 "이용자id 신고한id"형태의 문자열입니다.
  - 예를 들어 "muzi frodo"의 경우 "muzi"가 "frodo"를 신고했다는 의미입니다.
  - id는 알파벳 소문자로만 이루어져 있습니다.
  - 이용자id와 신고한id는 공백(스페이스)하나로 구분되어 있습니다.
  - 자기 자신을 신고하는 경우는 없습니다.

</div>
</Grid>

<!--
제한사항은 원문 그대로다. 두 단으로 나누면서 k와 return 항목을 왼쪽 단(id_list 아래)으로 옮겼다. 원문 순서는 id_list → report → k → return이다.
제한시간 안내(정확성 테스트 10초)는 노트북 실습과 상관없어 뺐다.
-->

---
class: dense
---

## #06. 문제 — 입출력 예

| id_list | report | k | result |
|:--|:--|:--:|:--|
| `["muzi", "frodo", "apeach", "neo"]` | `["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]` | 2 | <span class="whitespace-nowrap">[2,1,1,0]</span> |
| `["con", "ryan"]` | `["ryan con", "ryan con", "ryan con", "ryan con"]` | 3 | [0,0] |

<div class="kicker">입출력 예 설명</div>

<Steps>
<li><b>입출력 예 #1</b> 문제의 예시와 같습니다.</li>
<li><b>입출력 예 #2</b> "ryan"이 "con"을 4번 신고했으나, 주어진 조건에 따라 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리합니다. 따라서 "con"은 1회 신고당했습니다. 3번 이상 신고당한 이용자는 없으며, "con"과 "ryan"은 결과 메일을 받지 않습니다. 따라서 [0, 0]을 return 합니다.</li>
</Steps>

<p class="small muted">출처: <a href="https://school.programmers.co.kr/learn/courses/30/lessons/92334" target="_blank" rel="noopener">프로그래머스 코딩테스트 연습 「신고 결과 받기」</a></p>

<!--
입출력 예와 설명은 원문 그대로다.
#2가 이 문제의 함정을 보여 주는 예다. 중복을 지우지 않은 코드는 #1을 통과하고 #2에서만 [0, 4]가 나온다.
-->

---
class: dense
---

## #07. 오늘 더하는 것 — 신고 기록을 CSV 파일에서 읽는다

<Callout icon="💡" title="원래 문제는 report를 리스트로 받는다. 오늘은 신고 기록을 CSV 파일로 두고, 파일에서 읽어 report 리스트를 만든 뒤 solution을 부른다" color="pastel-1"></Callout>

<Grid cols="2fr 2fr 3fr" align="start">
<div>

<div class="kicker">report.csv · 입출력 예 #1</div>

```text
신고자,신고당한사람
muzi,frodo
apeach,frodo
frodo,neo
muzi,neo
apeach,muzi
```

</div>
<div>

<div class="kicker">report2.csv · 입출력 예 #2</div>

```text
신고자,신고당한사람
ryan,con
ryan,con
ryan,con
ryan,con
```

</div>
<div>

<div class="kicker">기본 코드 템플릿</div>

```python
def solution(id_list, report, k):
    answer = []
    return answer
```

<Steps>
<li>VS Code에서 노트북과 <b>같은 폴더</b>에 두 파일을 새로 만들어 그대로 붙인다</li>
<li>VS Code가 저장하는 인코딩은 <b>utf-8</b></li>
</Steps>

</div>
</Grid>

<!--
파일에서 읽는 부분은 프로그래머스 문제에 없는, 오늘 수업에서 더한 것이다. 프로그래머스에 제출할 때는 solution 함수만 붙여 넣는다.
CSV 한 줄 "muzi,frodo"를 split(",")한 뒤 원래 문제의 모양 "muzi frodo"로 이어 붙여 report 리스트를 만든다. 그러면 solution은 원래 문제 그대로 쓸 수 있다.
교안의 covid19.csv는 엑셀에서 만든 euc-kr 파일이지만, 오늘 파일은 VS Code에서 만들어 utf-8이다. 헤더에 한글이 있어서 인코딩을 잘못 적으면 첫 줄부터 에러가 난다(3단계 증상).
파일 끝에 빈 줄을 하나 더 넣지 않게 한다. 빈 줄이 있으면 split 결과가 ['']가 되어 IndexError가 난다(3단계 증상).
-->

---
layout: section
---

# 풀이 단계

설계 → 코드 받기 · 검증 → 고쳐 받기, 세 단계로 푼다

---

## #08. AI와 함께 푸는 세 단계

<Steps color="pastel">
<li><b>AI에게 물어 문제를 확인하고 함수를 설계한다</b> — 내 정리를 점검받고, 처리 순서를 단계표로 받는다 <Chip color="ai">프롬프트 ② + ⑤</Chip></li>
<li><b>먼저 직접 시도하고, 막히면 코드를 받아 검증한다</b> — 내 파일 정보와 내 시도를 보내 코드를 받고, 4단 확인을 한다 <Chip color="ai">프롬프트 ⑲</Chip> <Chip color="ok">4단 확인</Chip></li>
<li><b>틀리면 AI에게 고쳐 받는다</b> — 틀린 결과와 내가 생각한 원인을 보내 바꾼 줄만 받는다 <Chip color="ai">프롬프트 ⑱</Chip></li>
</Steps>

<Core color="ai">코드는 AI에게 받아도 된다. 4단 확인을 통과해야 내 코드다.</Core>

<!--
LAB-03 ~ 06과 같은 세 단계에서 2단계만 바뀌었다. 조언 받기 단계에서는 2단계를 AI 없이 썼고, 답 받기 단계에서는 직접 시도한 뒤 코드를 받아 검증한다.
1단계를 건너뛰면 받은 코드가 맞는지 판단할 기준이 없다. 특히 "중복 신고는 1회"와 "메일은 신고한 사람이 받는다"를 1단계에서 확인해 둔다.
-->

---
class: dense
---

## #09. 1단계 — AI에게 물어 문제를 확인하고 함수를 설계한다

<Callout icon="💡" title="문제를 제대로 이해했는지 확인하고, 어떤 순서로 코드를 쓸지 정하고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ② + ⑤번 패턴">

````md
## 맥락
파이썬 파일입출력 단원을 배우는 중이야. 코딩 테스트 문제를 풀기 전에 문제를 내 말로 정리했어.

## 상황
문제: {문제 원문 붙여 넣기}
신고 기록은 report.csv 파일(헤더 한 줄 + "신고자,신고당한사람" 행)에서 읽어 올 거야.

내 정리:
- 세어야 할 것: {내가 이해한 내용}
- 정지되는 조건: {내가 이해한 내용}
- 돌려줄 값: {내가 이해한 내용}

## 질문
1. 내 정리에서 문제와 다르게 이해한 부분과 빠진 부분을 짚어 줘
2. 그다음 파일 읽기부터 결과를 돌려주기까지 해야 할 일을 단계 순서로 나눠 줘

## 제약
- 코드나 의사코드 없이 말로만
- 배운 범위(#02 표) 안에서. csv 모듈 · set · 컴프리헨션은 쓰지 않는 방법으로

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
1단계는 코드를 받는 단계가 아니다. <code>## 내 시도</code>를 넣지 않고 말로만 받는다
</Callout>

</div>
</Grid>

<!--
LAB-02의 ② 내 설명 점검받기와 ⑤ 단계로 쪼개기를 한 프롬프트로 묶었다(LAB-03 ~ 06과 같다). 답 받기 지침이 들어가 있어도 ## 내 시도가 없고 "말로만"이라고 적으면 코드가 오지 않는다.
학생이 자주 빠뜨리는 정리: 같은 사람이 같은 사람을 여러 번 신고하면 1회, 메일은 정지된 사람이 아니라 그 사람을 신고한 사람이 받는다, 결과는 id_list 순서, 정지는 k번 "이상"(같아도 정지).
기대하는 단계표: ① 파일을 열어 줄 목록으로 읽기 ② 헤더를 건너뛰고 줄마다 줄바꿈을 지우고 쉼표로 나눠 report 리스트 만들기 ③ 사람마다 "나를 신고한 사람 목록"을 빈 리스트로 준비 ④ 신고마다 신고자가 목록에 없을 때만 추가(중복 제거) ⑤ 목록 길이가 k 이상인 사람을 신고한 사람마다 메일 수 1 증가 ⑥ id_list 순서대로 메일 수를 담아 돌려주기.
-->

---
class: dense
---

## #10. 2단계 — 먼저 직접 시도하고, 막히면 코드를 받아 검증한다

<Callout icon="💡" title="단계표대로 직접 써 보다 막혔고, 내 파일에 맞는 코드를 받아 검증하고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑲번 패턴 (오늘 새 패턴)">

````md
## 맥락
파이썬 파일입출력 단원을 배우는 중이야. VS Code 주피터 노트북에서 실행해.

## 상황
- 노트북과 같은 폴더에 report.csv · report2.csv가 있어. 인코딩은 utf-8
- report.csv 첫 3줄:
  신고자,신고당한사람
  muzi,frodo
  apeach,frodo
- 문제: {문제 원문 붙여 넣기}
- 정답: report.csv는 [2, 1, 1, 0], report2.csv는 [0, 0]
  (id_list와 k는 문제의 입출력 예 #1 · #2 그대로)

## 내 시도
{내 코드와 막힌 지점}

## 질문
내 시도를 이어서 완성한 코드를 줘.

## 제약
- 배운 범위(#02 표)만 써. csv 모듈 · pandas · set · 컴프리헨션은 쓰지 마
- 파일 이름 · 열 이름 · 변수 이름은 위에 적은 그대로 써

## 출력 형식
1. 코드
2. | 줄 | 하는 일 | 표로
3. 정답과 맞는지 내가 확인할 방법 2줄
````

</Prompt>

</div>
<div>

<div class="card ok">
<h3><carbon:list-checked /> 받은 코드 4단 확인</h3>

- **① 실행** 두 파일 모두 정답이 나오는지
- **② 범위** csv · set · 컴프리헨션이 없는지
- **③ 설명** 줄별 표 없이 줄마다 말로
- **④ 변형** 아래 문제를 AI 없이

</div>

<Callout kind="tip" title="④ 변형 문제">
메일 수 대신 <b>신고당한 횟수</b>(중복은 1회)를 id_list 순서로. report.csv면 <span class="whitespace-nowrap"><b>[1, 2, 0, 2]</b></span>
</Callout>

</div>
</Grid>

<!--
새 템플릿 ⑲. ⑰ 코드 받기와 다른 점은 ## 상황에 "내 데이터의 정보"가 들어간다는 것이다: 위치(같은 폴더) · 인코딩(utf-8) · 첫 3줄(열 이름) · 정답. 3단계 증상 중 UnicodeDecodeError · FileNotFoundError · 헤더를 데이터로 센 KeyError가 이 정보가 빠졌을 때 생긴다.
## 내 시도가 비어 있으면 지침 2-1에 따라 코드 대신 처리 순서가 온다. 1단계 단계표대로 파일 읽기까지라도 직접 써서 넣게 한다.
① 실행은 report.csv 하나로 끝내지 않는다. 중복 신고를 지우지 않은 코드도 report.csv는 [2, 1, 1, 0]으로 통과하고, report2.csv에서만 [0, 4]가 나온다.
④ 변형 정답(직접 실행): report.csv → [1, 2, 0, 2], report2.csv → [1, 0]. 받은 코드를 이해했다면 "나를 신고한 사람 목록"의 길이만 꺼내면 된다.

강사용 정답 코드(학생 자료에는 없음):
def solution(id_list, report, k):
    reporters = {}                 # 신고당한 사람: 나를 신고한 사람 목록
    for name in id_list:
        reporters[name] = []
    for r in report:
        user, target = r.split(" ")
        if user not in reporters[target]:
            reporters[target].append(user)
    mail = {}
    for name in id_list:
        mail[name] = 0
    for target in reporters:
        if len(reporters[target]) >= k:
            for user in reporters[target]:
                mail[user] += 1
    answer = []
    for name in id_list:
        answer.append(mail[name])
    return answer

report = []
with open("report.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if i == 0:
        continue
    cols = line.strip().split(",")
    report.append(cols[0] + " " + cols[1])

print(solution(["muzi", "frodo", "apeach", "neo"], report, 2))   # [2, 1, 1, 0]
report2.csv로 같은 순서를 밟고 solution(["con", "ryan"], report2, 3)이면 [0, 0]. 더 확인할 값: report.csv에 k = 1이면 [2, 1, 2, 0].
-->

---
class: dense
---

## #11. 3단계 — 틀리면 AI에게 고쳐 받는다

<Callout icon="💡" title="받은 코드나 내가 고친 코드에서 에러가 나거나 값이 틀렸고, 원인을 짐작해 봤는데 어떻게 고칠지 막힌 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑱번 패턴">

````md
## 맥락
파이썬 파일입출력 단원을 배우는 중이야.

## 상황
```python
{내 코드}
```
기대 결과: {예: report2.csv로 [0, 0]}
실제 출력: {예: [0, 4] · 에러가 났으면 에러 원문 그대로}

## 내 시도
내가 생각한 원인: {내 생각}

## 질문
내 코드를 고친 코드를 줘.

## 제약
- 내 코드에서 바꾼 줄만 바꿔. 나머지는 그대로 둬
- 배운 범위(#02 표)만 써. csv 모듈 · set · 컴프리헨션은 쓰지 마

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

- 실제 출력은 **그대로** 붙인다
- 원인을 **먼저 내 말로** 적고 보낸다
- `# 변경` 줄만 비교하고, 두 파일로 다시 ① 실행

</div>

<Callout kind="danger" title="에러가 파일 쪽이면">
코드만 보지 말고 파일 이름 · 위치 · 인코딩 · 마지막 빈 줄을 먼저 확인한다
</Callout>

</div>
</Grid>

<!--
LAB-07에서 만든 ⑱을 그대로 쓴다. 고친 뒤에는 두 파일로 ① 실행부터 4단 확인을 다시 한다.
강사용 증상과 원인(모두 Python 3.13으로 직접 실행해 확인):
report2.csv가 [0, 4] — 중복 신고를 지우지 않고 신고 줄마다 셌다. con이 4번 신고당해 정지되고, ryan이 신고한 줄 수만큼 4통을 받는다. report.csv는 [2, 1, 1, 0]으로 통과해서 놓치기 쉽다.
KeyError: '신고당한사람' — 헤더 줄을 건너뛰지 않아 "신고자 신고당한사람"이 신고 기록으로 들어갔다.
KeyError: 'frodo\n' — 줄 끝의 줄바꿈을 strip으로 지우지 않았다. 읽은 report가 ['muzi frodo\n', ...]가 된다.
UnicodeDecodeError: 'euc_kr' codec can't decode byte 0xec in position 0: illegal multibyte sequence — 교안 covid19.csv처럼 euc-kr로 열었다. 오늘 파일은 utf-8.
FileNotFoundError: [Errno 2] No such file or directory: 'data/report.csv' — AI가 폴더 구조를 지어냈다. ⑲의 "노트북과 같은 폴더"가 막아 준다.
IndexError: list index out of range — 파일 끝에 빈 줄이 하나 더 있어 split 결과가 ['']이다.
[0, 0, 0, 0] — 정지 조건을 > k로 썼다. k번 "이상"이므로 >= k.
[0, 1, 0, 1] — 메일을 신고한 사람이 아니라 정지된 사람에게 셌다.
-->

---
class: dense
---

## #12. 마무리 — ⑫ 거꾸로 질문

<Callout icon="💡" title="정답은 나왔는데, 받은 코드를 정말 이해했는지 점검하고 싶은 경우" color="pastel-1"></Callout>

<Grid cols="2fr 1fr" align="start">
<div>

<Prompt class="small" cols="2" title="프롬프트 실습 - ⑫번 패턴">

````md
## 맥락
파이썬 파일입출력 단원을 배우는 중이야. 신고 결과 받기 문제를 AI에게 받은 코드로 풀었어.

## 상황
4단 확인을 통과한 코드:
```python
{내 코드}
```

## 질문
이 코드를 내가 이해했는지 점검하는 문제를 한 번에 하나씩 내 줘.
내가 답하면 맞았는지 알려 주고 다음 문제로 넘어가.
다섯 문제가 끝나면 내가 약한 부분을 정리해 줘.

## 제약
- 문제는 이 코드의 실행 결과를 예측하거나 줄의 역할을 설명하는 것으로. 코드를 작성하라는 문제는 내지 마
- 배운 범위(#02 표) 안에서

## 출력 형식
문제는 아래 예시와 같은 모양으로, 한 번에 하나만.
- 예시: report.csv에서 strip()을 빼면 어느 줄에서 무슨 일이 생길까?
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
틀린 문제는 AI 설명만 읽고 넘기지 않는다. 그 줄에 print를 넣어 내 눈으로 확인한다
</Callout>

</div>
</Grid>

<!--
LAB-02의 ⑫를 받은 코드에 맞춰 쓴다. 답 받기 단계에서 ⑫는 4단 확인의 ③ 설명을 한 번 더 다지는 역할이다. 받은 코드를 읽기만 하고 넘어간 학생은 여기서 드러난다.
예시 문제의 답: strip()을 빼면 report가 ['muzi frodo\n', ...]가 되어 solution 안에서 KeyError: 'frodo\n'가 난다(3단계 증상).
-->

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-08] 파일입출력 3 · ITWILL · {teacher} 강사</p>

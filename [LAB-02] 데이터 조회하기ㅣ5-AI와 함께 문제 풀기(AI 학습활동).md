---
theme: ./theme
manuscript: true
colorMode: dark
fontScale: 1
title: 데이터베이스 · AI와 함께 문제 풀기
layout: cover
---

# AI와 함께 문제 풀기

코딩 테스트 문제의 풀이 과정을 AI의 도움으로 찾아가기

<p class="sub">[LAB-02] 데이터 조회하기 (5) / ITWILL - 주영아·이광호 강사</p>

---
layout: section
---

# 학습활동 진행 방법

AI에게 도움을 받는 법과 상황별 템플릿

---

## #01. AI와 함께 문제를 해결하는 법

<Core color="py">AI에게 받는 것은 정답이 아니라 <span class="hl py">정답까지 가는 길의 도움</span>이다.</Core>

<Grid cols="2" align="start">
<div class="card py">
<h3>내가 하는 일</h3>

- 문제를 읽고 **내 말로** 정리한다
- 쿼리를 **직접 쓰고** 실행한다
- 결과가 맞는지 **직접 확인**한다

</div>
<div class="card ok">
<h3>AI에게 받는 도움</h3>

- **방향** — 어떤 절을 어떤 순서로 쓸지
- **해석** — 실행 결과가 무엇을 뜻하는지
- **진단** — 결과가 다를 때 어디를 볼지

</div>
</Grid>

<Grid cols="2" gap="12">
<Tile kind="fill" color="danger" tag="✗ 묻지 않는 것" title="“이 문제 쿼리 짜 줘”"></Tile>
<Tile kind="soft" color="ok" tag="○ 대신 이렇게" title="“내가 이해한 게 맞는지 봐 줘”"></Tile>
</Grid>

<Callout kind="real" title="쿼리를 달라고 해도 주지 않는다">
1단원에서 설정한 <b>ChatGPT 지침</b>(하네스)이 쿼리 출력을 막고 있다. 절의 역할과 순서, 틀린 곳의 위치와 이유만 말로 알려 준다.
</Callout>

---

## #02. 학습활동 진행 방법

문제 하나를 아래 다섯 단계로 푼다. **직접 풀 수 있는 문제는 AI에게 묻지 않는다.** AI는 막힐 때만 쓴다.

<Flow color="pastel">
<li><carbon:document /><b>① 문제 읽기</b><span>내 말로 정리 · AI 없이</span></li>
<li><carbon:edit /><b>② 직접 풀기</b><span>풀 수 있으면 AI 없이 끝까지</span></li>
<li><carbon:bot /><b>③ 방향 묻기</b><span>막힐 때만 절과 순서를 받는다</span></li>
<li><carbon:checkmark-outline /><b>④ 힌트 확인</b><span>받은 힌트를 직접 실행해 확인</span></li>
<li><carbon:bot /><b>⑤ 원인 묻기</b><span>정답과 다르면 묻고 내가 고친다</span></li>
</Flow>

<Grid cols="3" gap="12">
<Tile kind="soft" color="py" tag="프롬프트" title="템플릿의 { }만 바꾼다">상황별 템플릿 두 개에서 <code>{ }</code> 부분만 문제에 맞게 바꿔 쓴다</Tile>
<Tile kind="soft" color="ok" tag="컨텍스트" title="있는 그대로 보여 준다">테이블 구조 · 내가 쓴 쿼리 · 실행 결과는 내 말로 바꾸지 않고 붙인다</Tile>
<Tile kind="soft" color="ai" tag="실행" title="수업용 DB에서 확인한다">쿼리는 <code>myschool</code>에서 실행하고, 결과를 슬라이드의 정답 결과와 비교한다</Tile>
</Grid>

---

## #03. 상황별 템플릿

프롬프트는 문제마다 새로 쓰지 않는다. 아래 템플릿에서 <code>{ }</code>로 묶인 곳만 문제에 맞게 바꿔 쓴다.

<Grid cols="2" gap="12">
<Tile kind="soft" color="py" tag="막혔을 때 · 진행 ③" title="방향 묻기 템플릿">내 이해가 맞는지 점검받고, 필요한 절과 순서를 받는다</Tile>
<Tile kind="soft" color="ok" tag="실행한 뒤에 · 진행 ⑤" title="원인 묻기 템플릿">에러가 나거나 정답 결과와 다를 때, 확인할 곳을 받는다</Tile>
</Grid>

<Steps>
<li>템플릿을 복사해 <code>.md</code> 파일로 저장해 둔다</li>
<li><code>{ }</code>로 묶인 곳을 <b>중괄호까지 지우고</b> 내 내용으로 바꾼다</li>
<li><code>##</code> 제목과 나머지 문장은 그대로 둔다</li>
</Steps>

<Callout kind="tip" title="한 번에 맞았다면">
같은 대화에서 쿼리를 한 절씩 <b>내 말로 설명</b>해 보내고, 설명이 맞는지 점검받는다.
</Callout>

---
class: dense
---

### #03-1. 방향 묻기 템플릿 — 풀기 전에 내 이해를 점검받을 때

<Grid cols="2" align="start">
<div>

<Prompt>

````md
## 맥락
SQL {배우는 단원}을 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
{테이블 이름} 테이블
- 주요 컬럼: {문제에 쓰이는 컬럼과 뜻}
- 내가 이해한 문제: {내 말로 정리한 내용}

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- {지금까지 배운 절 · 연산자} 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

</Prompt>

</div>
<div>

| 바꿀 곳 | 넣을 내용 |
|:--|:--|
| `{배우는 단원}` | 지금 배우는 단원. 예: 데이터 조회 |
| `{테이블 이름}` | 문제에 나온 테이블 이름 |
| `{문제에 쓰이는 컬럼과 뜻}` | 조건 · 정렬에 쓰는 컬럼 |
| `{내 말로 정리한 내용}` | 무엇을 · 어떤 행만 · 어떤 순서로 |
| `{지금까지 배운 절 · 연산자}` | 예: SELECT · WHERE · ORDER BY |

<Callout kind="warn" title="받은 답 확인">
답에 쿼리가 없어야 정상이다. 절의 순서표만 받고, 내 이해와 다른 곳이 있으면 문제를 다시 읽는다.
</Callout>

</div>
</Grid>

---
class: dense
---

### #03-2. 원인 묻기 템플릿 — 실행 결과가 정답과 다를 때

<Grid cols="2" align="start">
<div>

<Prompt>

````md
## 맥락
SQL {배우는 단원}을 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
{하려던 일을 한 문장으로}
```sql
{내가 쓴 쿼리}
```
- 기대한 결과: {정답 결과}
- 실제 결과: {에러 원문 또는 결과의 앞 몇 줄}

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

</Prompt>

</div>
<div>

| 바꿀 곳 | 넣을 내용 |
|:--|:--|
| `{하려던 일을 한 문장으로}` | 문제를 내 말로 줄인 한 문장 |
| `{내가 쓴 쿼리}` | 실행한 쿼리 그대로 |
| `{정답 결과}` | 슬라이드의 정답 결과 표 |
| `{에러 원문 또는 결과의 앞 몇 줄}` | 내 말로 바꾸지 않고 복사 |

<div class="card ok">
<h3>받은 답으로 할 일</h3>

- AI는 고친 쿼리를 주지 않는다. **위치와 이유**만 알려 준다
- 알려 준 곳을 보고 **내가 고쳐서** 다시 실행한다

</div>

</div>
</Grid>

---

## #04. 문제 1 — 특정 옵션이 포함된 자동차 리스트 구하기

<p><Chip color="py">Level 1</Chip> <Chip kind="outline" color="py">프로그래머스 157343</Chip> https://school.programmers.co.kr/learn/courses/30/lessons/157343</p>

<Grid cols="2" align="start">
<div>

다음은 어느 자동차 대여 회사에서 대여중인 자동차들의 정보를 담은 `CAR_RENTAL_COMPANY_CAR` 테이블입니다. `CAR_ID`, `CAR_TYPE`, `DAILY_FEE`, `OPTIONS` 는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트를 나타냅니다.

- 자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 이 있습니다
- 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트입니다
- 키워드 종류는 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 가 있습니다

</div>
<div>

| Column name | Type | Nullable |
|:--|:--|:--|
| CAR_ID | INTEGER | FALSE |
| CAR_TYPE | VARCHAR(255) | FALSE |
| DAILY_FEE | INTEGER | FALSE |
| OPTIONS | VARCHAR(255) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제">
<code>CAR_RENTAL_COMPANY_CAR</code> 테이블에서 '네비게이션' 옵션이 포함된 자동차 리스트를 출력하는 SQL문을 작성해주세요. 결과는 자동차 ID를 기준으로 내림차순 정렬해주세요.
</Callout>

---

### #04-1. 입출력 예시

예를 들어 `CAR_RENTAL_COMPANY_CAR` 테이블이 다음과 같다면

| CAR_ID | CAR_TYPE | DAILY_FEE | OPTIONS |
|:--|:--|:--|:--|
| 1 | 세단 | 16000 | 가죽시트,열선시트,후방카메라 |
| 2 | SUV | 14000 | 스마트키,네비게이션,열선시트 |
| 3 | SUV | 22000 | 주차감지센서,후방카메라,네비게이션 |

'네비게이션' 옵션이 포함된 자동차는 자동차 ID가 2, 3인 자동차이고, 자동차 ID를 기준으로 내림차순 정렬하면 다음과 같은 결과가 나와야 합니다.

| CAR_ID | CAR_TYPE | DAILY_FEE | OPTIONS |
|:--|:--|:--|:--|
| 3 | SUV | 22000 | 주차감지센서,후방카메라,네비게이션 |
| 2 | SUV | 14000 | 스마트키,네비게이션,열선시트 |

---
class: dense
---

### #04-2. 방향 묻기 프롬프트 작성 — 템플릿을 문제 1에 맞게 채우기

<Grid cols="2" align="start">
<div>

<Prompt title="방향 묻기 템플릿을 채운 프롬프트">

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
CAR_RENTAL_COMPANY_CAR 테이블
- 주요 컬럼: OPTIONS(콤마로 이어진 옵션 목록), CAR_ID
- 내가 이해한 문제: 옵션에 네비게이션이 있는 자동차를
  ID가 큰 순서로 전부 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

</Prompt>

</div>
<div>

| 바꿀 곳 | 넣은 내용 |
|:--|:--|
| `{배우는 단원}` | 데이터 조회 |
| `{테이블 이름}` | CAR_RENTAL_COMPANY_CAR |
| `{문제에 쓰이는 컬럼과 뜻}` | OPTIONS · CAR_ID |
| `{내 말로 정리한 내용}` | 무엇을 · 어떤 행만 · 어떤 순서로 |
| `{지금까지 배운 절 · 연산자}` | SELECT · WHERE · ORDER BY |

<Callout kind="tip" title="문제 문장을 그대로 붙이지 않았다">
내 말로 줄여 적어야 AI가 <b>내 이해</b>를 점검할 수 있다. 문제를 통째로 붙이면 AI는 문제만 풀이한다.
</Callout>

</div>
</Grid>

---

### #04-3. 방향 묻기 AI 답변 예시

<Callout kind="warn" title="이 쪽은 예시다">
설명을 위해 만든 답변이다. 같은 프롬프트를 보내도 AI의 답은 <b>매번 달라진다</b>. 문장과 표의 모양이 이와 달라도 정상이다.
</Callout>

<Callout kind="ai" title="AI 답변 예시" class="small">

이해한 내용은 맞음. 필요한 절은 네 개이고 아래 순서로 씀.

| 순서 | 절 | 하는 일 |
|:--:|:--|:--|
| 1 | SELECT | 보여 줄 컬럼을 정함. 문제는 자동차의 모든 정보를 요구함 |
| 2 | FROM | 대상 테이블을 정함 |
| 3 | WHERE | 옵션에 네비게이션이 **있는 행만** 남김 |
| 4 | ORDER BY | 자동차 ID를 기준으로 **큰 값부터** 정렬함 |

**내가 확인할 점**

- `OPTIONS` 값이 실제로 어떤 모양으로 저장돼 있는지 몇 행 조회해 보기
- 정렬 방향이 문제의 요구와 같은지 결과의 첫 행으로 확인하기

</Callout>

---
class: dense
---

### #04-4. 직접 풀고 결과 확인하기

<Grid cols="2" align="start">
<div>

<div class="kicker">순서표를 주석으로 옮기고, 주석 아래에 절을 쓴다</div>

```sql
-- 1. 자동차의 모든 정보를 보여 준다
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
-- 2. 대상 테이블
FROM CAR_RENTAL_COMPANY_CAR
-- 3. 네비게이션이 있는 행만 남긴다
WHERE OPTIONS = '네비게이션'
-- 4. 자동차 ID가 큰 값부터
ORDER BY CAR_ID DESC;
```

</div>
<div>

<div class="kicker">실행 전 예측</div>

네비게이션이 있는 자동차가 여러 대 나오고, 맨 위는 ID가 가장 큰 자동차일 것이다.

<div class="kicker ai">내 실행 결과 — 1행</div>

| CAR_ID | CAR_TYPE | DAILY_FEE | OPTIONS |
|:--|:--|:--|:--|
| 13 | 승합차 | 144000 | 네비게이션 |

</div>
</Grid>

<div class="kicker ok">정답 결과 — 3행. 내 결과는 1행이라 틀렸다</div>

| CAR_ID | CAR_TYPE | DAILY_FEE | OPTIONS |
|:--|:--|:--|:--|
| 28 | 리무진 | 298000 | 주차감지센서,스마트키,네비게이션,열선시트,후방카메라,가죽시트 |
| 23 | 세단 | 50000 | 스마트키,네비게이션,열선시트 |
| 13 | 승합차 | 144000 | 네비게이션 |

---
class: dense
---

### #04-5. 원인 묻기 프롬프트 작성 — 틀린 결과로 템플릿 채우기

<Prompt title="원인 묻기 템플릿을 채운 프롬프트" cols="2">

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
옵션에 네비게이션이 있는 자동차를 ID가 큰 순서로 조회하려고 해.
```sql
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS = '네비게이션'
ORDER BY CAR_ID DESC;
```
- 기대한 결과: 3행 (CAR_ID 28, 23, 13)
- 실제 결과: 1행 (CAR_ID 13, OPTIONS는 '네비게이션')

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

</Prompt>

<Callout kind="tip" title="고쳐 달라고 하지 않았다">
"어디가 틀렸는지"가 아니라 <b>확인할 곳</b>을 물었다. 쿼리 · 기대한 결과 · 실제 결과를 그대로 보여 주면 AI가 짐작하지 않는다.
</Callout>

---

### #04-6. 원인 묻기 AI 답변 예시

<Callout kind="warn" title="이 쪽은 예시다">
설명을 위해 만든 답변이다. 같은 프롬프트를 보내도 AI의 답은 <b>매번 달라진다</b>. 문장과 표의 모양이 이와 달라도 정상이다.
</Callout>

<Callout kind="ai" title="AI 답변 예시" class="small">

원인은 WHERE 절의 비교 방식일 가능성이 높음.

| 확인할 곳 | 이유 |
|:--|:--|
| WHERE 절의 비교 연산자 | `=`는 값 **전체**가 같을 때만 참임. 옵션이 여러 개 이어진 행은 전체가 '네비게이션'과 같지 않아 빠짐 |
| `OPTIONS`에 저장된 값 | 추론: 결과로 나온 1행은 옵션이 하나뿐인 행임. 나머지 행은 여러 옵션이 콤마로 이어져 있을 것임. 확인 필요 |

**내가 확인할 점**

- `OPTIONS`를 조건 없이 몇 행 조회해서 값의 모양 보기
- 값의 **일부**가 들어 있는지 찾는 검색 연산자를 복습하고, 쿼리는 직접 고치기

</Callout>

<Core color="ok">알려 준 곳을 보고 <span class="hl ok">내가 고쳐서</span> 다시 실행한다. 정답 결과와 같아지면 끝.</Core>

---
layout: section
---

# SQL 코딩 테스트

이제부터는 프롬프트를 직접 작성하여 문제를 풀어보세요

---

## #05. 문제 2 — 모든 레코드 조회하기

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59034">

동물 보호소에 들어온 모든 동물의 정보를 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요.

</Callout>

---

### #05-1. 입출력 예시

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A349996 | Cat | 2018-01-22 14:32:00 | Normal | Sugar | Neutered Male |
| A350276 | Cat | 2017-08-13 13:50:00 | Normal | Jewel | Spayed Female |
| A350375 | Cat | 2017-03-06 15:01:00 | Normal | Meo | Neutered Male |
| A352555 | Dog | 2014-08-08 04:20:00 | Normal | Harley | Spayed Female |

..이하 생략

---

## #06. 문제 3 — 동물의 아이디와 이름

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59403">

동물 보호소에 들어온 모든 동물의 아이디와 이름을 ANIMAL_ID순으로 조회하는 SQL문을 작성해주세요.

</Callout>

---

### #06-1. 입출력 예시

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| ANIMAL_ID | NAME |
| --- | --- |
| A349996 | Sugar |
| A350276 | Jewel |
| A350375 | Meo |
| A352555 | Harley |
| A352713 | Gia |
| A352872 | Peanutbutter |
| A353259 | Bj |

((이하 생략))

---

## #07. 문제 4 — 역순 정렬하기

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59035">

동물 보호소에 들어온 모든 동물의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 ANIMAL_ID 역순으로 보여주세요. SQL을 실행하면 다음과 같이 출력되어야 합니다.

</Callout>

---

### #07-1. 입출력 예시

| NAME | DATETIME |
| --- | --- |
| Rocky | 2016-06-07 09:17:00 |
| Shelly | 2015-01-29 15:01:00 |
| Benji | 2016-04-19 13:28:00 |
| Jackie | 2016-01-03 16:25:00 |
| *Sam | 2016-03-13 11:17:00 |

..이하 생략

---

## #08. 문제 5 — 여러 기준으로 정렬하기

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59404">

동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문을 작성해주세요. 단, 이름이 같은 동물 중에서는 보호를 나중에 시작한 동물을 먼저 보여줘야 합니다.

</Callout>

---

### #08-1. 입출력 예시 (1)

예를 들어, `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A349996 | Cat | 2018-01-22 14:32:00 | Normal | Sugar | Neutered Male |
| A350276 | Cat | 2017-08-13 13:50:00 | Normal | Jewel | Spayed Female |
| A396810 | Dog | 2016-08-22 16:13:00 | Injured | Raven | Spayed Female |
| A410668 | Cat | 2015-11-19 13:41:00 | Normal | Raven | Spayed Female |

1. 이름을 사전 순으로 정렬하면 다음과 같으며, 'Jewel', 'Raven', 'Sugar'
2. 'Raven'이라는 이름을 가진 개와 고양이가 있으므로, 이 중에서는 보호를 나중에 시작한 개를 먼저 조회합니다.

---

### #08-2. 입출력 예시 (2)

따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME | DATETIME |
| --- | --- | --- |
| A350276 | Jewel | 2017-08-13 13:50:00 |
| A396810 | Raven | 2016-08-22 16:13:00 |
| A410668 | Raven | 2015-11-19 13:41:00 |
| A349996 | Sugar | 2018-01-22 14:32:00 |

---

## #09. 문제 6 — 인기있는 아이스크림

<Grid cols="2" align="start">
<div>

`FIRST_HALF` 테이블은 아이스크림 가게의 상반기 주문 정보를 담은 테이블입니다.`FIRST_HALF` 테이블 구조는 다음과 같으며, `SHIPMENT_ID`, `FLAVOR`, `TOTAL_ORDER`는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량을 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| SHIPMENT_ID | INT(N) | FALSE |
| FLAVOR | VARCHAR(N) | FALSE |
| TOTAL_ORDER | INT(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 133024">

상반기에 판매된 아이스크림의 맛을 총주문량을 기준으로 내림차순 정렬하고 총주문량이 같다면 출하 번호를 기준으로 오름차순 정렬하여 조회하는 SQL 문을 작성해주세요.

</Callout>

---

### #09-1. 입출력 예시 (1)

예를 들어 `FIRST_HALF` 테이블이 다음과 같을 때

<Grid cols="2" align="start">
<div>

| SHIPMENT_ID | FLAVOR | TOTAL_ORDER |
| --- | --- | --- |
| 101 | chocolate | 3200 |
| 102 | vanilla | 2800 |
| 103 | mint_chocolate | 1700 |
| 104 | caramel | 2600 |
| 105 | white_chocolate | 3100 |
| 106 | peach | 2450 |

</div>
<div>

| SHIPMENT_ID | FLAVOR | TOTAL_ORDER |
| --- | --- | --- |
| 107 | watermelon | 2150 |
| 108 | mango | 2900 |
| 109 | strawberry | 3100 |
| 110 | melon | 3150 |
| 111 | orange | 2900 |
| 112 | pineapple | 2900 |

</div>
</Grid>

---

### #09-2. 입출력 예시 (2)

상반기 아이스크림 맛을 총주문량을 기준으로 내림차순 정렬하고 총주문량이 같은 경우 출하 번호를 기준으로 오름차순 정렬하면 chocolate, melon, white_chocolate, strawberry, mango, orange, pineapple, vanilla, caramel, peach, watermelon, mint_chocolate 순서대로 조회되어야 합니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

<Grid cols="3" align="start">
<div>

| FLAVOR |
| --- |
| chocolate |
| melon |
| white_chocolate |
| strawberry |

</div>
<div>

| FLAVOR |
| --- |
| mango |
| orange |
| pineapple |
| vanilla |

</div>
<div>

| FLAVOR |
| --- |
| caramel |
| peach |
| watermelon |
| mint_chocolate |

</div>
</Grid>

---

## #10. 문제 7 — 상위 n개 레코드

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59405">

동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.

</Callout>

---

### #10-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A399552 | Dog | 2013-10-14 15:38:00 | Normal | Jack | Neutered Male |
| A379998 | Dog | 2013-10-23 11:42:00 | Normal | Disciple | Intact Male |
| A370852 | Dog | 2013-11-03 15:04:00 | Normal | Katie | Spayed Female |
| A403564 | Dog | 2013-11-18 17:03:00 | Normal | Anna | Spayed Female |

이 중 가장 보호소에 먼저 들어온 동물은 Jack입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| NAME |
| --- |
| Jack |

---

### #10-2. 입출력 예시 (2)

※ 보호소에 가장 먼저 들어온 동물은 한 마리인 경우만 테스트 케이스로 주어집니다.

---

## #11. 문제 8 — 최댓값 구하기

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59415">

가장 최근에 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

</Callout>

---

### #11-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A399552 | Dog | 2013-10-14 15:38:00 | Normal | Jack | Neutered Male |
| A379998 | Dog | 2013-10-23 11:42:00 | Normal | Disciple | Intact Male |
| A370852 | Dog | 2013-11-03 15:04:00 | Normal | Katie | Spayed Female |
| A403564 | Dog | 2013-11-18 17:03:00 | Normal | Anna | Spayed Female |

가장 늦게 들어온 동물은 Anna이고, Anna는 2013-11-18 17:03:00에 들어왔습니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| 시간 |
| --- |
| 2013-11-18 17:03:00 |

---

### #11-2. 입출력 예시 (2)

※ 컬럼 이름(위 예제에서는 "시간")은 일치하지 않아도 됩니다.

---

## #12. 문제 9 — 가장 비싼 상품 구하기

<Grid cols="2" align="start">
<div>

다음은 어느 의류 쇼핑몰에서 판매 중인 상품들의 정보를 담은 `PRODUCT` 테이블입니다. `PRODUCT` 테이블은 아래와 같은 구조로 되어있으며, `PRODUCT_ID`, `PRODUCT_CODE`, `PRICE`는 각각 상품 ID, 상품코드, 판매가를 나타냅니다.

상품 별로 중복되지 않는 8자리 상품코드 값을 가지며, 앞 2자리는 카테고리 코드를 의미합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| PRODUCT_ID | INTEGER | FALSE |
| PRODUCT_CODE | VARCHAR(8) | FALSE |
| PRICE | INTEGER | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 131697">

`PRODUCT` 테이블에서 판매 중인 상품 중 가장 높은 판매가를 출력하는 SQL문을 작성해주세요. 이때 컬럼명은 MAX_PRICE로 지정해주세요.

</Callout>

---

### #12-1. 입출력 예시

예를 들어 `PRODUCT` 테이블이 다음과 같다면

| PRODUCT_ID | PRODUCT_CODE | PRICE |
| --- | --- | --- |
| 1 | A1000001 | 10000 |
| 2 | A2000005 | 9000 |
| 3 | C1000006 | 22000 |

가장 높은 판매가는 22,000 원 이므로, 다음과 같은 결과가 나와야 합니다.

| MAX_PRICE |
| --- |
| 22000 |

---

## #13. 문제 10 — 아픈 동물 찾기

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59036">

동물 보호소에 들어온 동물 중 아픈 동물[1]의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.

</Callout>

---

### #13-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A365172 | Dog | 2014-08-26 12:53:00 | Normal | Diablo | Neutered Male |
| A367012 | Dog | 2015-09-16 09:06:00 | Sick | Miller | Neutered Male |
| A365302 | Dog | 2017-01-08 16:34:00 | Aged | Minnie | Spayed Female |
| A381217 | Dog | 2017-07-08 09:41:00 | Sick | Cherokee | Neutered Male |

---

### #13-2. 입출력 예시 (2)

이 중 아픈 동물은 Miller와 Cherokee입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME |
| --- | --- |
| A367012 | Miller |
| A381217 | Cherokee |

`INTAKE_CONDITION`이 Sick 인 경우를 뜻함

---

## #14. 문제 11 — 어린 동물 찾기

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59037">

동물 보호소에 들어온 동물 중 젊은 동물[1]의 아이디와 이름을 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요.

</Callout>

---

### #14-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A365172 | Dog | 2014-08-26 12:53:00 | Normal | Diablo | Neutered Male |
| A367012 | Dog | 2015-09-16 09:06:00 | Sick | Miller | Neutered Male |
| A365302 | Dog | 2017-01-08 16:34:00 | Aged | Minnie | Spayed Female |
| A381217 | Dog | 2017-07-08 09:41:00 | Sick | Cherokee | Neutered Male |

---

### #14-2. 입출력 예시 (2)

이 중 젊은 동물은 Diablo, Miller, Cherokee입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME |
| --- | --- |
| A365172 | Diablo |
| A367012 | Miller |
| A381217 | Cherokee |

`INTAKE_CONDITION`이 Aged가 아닌 경우를 뜻함

---

## #15. 문제 12 — 이름이 없는 동물의 아이디

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59039">

동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.

</Callout>

---

### #15-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A368930 | Dog | 2014-06-08 13:20:00 | Normal | NULL | Spayed Female |
| A524634 | Dog | 2015-01-02 18:54:00 | Normal | *Belle | Intact Female |
| A465637 | Dog | 2017-06-04 08:17:00 | Injured | *Commander | Neutered Male |

이름이 없는 채로 들어온 동물의 ID는 A368930입니다. 따라서 SQL을 실행하면 다음과 같이 출력되어야 합니다.

| ANIMAL_ID |
| --- |
| A368930 |

---

### #15-2. 입출력 예시 (2)

※ 2019년 9월 4일 13시: 예시가 헷갈린다는 의견이 많아, 본문의 예시를 수정하였습니다.

---

## #16. 문제 13 — 이름이 있는 동물의 아이디

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 59407">

동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.

</Callout>

---

### #16-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A434523 | Cat | 2015-11-20 14:18:00 | Normal | NULL | Spayed Female |
| A562649 | Dog | 2014-03-20 18:06:00 | Sick | NULL | Spayed Female |
| A524634 | Dog | 2015-01-02 18:54:00 | Normal | *Belle | Intact Female |
| A465637 | Dog | 2017-06-04 08:17:00 | Injured | *Commander | Neutered Male |

---

### #16-2. 입출력 예시 (2)

이름이 있는 동물의 ID는 A524634와 A465637입니다. 따라서 SQL을 실행하면 다음과 같이 출력되어야 합니다.

| ANIMAL_ID |
| --- |
| A465637 |
| A524634 |

---

## #17. 문제 14 — 강원도에 위치한 생산공장 목록 출력하기

<Grid cols="2" align="start">
<div>

다음은 식품공장의 정보를 담은 `FOOD_FACTORY` 테이블입니다. `FOOD_FACTORY` 테이블은 다음과 같으며 `FACTORY_ID`, `FACTORY_NAME`, `ADDRESS`, `TLNO`는 각각 공장 ID, 공장 이름, 주소, 전화번호를 의미합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| FACTORY_ID | VARCHAR(10) | FALSE |
| FACTORY_NAME | VARCHAR(50) | FALSE |
| ADDRESS | VARCHAR(100) | FALSE |
| TLNO | VARCHAR(20) | TRUE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 131112">

`FOOD_FACTORY` 테이블에서 강원도에 위치한 식품공장의 공장 ID, 공장 이름, 주소를 조회하는 SQL문을 작성해주세요. 이때 결과는 공장 ID를 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #17-1. 입출력 예시 (1)

`FOOD_FACTORY` 테이블이 다음과 같을 때

| FACTORY_ID | FACTORY_NAME | ADDRESS | TLNO |
| --- | --- | --- | --- |
| FT19980003 | (주)맛있는라면 | 강원도 정선군 남면 칠현로 679 | 033-431-3122 |
| FT19980004 | (주)맛있는기름 | 경기도 평택시 포승읍 포승공단순환로 245 | 031-651-2410 |
| FT20010001 | (주)맛있는소스 | 경상북도 구미시 1공단로7길 58-11 | 054-231-2121 |
| FT20010002 | (주)맛있는통조림 | 전라남도 영암군 미암면 곤미현로 1336 | 061-341-5210 |
| FT20100001 | (주)맛있는차 | 전라남도 장성군 서삼면 장산리 233-1번지 | 061-661-1420 |

---

### #17-2. 입출력 예시 (2)

| FACTORY_ID | FACTORY_NAME | ADDRESS | TLNO |
| --- | --- | --- | --- |
| FT20100002 | (주)맛있는김치 | 충청남도 아산시 탕정면 탕정면로 485 | 041-241-5421 |
| FT20100003 | (주)맛있는음료 | 강원도 원주시 문막읍 문막공단길 154 | 033-232-7630 |
| FT20100004 | (주)맛있는국 | 강원도 평창군 봉평면 진조길 227-35 | 033-323-6640 |
| FT20110001 | (주)맛있는밥 | 경기도 화성시 팔탄면 가재리 34번지 | 031-661-1532 |
| FT20110002 | (주)맛있는과자 | 광주광역시 북구 하서로 222 | 062-211-7759 |

---

### #17-3. 입출력 예시 (3)

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| FACTORY_ID | FACTORY_NAME | ADDRESS |
| --- | --- | --- |
| FT19980003 | (주)맛있는라면 | 강원도 정선군 남면 칠현로 679 |
| FT20100003 | (주)맛있는음료 | 강원도 원주시 문막읍 문막공단길 154 |
| FT20100004 | (주)맛있는국 | 강원도 평창군 봉평면 진조길 227-35 |

---
class: tight
---

## #18. 문제 15 — Python 개발자 찾기

<Grid cols="2" align="start">
<div>

`DEVELOPER_INFOS` 테이블은 개발자들의 프로그래밍 스킬 정보를 담은 테이블입니다. `DEVELOPER_INFOS` 테이블 구조는 다음과 같으며, `ID`, `FIRST_NAME`, `LAST_NAME`, `EMAIL`, `SKILL_1`, `SKILL_2`, `SKILL_3`는 각각 ID, 이름, 성, 이메일, 첫 번째 스킬, 두 번째 스킬, 세 번째 스킬을 의미합니다.

</div>
<div>

| NAME | TYPE | UNIQUE | NULLABLE |
| --- | --- | --- | --- |
| ID | VARCHAR(N) | Y | N |
| FIRST_NAME | VARCHAR(N) | N | Y |
| LAST_NAME | VARCHAR(N) | N | Y |
| EMAIL | VARCHAR(N) | Y | N |
| SKILL_1 | VARCHAR(N) | N | Y |
| SKILL_2 | VARCHAR(N) | N | Y |
| SKILL_3 | VARCHAR(N) | N | Y |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 276013">

`DEVELOPER_INFOS` 테이블에서 Python 스킬을 가진 개발자의 정보를 조회하려 합니다. Python 스킬을 가진 개발자의 ID, 이메일, 이름, 성을 조회하는 SQL 문을 작성해 주세요. 결과는 ID를 기준으로 오름차순 정렬해 주세요.

</Callout>

---

### #18-1. 입출력 예시 (1)

예를 들어 `DEVELOPER_INFOS` 테이블이 다음과 같다면

| ID | FIRST_NAME | LAST_NAME | EMAIL | SKILL_1 | SKILL_2 | SKILL_3 |
| --- | --- | --- | --- | --- | --- | --- |
| D165 | Jerami | Edwards | `jerami_edwards@grepp.co` | Java | JavaScript | Python |
| D161 | Carsen | Garza | `carsen_garza@grepp.co` | React |  |  |
| D164 | Kelly | Grant | `kelly_grant@grepp.co` | C# |  |  |
| D163 | Luka | Cory | `luka_cory@grepp.co` | Node.js |  |  |
| D162 | Cade | Cunningham | `cade_cunningham@grepp.co` | Vue | C++ | Python |

---

### #18-2. 입출력 예시 (2)

다음과 같이 Python 스킬을 가진 개발자의 정보가 결과에 나와야 합니다.

| ID | EMAIL | FIRST_NAME | LAST_NAME |
| --- | --- | --- | --- |
| D162 | `cade_cunningham@grepp.co` | Cade | Cunningham |
| D165 | `jerami_edwards@grepp.co` | Jerami | Edwards |

---

## #19. 문제 16 — 최솟값 구하기

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59038">

동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

</Callout>

---

### #19-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A399552 | Dog | 2013-10-14 15:38:00 | Normal | Jack | Neutered Male |
| A379998 | Dog | 2013-10-23 11:42:00 | Normal | Disciple | Intact Male |
| A370852 | Dog | 2013-11-03 15:04:00 | Normal | Katie | Spayed Female |
| A403564 | Dog | 2013-11-18 17:03:00 | Normal | Anna | Spayed Female |

가장 먼저 들어온 동물은 Jack이고, Jack은 2013-10-14 15:38:00에 들어왔습니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| 시간 |
| --- |
| 2013-10-14 15:38:00 |

---

### #19-2. 입출력 예시 (2)

※ 컬럼 이름(위 예제에서는 "시간")은 일치하지 않아도 됩니다.

---

## #20. 문제 17 — 가격이 제일 비싼 식품의 정보 출력하기

<Grid cols="2" align="start">
<div>

다음은 식품의 정보를 담은 `FOOD_PRODUCT` 테이블입니다. `FOOD_PRODUCT` 테이블은 다음과 같으며 `PRODUCT_ID`, `PRODUCT_NAME`, `PRODUCT_CD`, `CATEGORY`, `PRICE`는 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 의미합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| PRODUCT_ID | VARCHAR(10) | FALSE |
| PRODUCT_NAME | VARCHAR(50) | FALSE |
| PRODUCT_CD | VARCHAR(10) | TRUE |
| CATEGORY | VARCHAR(10) | TRUE |
| PRICE | NUMBER | TRUE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 131115">

`FOOD_PRODUCT` 테이블에서 가격이 제일 비싼 식품의 식품 ID, 식품 이름, 식품 코드, 식품분류, 식품 가격을 조회하는 SQL문을 작성해주세요.

</Callout>

---

### #20-1. 입출력 예시 (1)

`FOOD_PRODUCT` 테이블이 다음과 같을 때

| PRODUCT_ID | PRODUCT_NAME | PRODUCT_CD | CATEGORY | PRICE |
| --- | --- | --- | --- | --- |
| P0018 | 맛있는고추기름 | CD_OL00008 | 식용유 | 6100 |
| P0019 | 맛있는카놀라유 | CD_OL00009 | 식용유 | 5100 |
| P0020 | 맛있는산초유 | CD_OL00010 | 식용유 | 6500 |
| P0021 | 맛있는케첩 | CD_OL00001 | 소스 | 4500 |
| P0022 | 맛있는마요네즈 | CD_OL00002 | 소스 | 4700 |

---

### #20-2. 입출력 예시 (2)

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| PRODUCT_ID | PRODUCT_NAME | PRODUCT_CD | CATEGORY | PRICE |
| --- | --- | --- | --- | --- |
| P0020 | 맛있는산초유 | CD_OL00010 | 식용유 | 6500 |

---

## #21. 문제 18 — 루시와 엘라 찾기

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59046">

동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요.

</Callout>

---

### #21-1. 입출력 예시 (1)

이때 결과는 아이디 순으로 조회해주세요. 예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A373219 | Cat | 2014-07-29 11:43:00 | Normal | Ella | Spayed Female |
| A377750 | Dog | 2017-10-25 17:17:00 | Normal | Lucy | Spayed Female |
| A353259 | Dog | 2016-05-08 12:57:00 | Injured | Bj | Neutered Male |
| A354540 | Cat | 2014-12-11 11:48:00 | Normal | Tux | Neutered Male |
| A354597 | Cat | 2014-05-02 12:16:00 | Normal | Ariel | Spayed Female |

---

### #21-2. 입출력 예시 (2)

SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME | SEX_UPON_INTAKE |
| --- | --- | --- |
| A373219 | Ella | Spayed Female |
| A377750 | Lucy | Spayed Female |

---
class: tight
---

## #22. 문제 19 — 이름에 el이 들어가는 동물 찾기

<Grid cols="2" align="start">
<div>

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59047">

보호소에 돌아가신 할머니가 기르던 개를 찾는 사람이 찾아왔습니다. 이 사람이 말하길 할머니가 기르던 개는 이름에 'el'이 들어간다고 합니다. 동물 보호소에 들어온 동물 이름 중, 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 만약 이름이 같은 경우 아이디를 기준으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.

</Callout>

---

### #22-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A355753 | Dog | 2015-09-10 13:14:00 | Normal | Elijah | Neutered Male |
| A352872 | Dog | 2015-07-09 17:51:00 | Aged | Peanutbutter | Neutered Male |
| A353259 | Dog | 2016-05-08 12:57:00 | Injured | Bj | Neutered Male |
| A373219 | Cat | 2014-07-29 11:43:00 | Normal | Ella | Spayed Female |
| A382192 | Dog | 2015-03-13 13:14:00 | Normal | Maxwell 2 | Intact Male |

- 이름에 'el'이 들어가는 동물은 Elijah, Ella, Maxwell 2입니다.
- 이 중, 개는 Elijah, Maxwell 2입니다.

---

### #22-2. 입출력 예시 (2)

따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME |
| --- | --- |
| A355753 | Elijah |
| A382192 | Maxwell 2 |

---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-02] 데이터 조회하기 5 · ITWILL · {teacher} 강사</p>

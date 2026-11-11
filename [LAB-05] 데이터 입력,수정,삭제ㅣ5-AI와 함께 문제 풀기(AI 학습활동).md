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

<p class="sub">[LAB-05] 데이터 입력,수정,삭제 (5) / ITWILL - 주영아·이광호 강사</p>

---
layout: section
---

# SQL 코딩 테스트

앞서 배운 상황별 템플릿으로 프롬프트를 직접 작성하여 문제를 풀어보세요

문제를 풀기 전에 <code>lab05_setup.sql</code>을 실행해 실습용 테이블을 만드세요. 처음 상태로 되돌릴 때도 다시 실행합니다

---

## #01. 문제 1 — 새 회원 등록하기

<Grid cols="2" align="start">
<div>

다음은 동아리 회원 정보를 담은 `LAB05_MEMBER` 테이블입니다. `MEMBER_ID`, `NAME`, `GRADE`, `PHONE`, `STATUS`, `CLUB_ID`는 각각 회원 번호, 이름, 학년, 연락처, 활동 상태(활동, 휴면), 소속 동아리 번호를 의미합니다. `MEMBER_ID`는 기본키이며 자동 증가 일련번호입니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| MEMBER_ID | INT | FALSE |
| NAME | VARCHAR(20) | FALSE |
| GRADE | INT | FALSE |
| PHONE | VARCHAR(15) | TRUE |
| STATUS | VARCHAR(10) | FALSE |
| CLUB_ID | INT | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

독서부(동아리 번호 1)에 1학년 '정하윤' 학생이 '활동' 상태로 가입했습니다. 회원 번호는 자동으로 생성되게 하고, 연락처는 아직 받지 못해 비워 두려고 합니다. 이 회원을 `LAB05_MEMBER` 테이블에 등록하는 SQL문을 작성해주세요.

</Callout>

---

### #01-1. 입출력 예시 (1)

`LAB05_MEMBER` 테이블이 다음과 같을 때

| MEMBER_ID | NAME | GRADE | PHONE | STATUS | CLUB_ID |
| --- | --- | --- | --- | --- | --- |
| 1 | 김민준 | 4 | 010-1111-2222 | 휴면 | 1 |
| 2 | 이서연 | 3 | 010-2222-3333 | 활동 | 1 |
| 3 | 박도윤 | 2 | 010-3333-4444 | 활동 | 2 |
| 4 | 최지우 | 4 | 010-4444-5555 | 활동 | 2 |
| 5 | 정예준 | 1 | NULL | 활동 | 3 |
| 6 | 강하은 | 3 | 010-6666-7777 | 휴면 | 3 |
| 7 | 윤시우 | 4 | 010-7777-8888 | 휴면 | 2 |
| 8 | 한지민 | 2 | 010-8888-9999 | 활동 | 4 |

---

### #01-2. 입출력 예시 (2)

SQL을 실행한 뒤 `SELECT * FROM LAB05_MEMBER WHERE NAME = '정하윤';`을 실행하면 다음과 같이 출력되어야 합니다.

| MEMBER_ID | NAME | GRADE | PHONE | STATUS | CLUB_ID |
| --- | --- | --- | --- | --- | --- |
| 9 | 정하윤 | 1 | NULL | 활동 | 1 |

---
class: tight
---

## #02. 문제 2 — 새 동아리와 첫 회원 등록하기

다음은 동아리 정보를 담은 `LAB05_CLUB` 테이블입니다. `CLUB_ID`, `CLUB_NAME`, `ROOM`, `FEE`는 각각 동아리 번호, 동아리 이름, 동아리방, 월 회비(원)를 의미합니다. `CLUB_ID`는 기본키입니다.

다음은 동아리 회원 정보를 담은 `LAB05_MEMBER` 테이블입니다. `MEMBER_ID`, `NAME`, `GRADE`, `PHONE`, `STATUS`, `CLUB_ID`는 각각 회원 번호, 이름, 학년, 연락처, 활동 상태(활동, 휴면), 소속 동아리 번호를 의미합니다. `MEMBER_ID`는 자동 증가 일련번호인 기본키이고, `CLUB_ID`는 `LAB05_CLUB` 테이블의 `CLUB_ID`를 참조하는 참조키입니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

새 동아리 '밴드부'가 생겼습니다. 동아리 번호는 5, 동아리방은 '예술관 B101호', 월 회비는 7000원입니다. 밴드부의 첫 회원은 2학년 '오유나' 학생이며 연락처는 '010-5555-1234', 상태는 '활동'입니다. 회원 번호는 자동으로 생성되게 하여, 밴드부와 첫 회원을 등록하는 SQL문을 작성해주세요.

</Callout>

---

### #02-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">LAB05_CLUB</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| CLUB_ID | INT | FALSE |
| CLUB_NAME | VARCHAR(30) | FALSE |
| ROOM | VARCHAR(30) | FALSE |
| FEE | INT | FALSE |

</div>
<div>

<div class="kicker">LAB05_MEMBER</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| MEMBER_ID | INT | FALSE |
| NAME | VARCHAR(20) | FALSE |
| GRADE | INT | FALSE |
| PHONE | VARCHAR(15) | TRUE |
| STATUS | VARCHAR(10) | FALSE |
| CLUB_ID | INT | FALSE |

</div>
</Grid>

---

### #02-2. 입출력 예시 (2)

`LAB05_CLUB` 테이블이 다음과 같고, `LAB05_MEMBER` 테이블에는 `CLUB_ID`가 5인 회원이 없을 때

| CLUB_ID | CLUB_NAME | ROOM | FEE |
| --- | --- | --- | --- |
| 1 | 독서부 | 학생회관 201호 | 3000 |
| 2 | 코딩부 | 학생회관 305호 | 5000 |
| 3 | 축구부 | 운동장 클럽하우스 | 10000 |
| 4 | 풋살부 | 체육관 102호 | 8000 |

SQL을 실행한 뒤 `SELECT * FROM LAB05_CLUB WHERE CLUB_ID = 5;`를 실행하면 다음과 같이 출력되어야 합니다.

| CLUB_ID | CLUB_NAME | ROOM | FEE |
| --- | --- | --- | --- |
| 5 | 밴드부 | 예술관 B101호 | 7000 |

---

### #02-3. 입출력 예시 (3)

이어서 `SELECT NAME, GRADE, PHONE, STATUS, CLUB_ID FROM LAB05_MEMBER WHERE CLUB_ID = 5;`를 실행하면 다음과 같이 출력되어야 합니다.

| NAME | GRADE | PHONE | STATUS | CLUB_ID |
| --- | --- | --- | --- | --- |
| 오유나 | 2 | 010-5555-1234 | 활동 | 5 |

---

## #03. 문제 3 — 학생회관 동아리 회비 인상하기

<Grid cols="2" align="start">
<div>

다음은 동아리 정보를 담은 `LAB05_CLUB` 테이블입니다. `CLUB_ID`, `CLUB_NAME`, `ROOM`, `FEE`는 각각 동아리 번호, 동아리 이름, 동아리방, 월 회비(원)를 의미합니다. `CLUB_ID`는 기본키입니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| CLUB_ID | INT | FALSE |
| CLUB_NAME | VARCHAR(30) | FALSE |
| ROOM | VARCHAR(30) | FALSE |
| FEE | INT | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

학생회관의 관리비가 올라, 동아리방이 학생회관에 있는 동아리의 월 회비를 지금보다 1000원씩 올리기로 했습니다. 동아리방이 '학생회관'으로 시작하는 동아리의 월 회비를 1000원씩 인상하는 SQL문을 작성해주세요.

</Callout>

---

### #03-1. 입출력 예시

`LAB05_CLUB` 테이블이 다음과 같을 때

| CLUB_ID | CLUB_NAME | ROOM | FEE |
| --- | --- | --- | --- |
| 1 | 독서부 | 학생회관 201호 | 3000 |
| 2 | 코딩부 | 학생회관 305호 | 5000 |
| 3 | 축구부 | 운동장 클럽하우스 | 10000 |
| 4 | 풋살부 | 체육관 102호 | 8000 |

SQL을 실행한 뒤 `SELECT * FROM LAB05_CLUB WHERE ROOM LIKE '학생회관%' ORDER BY CLUB_ID;`를 실행하면 다음과 같이 출력되어야 합니다.

| CLUB_ID | CLUB_NAME | ROOM | FEE |
| --- | --- | --- | --- |
| 1 | 독서부 | 학생회관 201호 | 4000 |
| 2 | 코딩부 | 학생회관 305호 | 6000 |

---

## #04. 문제 4 — 4학년 휴면 회원 삭제하기

<Grid cols="2" align="start">
<div>

다음은 동아리 회원 정보를 담은 `LAB05_MEMBER` 테이블입니다. `MEMBER_ID`, `NAME`, `GRADE`, `PHONE`, `STATUS`, `CLUB_ID`는 각각 회원 번호, 이름, 학년, 연락처, 활동 상태(활동, 휴면), 소속 동아리 번호를 의미합니다. `MEMBER_ID`는 기본키입니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| MEMBER_ID | INT | FALSE |
| NAME | VARCHAR(20) | FALSE |
| GRADE | INT | FALSE |
| PHONE | VARCHAR(15) | TRUE |
| STATUS | VARCHAR(10) | FALSE |
| CLUB_ID | INT | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

졸업을 앞두고 활동하지 않는 회원을 정리하려고 합니다. 4학년이면서 상태가 '휴면'인 회원만 `LAB05_MEMBER` 테이블에서 삭제하는 SQL문을 작성해주세요.

</Callout>

---

### #04-1. 입출력 예시 (1)

`LAB05_MEMBER` 테이블이 다음과 같을 때

| MEMBER_ID | NAME | GRADE | PHONE | STATUS | CLUB_ID |
| --- | --- | --- | --- | --- | --- |
| 1 | 김민준 | 4 | 010-1111-2222 | 휴면 | 1 |
| 2 | 이서연 | 3 | 010-2222-3333 | 활동 | 1 |
| 3 | 박도윤 | 2 | 010-3333-4444 | 활동 | 2 |
| 4 | 최지우 | 4 | 010-4444-5555 | 활동 | 2 |
| 5 | 정예준 | 1 | NULL | 활동 | 3 |
| 6 | 강하은 | 3 | 010-6666-7777 | 휴면 | 3 |
| 7 | 윤시우 | 4 | 010-7777-8888 | 휴면 | 2 |
| 8 | 한지민 | 2 | 010-8888-9999 | 활동 | 4 |

---

### #04-2. 입출력 예시 (2)

4학년이면서 휴면인 회원은 김민준, 윤시우 두 명입니다. 4학년이지만 활동 중인 최지우와, 휴면이지만 3학년인 강하은은 남아야 합니다. SQL을 실행한 뒤 `SELECT * FROM LAB05_MEMBER WHERE GRADE = 4 OR STATUS = '휴면' ORDER BY MEMBER_ID;`를 실행하면 다음과 같이 출력되어야 합니다.

| MEMBER_ID | NAME | GRADE | PHONE | STATUS | CLUB_ID |
| --- | --- | --- | --- | --- | --- |
| 4 | 최지우 | 4 | 010-4444-5555 | 활동 | 2 |
| 6 | 강하은 | 3 | 010-6666-7777 | 휴면 | 3 |

---
class: tight
---

## #05. 문제 5 — 축구부를 풋살부로 합치기

다음은 동아리 정보를 담은 `LAB05_CLUB` 테이블입니다. `CLUB_ID`, `CLUB_NAME`, `ROOM`, `FEE`는 각각 동아리 번호, 동아리 이름, 동아리방, 월 회비(원)를 의미합니다. `CLUB_ID`는 기본키입니다.

다음은 동아리 회원 정보를 담은 `LAB05_MEMBER` 테이블입니다. `MEMBER_ID`, `NAME`, `GRADE`, `PHONE`, `STATUS`, `CLUB_ID`는 각각 회원 번호, 이름, 학년, 연락처, 활동 상태(활동, 휴면), 소속 동아리 번호를 의미합니다. `MEMBER_ID`는 기본키이고, `CLUB_ID`는 `LAB05_CLUB` 테이블의 `CLUB_ID`를 참조하는 참조키입니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

축구부(동아리 번호 3)가 풋살부(동아리 번호 4)와 합쳐집니다. 축구부 회원을 모두 풋살부로 옮기고 축구부를 삭제해야 하는데, 두 작업 중 하나만 반영되면 안 됩니다. 두 작업을 하나의 트랜잭션으로 묶어 실행하고, 결과를 확인한 뒤 이상이 없으면 COMMIT, 이상이 있으면 ROLLBACK하는 SQL문을 작성해주세요.

</Callout>

---

### #05-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">LAB05_CLUB</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| CLUB_ID | INT | FALSE |
| CLUB_NAME | VARCHAR(30) | FALSE |
| ROOM | VARCHAR(30) | FALSE |
| FEE | INT | FALSE |

</div>
<div>

<div class="kicker">LAB05_MEMBER</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| MEMBER_ID | INT | FALSE |
| NAME | VARCHAR(20) | FALSE |
| GRADE | INT | FALSE |
| PHONE | VARCHAR(15) | TRUE |
| STATUS | VARCHAR(10) | FALSE |
| CLUB_ID | INT | FALSE |

</div>
</Grid>

---

### #05-2. 입출력 예시 (2)

`LAB05_CLUB` 테이블이 다음과 같고

| CLUB_ID | CLUB_NAME | ROOM | FEE |
| --- | --- | --- | --- |
| 1 | 독서부 | 학생회관 201호 | 3000 |
| 2 | 코딩부 | 학생회관 305호 | 5000 |
| 3 | 축구부 | 운동장 클럽하우스 | 10000 |
| 4 | 풋살부 | 체육관 102호 | 8000 |

---

### #05-3. 입출력 예시 (3)

`LAB05_MEMBER` 테이블이 다음과 같을 때

| MEMBER_ID | NAME | GRADE | PHONE | STATUS | CLUB_ID |
| --- | --- | --- | --- | --- | --- |
| 1 | 김민준 | 4 | 010-1111-2222 | 휴면 | 1 |
| 2 | 이서연 | 3 | 010-2222-3333 | 활동 | 1 |
| 3 | 박도윤 | 2 | 010-3333-4444 | 활동 | 2 |
| 4 | 최지우 | 4 | 010-4444-5555 | 활동 | 2 |
| 5 | 정예준 | 1 | NULL | 활동 | 3 |
| 6 | 강하은 | 3 | 010-6666-7777 | 휴면 | 3 |
| 7 | 윤시우 | 4 | 010-7777-8888 | 휴면 | 2 |
| 8 | 한지민 | 2 | 010-8888-9999 | 활동 | 4 |

---

### #05-4. 입출력 예시 (4)

COMMIT한 뒤 `SELECT * FROM LAB05_CLUB WHERE CLUB_ID IN (3, 4);`를 실행하면 다음과 같이 출력되어야 합니다.

| CLUB_ID | CLUB_NAME | ROOM | FEE |
| --- | --- | --- | --- |
| 4 | 풋살부 | 체육관 102호 | 8000 |

이어서 `SELECT MEMBER_ID, NAME, CLUB_ID FROM LAB05_MEMBER WHERE CLUB_ID IN (3, 4) ORDER BY MEMBER_ID;`를 실행하면 다음과 같이 출력되어야 합니다.

| MEMBER_ID | NAME | CLUB_ID |
| --- | --- | --- |
| 5 | 정예준 | 4 |
| 6 | 강하은 | 4 |
| 8 | 한지민 | 4 |


---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-05] 데이터 입력,수정,삭제 5 · ITWILL · {teacher} 강사</p>

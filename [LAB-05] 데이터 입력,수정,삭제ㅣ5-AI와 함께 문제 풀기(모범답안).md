# [LAB-05] 데이터 입력,수정,삭제ㅣ5-AI와 함께 문제 풀기 모범답안

「[LAB-05] 데이터 입력,수정,삭제ㅣ5-AI와 함께 문제 풀기(AI 학습활동)」 덱의 문제 5개에 대한 정답 SQL과, 두 템플릿(방향 묻기 · 원인 묻기)을 빈칸 없이 채운 프롬프트를 담았다.

## 문제 1. 새 회원 등록하기

- Level 1 · 직접 만든 문제 · INSERT

### 정답 SQL

```sql
INSERT INTO LAB05_MEMBER (NAME, GRADE, STATUS, CLUB_ID)
VALUES ('정하윤', 1, '활동', 1);

SELECT * FROM LAB05_MEMBER WHERE NAME = '정하윤';
```

- 확인 결과: 1행

```text
+-----------+-----------+-------+-------+--------+---------+
| MEMBER_ID | NAME      | GRADE | PHONE | STATUS | CLUB_ID |
+-----------+-----------+-------+-------+--------+---------+
|         9 | 정하윤    |     1 | NULL  | 활동   |       1 |
+-----------+-----------+-------+-------+--------+---------+
```

- 풀이 핵심: 일부 컬럼만 저장할 때는 테이블 이름 뒤에 컬럼 이름을 나열함. 생략한 자동 증가 컬럼에는 다음 번호가, 생략한 `PHONE`에는 NULL이 저장됨

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
LAB05_MEMBER 테이블 구조:
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| MEMBER_ID | int(11)     | NO   | PRI | NULL    | auto_increment |
| NAME      | varchar(20) | NO   |     | NULL    |                |
| GRADE     | int(11)     | NO   |     | NULL    |                |
| PHONE     | varchar(15) | YES  |     | NULL    |                |
| STATUS    | varchar(10) | NO   |     | NULL    |                |
| CLUB_ID   | int(11)     | NO   | MUL | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
- 컬럼 뜻: 회원 번호(자동 증가) · 이름 · 학년 · 연락처 · 활동 상태(활동, 휴면) · 소속 동아리 번호
- 내가 이해한 문제: 독서부(1번)에 1학년 정하윤 회원을 활동 상태로 등록하는데, 회원 번호는 자동으로 만들고 연락처는 비워 둠

## 질문
내 이해가 맞는지 봐 주고, 필요한 구문과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · INSERT · UPDATE · DELETE · 트랜잭션(START TRANSACTION · COMMIT · ROLLBACK) 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 컬럼 이름을 쓰지 않고 넣을 값 4개만 나열함. 컬럼 이름을 생략하면 6개 컬럼 값을 모두 순서대로 써야 함

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
독서부(1번)에 1학년 정하윤 회원을 활동 상태로 등록하려고 해. 회원 번호는 자동으로 만들고 연락처는 비워 둘 거야.
LAB05_MEMBER 테이블 구조:
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| MEMBER_ID | int(11)     | NO   | PRI | NULL    | auto_increment |
| NAME      | varchar(20) | NO   |     | NULL    |                |
| GRADE     | int(11)     | NO   |     | NULL    |                |
| PHONE     | varchar(15) | YES  |     | NULL    |                |
| STATUS    | varchar(10) | NO   |     | NULL    |                |
| CLUB_ID   | int(11)     | NO   | MUL | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```sql
INSERT INTO LAB05_MEMBER VALUES ('정하윤', 1, '활동', 1);
```
- 기대한 결과: 1행이 저장되고 확인용 SELECT에서 (9, 정하윤, 1, NULL, 활동, 1)
- 실제 결과: ERROR 1136 (21S01): Column count doesn't match value count at row 1

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 2. 새 동아리와 첫 회원 등록하기

- Level 1 · 직접 만든 문제 · INSERT · 참조키

### 정답 SQL

```sql
INSERT INTO LAB05_CLUB VALUES (5, '밴드부', '예술관 B101호', 7000);

INSERT INTO LAB05_MEMBER (NAME, GRADE, PHONE, STATUS, CLUB_ID)
VALUES ('오유나', 2, '010-5555-1234', '활동', 5);

SELECT * FROM LAB05_CLUB WHERE CLUB_ID = 5;
SELECT NAME, GRADE, PHONE, STATUS, CLUB_ID FROM LAB05_MEMBER WHERE CLUB_ID = 5;
```

- 확인 결과: 각 1행

```text
+---------+-----------+-------------------+------+
| CLUB_ID | CLUB_NAME | ROOM              | FEE  |
+---------+-----------+-------------------+------+
|       5 | 밴드부    | 예술관 B101호     | 7000 |
+---------+-----------+-------------------+------+
+-----------+-------+---------------+--------+---------+
| NAME      | GRADE | PHONE         | STATUS | CLUB_ID |
+-----------+-------+---------------+--------+---------+
| 오유나    |     2 | 010-5555-1234 | 활동   |       5 |
+-----------+-------+---------------+--------+---------+
```

- 풀이 핵심: 참조키 컬럼에는 부모 테이블에 있는 값만 저장할 수 있으므로 부모(`LAB05_CLUB`)를 먼저, 자식(`LAB05_MEMBER`)을 나중에 저장함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
LAB05_CLUB 테이블 구조:
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| CLUB_ID   | int(11)     | NO   | PRI | NULL    |       |
| CLUB_NAME | varchar(30) | NO   |     | NULL    |       |
| ROOM      | varchar(30) | NO   |     | NULL    |       |
| FEE       | int(11)     | NO   |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
LAB05_MEMBER 테이블 구조:
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| MEMBER_ID | int(11)     | NO   | PRI | NULL    | auto_increment |
| NAME      | varchar(20) | NO   |     | NULL    |                |
| GRADE     | int(11)     | NO   |     | NULL    |                |
| PHONE     | varchar(15) | YES  |     | NULL    |                |
| STATUS    | varchar(10) | NO   |     | NULL    |                |
| CLUB_ID   | int(11)     | NO   | MUL | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
- LAB05_CLUB 컬럼 뜻: 동아리 번호 · 동아리 이름 · 동아리방 · 월 회비(원)
- LAB05_MEMBER 컬럼 뜻: 회원 번호(자동 증가) · 이름 · 학년 · 연락처 · 활동 상태(활동, 휴면) · 소속 동아리 번호(LAB05_CLUB의 CLUB_ID를 참조하는 참조키)
- 내가 이해한 문제: 5번 밴드부(예술관 B101호, 월 회비 7000원)를 만들고, 첫 회원 오유나(2학년, 010-5555-1234, 활동)를 밴드부 소속으로 등록

## 질문
내 이해가 맞는지 봐 주고, 필요한 구문과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · INSERT · UPDATE · DELETE · 트랜잭션(START TRANSACTION · COMMIT · ROLLBACK) 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 회원을 먼저 저장하고 동아리를 나중에 저장함. 5번 동아리가 아직 없어 회원 저장이 참조 무결성 위반으로 거부됨

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
5번 밴드부(예술관 B101호, 월 회비 7000원)를 만들고, 첫 회원 오유나(2학년, 010-5555-1234, 활동)를 밴드부 소속으로 등록하려고 해.
LAB05_CLUB 테이블 구조:
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| CLUB_ID   | int(11)     | NO   | PRI | NULL    |       |
| CLUB_NAME | varchar(30) | NO   |     | NULL    |       |
| ROOM      | varchar(30) | NO   |     | NULL    |       |
| FEE       | int(11)     | NO   |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
LAB05_MEMBER 테이블 구조:
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| MEMBER_ID | int(11)     | NO   | PRI | NULL    | auto_increment |
| NAME      | varchar(20) | NO   |     | NULL    |                |
| GRADE     | int(11)     | NO   |     | NULL    |                |
| PHONE     | varchar(15) | YES  |     | NULL    |                |
| STATUS    | varchar(10) | NO   |     | NULL    |                |
| CLUB_ID   | int(11)     | NO   | MUL | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```sql
INSERT INTO LAB05_MEMBER (NAME, GRADE, PHONE, STATUS, CLUB_ID)
VALUES ('오유나', 2, '010-5555-1234', '활동', 5);

INSERT INTO LAB05_CLUB VALUES (5, '밴드부', '예술관 B101호', 7000);
```
- 기대한 결과: 두 문장 모두 저장되고, 확인용 SELECT에서 밴드부 1행 · CLUB_ID가 5인 회원 1행(오유나)
- 실제 결과: 첫 문장에서 ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`myschool`.`lab05_member`, CONSTRAINT `lab05_member_ibfk_1` FOREIGN KEY (`CLUB_ID`) REFERENCES `LAB05_CLUB` (`CLUB_ID`)). 확인용 SELECT에서 밴드부 1행 · CLUB_ID가 5인 회원 0행

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 3. 학생회관 동아리 회비 인상하기

- Level 1 · 직접 만든 문제 · UPDATE

### 정답 SQL

```sql
UPDATE LAB05_CLUB
SET FEE = FEE + 1000
WHERE ROOM LIKE '학생회관%';

SELECT * FROM LAB05_CLUB WHERE ROOM LIKE '학생회관%' ORDER BY CLUB_ID;
```

- 확인 결과: 2행

```text
+---------+-----------+---------------------+------+
| CLUB_ID | CLUB_NAME | ROOM                | FEE  |
+---------+-----------+---------------------+------+
|       1 | 독서부    | 학생회관 201호      | 4000 |
|       2 | 코딩부    | 학생회관 305호      | 6000 |
+---------+-----------+---------------------+------+
```

- 풀이 핵심: 지금 값에서 늘릴 때는 `SET FEE = FEE + 1000`처럼 컬럼 자신을 계산식에 쓰고, `WHERE`로 수정할 행을 고름

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
LAB05_CLUB 테이블 구조:
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| CLUB_ID   | int(11)     | NO   | PRI | NULL    |       |
| CLUB_NAME | varchar(30) | NO   |     | NULL    |       |
| ROOM      | varchar(30) | NO   |     | NULL    |       |
| FEE       | int(11)     | NO   |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 동아리 번호 · 동아리 이름 · 동아리방 · 월 회비(원)
- 내가 이해한 문제: 동아리방이 '학생회관'으로 시작하는 동아리만 골라 월 회비를 지금보다 1000원씩 올림

## 질문
내 이해가 맞는지 봐 주고, 필요한 구문과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · INSERT · UPDATE · DELETE · 트랜잭션(START TRANSACTION · COMMIT · ROLLBACK) 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `SET FEE = 1000`으로 써서 회비가 1000원 오르지 않고 1000원으로 바뀜

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
동아리방이 '학생회관'으로 시작하는 동아리의 월 회비를 지금보다 1000원씩 올리려고 해.
LAB05_CLUB 테이블 구조:
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| CLUB_ID   | int(11)     | NO   | PRI | NULL    |       |
| CLUB_NAME | varchar(30) | NO   |     | NULL    |       |
| ROOM      | varchar(30) | NO   |     | NULL    |       |
| FEE       | int(11)     | NO   |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
```sql
UPDATE LAB05_CLUB
SET FEE = 1000
WHERE ROOM LIKE '학생회관%';

SELECT * FROM LAB05_CLUB WHERE ROOM LIKE '학생회관%' ORDER BY CLUB_ID;
```
- 기대한 결과: 2행: (1, 독서부, 학생회관 201호, 4000) / (2, 코딩부, 학생회관 305호, 6000)
- 실제 결과: 2행: (1, 독서부, 학생회관 201호, 1000) / (2, 코딩부, 학생회관 305호, 1000)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 4. 4학년 휴면 회원 삭제하기

- Level 1 · 직접 만든 문제 · DELETE

### 정답 SQL

```sql
DELETE FROM LAB05_MEMBER
WHERE GRADE = 4 AND STATUS = '휴면';

SELECT * FROM LAB05_MEMBER WHERE GRADE = 4 OR STATUS = '휴면' ORDER BY MEMBER_ID;
```

- 확인 결과: 2행 (김민준 · 윤시우가 삭제되고 최지우 · 강하은이 남음)

```text
+-----------+-----------+-------+---------------+--------+---------+
| MEMBER_ID | NAME      | GRADE | PHONE         | STATUS | CLUB_ID |
+-----------+-----------+-------+---------------+--------+---------+
|         4 | 최지우    |     4 | 010-4444-5555 | 활동   |       2 |
|         6 | 강하은    |     3 | 010-6666-7777 | 휴면   |       3 |
+-----------+-----------+-------+---------------+--------+---------+
```

- 풀이 핵심: 두 조건을 모두 만족하는 행만 지우려면 `AND`로 연결함. 지우기 전에 같은 `WHERE`로 `SELECT`해 보면 안전함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
LAB05_MEMBER 테이블 구조:
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| MEMBER_ID | int(11)     | NO   | PRI | NULL    | auto_increment |
| NAME      | varchar(20) | NO   |     | NULL    |                |
| GRADE     | int(11)     | NO   |     | NULL    |                |
| PHONE     | varchar(15) | YES  |     | NULL    |                |
| STATUS    | varchar(10) | NO   |     | NULL    |                |
| CLUB_ID   | int(11)     | NO   | MUL | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
- 컬럼 뜻: 회원 번호 · 이름 · 학년 · 연락처 · 활동 상태(활동, 휴면) · 소속 동아리 번호
- 내가 이해한 문제: 4학년이면서 상태가 '휴면'인 회원만 삭제하고, 4학년이어도 활동 중이거나 휴면이어도 4학년이 아니면 남김

## 질문
내 이해가 맞는지 봐 주고, 필요한 구문과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · INSERT · UPDATE · DELETE · 트랜잭션(START TRANSACTION · COMMIT · ROLLBACK) 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 두 조건을 `OR`로 이어 4학년이거나 휴면인 회원이 모두 삭제됨

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
4학년이면서 상태가 '휴면'인 회원만 삭제하려고 해.
LAB05_MEMBER 테이블 구조:
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| MEMBER_ID | int(11)     | NO   | PRI | NULL    | auto_increment |
| NAME      | varchar(20) | NO   |     | NULL    |                |
| GRADE     | int(11)     | NO   |     | NULL    |                |
| PHONE     | varchar(15) | YES  |     | NULL    |                |
| STATUS    | varchar(10) | NO   |     | NULL    |                |
| CLUB_ID   | int(11)     | NO   | MUL | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```sql
DELETE FROM LAB05_MEMBER
WHERE GRADE = 4 OR STATUS = '휴면';

SELECT * FROM LAB05_MEMBER WHERE GRADE = 4 OR STATUS = '휴면' ORDER BY MEMBER_ID;
```
- 기대한 결과: 2행: (4, 최지우, 4, 010-4444-5555, 활동, 2) / (6, 강하은, 3, 010-6666-7777, 휴면, 3)
- 실제 결과: 0행. 회원 8명 중 4명이 삭제되어 4명만 남음

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 5. 축구부를 풋살부로 합치기

- Level 2 · 직접 만든 문제 · 트랜잭션

### 정답 SQL

```sql
START TRANSACTION;

UPDATE LAB05_MEMBER SET CLUB_ID = 4 WHERE CLUB_ID = 3;
DELETE FROM LAB05_CLUB WHERE CLUB_ID = 3;

SELECT * FROM LAB05_CLUB WHERE CLUB_ID IN (3, 4);
SELECT MEMBER_ID, NAME, CLUB_ID FROM LAB05_MEMBER WHERE CLUB_ID IN (3, 4) ORDER BY MEMBER_ID;

COMMIT;

SELECT * FROM LAB05_CLUB WHERE CLUB_ID IN (3, 4);
SELECT MEMBER_ID, NAME, CLUB_ID FROM LAB05_MEMBER WHERE CLUB_ID IN (3, 4) ORDER BY MEMBER_ID;
```

- 확인 결과: COMMIT 전후 모두 동아리 1행 · 회원 3행

```text
+---------+-----------+------------------+------+
| CLUB_ID | CLUB_NAME | ROOM             | FEE  |
+---------+-----------+------------------+------+
|       4 | 풋살부    | 체육관 102호     | 8000 |
+---------+-----------+------------------+------+
+-----------+-----------+---------+
| MEMBER_ID | NAME      | CLUB_ID |
+-----------+-----------+---------+
|         5 | 정예준    |       4 |
|         6 | 강하은    |       4 |
|         8 | 한지민    |       4 |
+-----------+-----------+---------+
```

- 풀이 핵심: 축구부를 참조하는 회원을 먼저 옮겨야 축구부를 삭제할 수 있음. 두 문장을 `START TRANSACTION`으로 묶고, `SELECT`로 확인한 뒤 이상이 없을 때만 `COMMIT`함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
LAB05_CLUB 테이블 구조:
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| CLUB_ID   | int(11)     | NO   | PRI | NULL    |       |
| CLUB_NAME | varchar(30) | NO   |     | NULL    |       |
| ROOM      | varchar(30) | NO   |     | NULL    |       |
| FEE       | int(11)     | NO   |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
LAB05_MEMBER 테이블 구조:
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| MEMBER_ID | int(11)     | NO   | PRI | NULL    | auto_increment |
| NAME      | varchar(20) | NO   |     | NULL    |                |
| GRADE     | int(11)     | NO   |     | NULL    |                |
| PHONE     | varchar(15) | YES  |     | NULL    |                |
| STATUS    | varchar(10) | NO   |     | NULL    |                |
| CLUB_ID   | int(11)     | NO   | MUL | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
- LAB05_CLUB 컬럼 뜻: 동아리 번호 · 동아리 이름 · 동아리방 · 월 회비(원)
- LAB05_MEMBER 컬럼 뜻: 회원 번호 · 이름 · 학년 · 연락처 · 활동 상태 · 소속 동아리 번호(LAB05_CLUB의 CLUB_ID를 참조하는 참조키)
- 내가 이해한 문제: 축구부(3번) 회원을 모두 풋살부(4번)로 옮기고 축구부를 삭제하는 두 작업을 하나의 트랜잭션으로 묶음. 결과를 확인해 이상이 없으면 COMMIT, 이상이 있으면 ROLLBACK

## 질문
내 이해가 맞는지 봐 주고, 필요한 구문과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · INSERT · UPDATE · DELETE · 트랜잭션(START TRANSACTION · COMMIT · ROLLBACK) 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 축구부를 먼저 삭제하려다 에러가 났는데, 확인하지 않고 회원 이동과 `COMMIT`까지 실행함. 회원만 옮겨지고 축구부는 남음

````md
## 맥락
SQL 데이터 입력 · 수정 · 삭제를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
축구부(3번) 회원을 모두 풋살부(4번)로 옮기고 축구부를 삭제하는 두 작업을 하나의 트랜잭션으로 묶으려고 해.
LAB05_CLUB 테이블 구조:
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| CLUB_ID   | int(11)     | NO   | PRI | NULL    |       |
| CLUB_NAME | varchar(30) | NO   |     | NULL    |       |
| ROOM      | varchar(30) | NO   |     | NULL    |       |
| FEE       | int(11)     | NO   |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
LAB05_MEMBER 테이블 구조:
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| MEMBER_ID | int(11)     | NO   | PRI | NULL    | auto_increment |
| NAME      | varchar(20) | NO   |     | NULL    |                |
| GRADE     | int(11)     | NO   |     | NULL    |                |
| PHONE     | varchar(15) | YES  |     | NULL    |                |
| STATUS    | varchar(10) | NO   |     | NULL    |                |
| CLUB_ID   | int(11)     | NO   | MUL | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```sql
START TRANSACTION;
DELETE FROM LAB05_CLUB WHERE CLUB_ID = 3;
UPDATE LAB05_MEMBER SET CLUB_ID = 4 WHERE CLUB_ID = 3;
COMMIT;

SELECT * FROM LAB05_CLUB WHERE CLUB_ID IN (3, 4);
SELECT MEMBER_ID, NAME, CLUB_ID FROM LAB05_MEMBER WHERE CLUB_ID IN (3, 4) ORDER BY MEMBER_ID;
```
- 기대한 결과: 동아리 1행 (4, 풋살부, 체육관 102호, 8000) · 회원 3행 (5, 정예준, 4) / (6, 강하은, 4) / (8, 한지민, 4)
- 실제 결과: DELETE에서 ERROR 1451 (23000): Cannot delete or update a parent row: a foreign key constraint fails (`myschool`.`lab05_member`, CONSTRAINT `lab05_member_ibfk_1` FOREIGN KEY (`CLUB_ID`) REFERENCES `LAB05_CLUB` (`CLUB_ID`)). COMMIT 뒤 동아리 2행 (3, 축구부, 운동장 클럽하우스, 10000) / (4, 풋살부, 체육관 102호, 8000) · 회원 3행 (5, 정예준, 4) / (6, 강하은, 4) / (8, 한지민, 4)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

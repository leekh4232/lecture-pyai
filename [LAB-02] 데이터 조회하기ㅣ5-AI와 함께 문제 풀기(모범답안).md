# [LAB-02] AI와 함께 문제 풀기 모범답안

「[LAB-02] 데이터 조회하기ㅣ5-AI와 함께 문제 풀기(AI 학습활동)」 덱의 문제 16개에 대한 정답 SQL과, 두 템플릿(방향 묻기 · 원인 묻기)을 빈칸 없이 채운 프롬프트를 담았다.

## 문제 1. 특정 옵션이 포함된 자동차 리스트 구하기

- Level 1 · 프로그래머스 157343 · https://school.programmers.co.kr/learn/courses/30/lessons/157343

### 정답 SQL

```sql
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC;
```

- 결과: 3행
- 풀이 핵심: OPTIONS는 여러 옵션이 콤마로 이어진 문자열이라 `=`가 아니라 `LIKE '%네비게이션%'`로 값의 일부를 찾음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
CAR_RENTAL_COMPANY_CAR 테이블 구조:
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| CAR_ID    | int(11)      | NO   | PRI | NULL    |       |
| CAR_TYPE  | varchar(255) | NO   |     | NULL    |       |
| DAILY_FEE | int(11)      | NO   |     | NULL    |       |
| OPTIONS   | varchar(255) | NO   |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
- 컬럼 뜻: 자동차 ID · 자동차 종류 · 일일 대여 요금(원) · 옵션 목록(콤마로 구분)
- 내가 이해한 문제: 옵션에 네비게이션이 있는 자동차를 ID가 큰 순서로 전부 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `=`로 비교해 옵션이 하나뿐인 행만 나옴

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
옵션에 네비게이션이 있는 자동차를 ID가 큰 순서로 조회하려고 해.
CAR_RENTAL_COMPANY_CAR 테이블 구조:
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| CAR_ID    | int(11)      | NO   | PRI | NULL    |       |
| CAR_TYPE  | varchar(255) | NO   |     | NULL    |       |
| DAILY_FEE | int(11)      | NO   |     | NULL    |       |
| OPTIONS   | varchar(255) | NO   |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
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

## 문제 2. 여러 기준으로 정렬하기

- Level 1 · 프로그래머스 59404 · https://school.programmers.co.kr/learn/courses/30/lessons/59404

### 정답 SQL

```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```

- 결과: 100행
- 풀이 핵심: 정렬 기준을 쉼표로 이어 쓰고, 방향은 기준마다 따로 정함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 모든 동물의 아이디 · 이름 · 보호 시작일을 이름 순으로 조회. 이름이 같으면 보호를 나중에 시작한 동물이 먼저

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 두 번째 기준의 `DESC`를 빠뜨림. 이름이 같은 행에서만 차이가 남

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
모든 동물의 아이디 · 이름 · 보호 시작일을 이름 순으로 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME;
```
- 기대한 결과: 100행, 53번째 행부터: (A377750, Lucy, 2017-10-25 17:17:00) / (A400680, Lucy, 2017-06-17 13:29:00) …
- 실제 결과: 100행, 53번째 행부터: (A399421, Lucy, 2015-08-25 14:08:00) / (A400680, Lucy, 2017-06-17 13:29:00) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 3. 인기있는 아이스크림

- Level 1 · 프로그래머스 133024 · https://school.programmers.co.kr/learn/courses/30/lessons/133024

### 정답 SQL

```sql
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID;
```

- 결과: 7행
- 풀이 핵심: 첫 기준은 내림차순, 둘째 기준은 오름차순

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
FIRST_HALF 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| SHIPMENT_ID | int(11)      | NO   |     | NULL    |       |
| FLAVOR      | varchar(300) | NO   | PRI | NULL    |       |
| TOTAL_ORDER | int(11)      | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
- 컬럼 뜻: 출하 번호 · 아이스크림 맛 · 상반기 총주문량
- 내가 이해한 문제: 아이스크림 맛을 총주문량이 많은 순서로 조회. 총주문량이 같으면 출하 번호가 작은 순서

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 첫 기준의 `DESC`를 빠뜨림

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
아이스크림 맛을 총주문량이 많은 순서로 조회하려고 해.
FIRST_HALF 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| SHIPMENT_ID | int(11)      | NO   |     | NULL    |       |
| FLAVOR      | varchar(300) | NO   | PRI | NULL    |       |
| TOTAL_ORDER | int(11)      | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
```sql
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER, SHIPMENT_ID;
```
- 기대한 결과: 7행, 앞 2행: (chocolate) / (white_chocolate) …
- 실제 결과: 7행, 앞 2행: (mint_chocolate) / (peach) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 4. 상위 n개 레코드

- Level 1 · 프로그래머스 59405 · https://school.programmers.co.kr/learn/courses/30/lessons/59405

### 정답 SQL

```sql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 0, 1;
```

- 결과: 1행
- 풀이 핵심: 보호 시작일 오름차순으로 정렬한 뒤 맨 위 한 행만 `LIMIT 0, 1`로 남김

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 보호소에 가장 먼저 들어온 동물 한 마리의 이름을 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 정렬 방향을 반대로 써 가장 늦게 들어온 동물이 나옴

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
보호소에 가장 먼저 들어온 동물 한 마리의 이름을 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 0, 1;
```
- 기대한 결과: 1행 (Jack)
- 실제 결과: 1행 (Stormy)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 5. 최댓값 구하기

- Level 1 · 프로그래머스 59415 · https://school.programmers.co.kr/learn/courses/30/lessons/59415

### 정답 SQL

```sql
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 0, 1;
```

- 결과: 1행
- 풀이 핵심: 보호 시작일 내림차순의 첫 행. 정답 파일은 `MAX`를 쓰지만 이 단원 범위에서는 정렬과 `LIMIT`으로 품

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 가장 최근에 들어온 동물의 보호 시작일 하나를 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 정렬 방향을 반대로 써 가장 오래된 날짜가 나옴

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
가장 최근에 들어온 동물의 보호 시작일 하나를 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 0, 1;
```
- 기대한 결과: 1행 (2018-02-03 10:40:00)
- 실제 결과: 1행 (2013-10-14 15:38:00)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 6. 가장 비싼 상품 구하기

- Level 1 · 프로그래머스 131697 · https://school.programmers.co.kr/learn/courses/30/lessons/131697

### 정답 SQL

```sql
SELECT PRICE AS MAX_PRICE
FROM PRODUCT
ORDER BY PRICE DESC
LIMIT 0, 1;
```

- 결과: 1행
- 풀이 핵심: 판매가 내림차순의 첫 행에 별칭 `MAX_PRICE`를 붙임. 정답 파일은 `MAX`를 씀

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
PRODUCT 테이블 구조:
+--------------+---------+------+-----+---------+-------+
| Field        | Type    | Null | Key | Default | Extra |
+--------------+---------+------+-----+---------+-------+
| PRODUCT_ID   | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_CODE | char(8) | NO   | UNI | NULL    |       |
| PRICE        | int(11) | NO   |     | NULL    |       |
+--------------+---------+------+-----+---------+-------+
- 컬럼 뜻: 상품 ID · 상품코드 · 판매가
- 내가 이해한 문제: 가장 높은 판매가 하나를 MAX_PRICE라는 컬럼 이름으로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `ORDER BY`를 빠뜨려 저장된 순서의 첫 행이 나옴

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
가장 높은 판매가 하나를 MAX_PRICE라는 컬럼 이름으로 조회하려고 해.
PRODUCT 테이블 구조:
+--------------+---------+------+-----+---------+-------+
| Field        | Type    | Null | Key | Default | Extra |
+--------------+---------+------+-----+---------+-------+
| PRODUCT_ID   | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_CODE | char(8) | NO   | UNI | NULL    |       |
| PRICE        | int(11) | NO   |     | NULL    |       |
+--------------+---------+------+-----+---------+-------+
```sql
SELECT PRICE AS MAX_PRICE
FROM PRODUCT
LIMIT 0, 1;
```
- 기대한 결과: 1행 (85000)
- 실제 결과: 1행 (72000)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 7. 아픈 동물 찾기

- Level 1 · 프로그래머스 59036 · https://school.programmers.co.kr/learn/courses/30/lessons/59036

### 정답 SQL

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID;
```

- 결과: 6행
- 풀이 핵심: 문자 값은 작은따옴표로 감싸 비교함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 보호 시작 시 상태가 Sick인 동물의 아이디와 이름을 아이디 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 문자 값의 작은따옴표를 빠뜨려 에러가 남

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
보호 시작 시 상태가 Sick인 동물의 아이디와 이름을 아이디 순서로 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = Sick
ORDER BY ANIMAL_ID;
```
- 기대한 결과: 6행, 앞 2행: (A362707, Girly Girl) / (A367012, Miller) …
- 실제 결과: ERROR 1054 (42S22): Unknown column 'Sick' in 'WHERE'

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 8. 어린 동물 찾기

- Level 1 · 프로그래머스 59037 · https://school.programmers.co.kr/learn/courses/30/lessons/59037

### 정답 SQL

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID;
```

- 결과: 93행
- 풀이 핵심: '아닌' 조건은 `!=`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 보호 시작 시 상태가 Aged가 아닌 동물의 아이디와 이름을 아이디 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 조건을 반대로 써 늙은 동물만 나옴

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
보호 시작 시 상태가 Aged가 아닌 동물의 아이디와 이름을 아이디 순서로 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Aged'
ORDER BY ANIMAL_ID;
```
- 기대한 결과: 93행, 앞 2행: (A349996, Sugar) / (A350276, Jewel) …
- 실제 결과: 7행, 앞 2행: (A352872, Peanutbutter) / (A365302, Minnie) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 9. 이름이 없는 동물의 아이디

- Level 1 · 프로그래머스 59039 · https://school.programmers.co.kr/learn/courses/30/lessons/59039

### 정답 SQL

```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL
ORDER BY ANIMAL_ID;
```

- 결과: 1행
- 풀이 핵심: NULL은 `=`로 비교할 수 없고 `IS NULL`로 찾음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 이름이 비어 있는(NULL) 동물의 아이디를 아이디 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: NULL을 `=`로 비교해 결과가 비어 있음

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
이름이 비어 있는(NULL) 동물의 아이디를 아이디 순서로 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME = NULL
ORDER BY ANIMAL_ID;
```
- 기대한 결과: 1행 (A368930)
- 실제 결과: 0행 (결과가 비어 있음)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 10. 이름이 있는 동물의 아이디

- Level 1 · 프로그래머스 59407 · https://school.programmers.co.kr/learn/courses/30/lessons/59407

### 정답 SQL

```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID;
```

- 결과: 99행
- 풀이 핵심: NULL이 아닌 행은 `IS NOT NULL`로 찾음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 이름이 있는(NULL이 아닌) 동물의 아이디를 아이디 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: NULL을 `!=`로 비교해 결과가 비어 있음

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
이름이 있는(NULL이 아닌) 동물의 아이디를 아이디 순서로 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME != NULL
ORDER BY ANIMAL_ID;
```
- 기대한 결과: 99행, 앞 2행: (A349996) / (A350276) …
- 실제 결과: 0행 (결과가 비어 있음)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 11. 강원도에 위치한 생산공장 목록 출력하기

- Level 1 · 프로그래머스 131112 · https://school.programmers.co.kr/learn/courses/30/lessons/131112

### 정답 SQL

```sql
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID;
```

- 결과: 3행
- 풀이 핵심: '~로 시작'은 `LIKE '강원도%'`. `%`는 뒤에 어떤 글자가 와도 된다는 뜻

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
FOOD_FACTORY 테이블 구조:
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| FACTORY_ID   | varchar(10)  | NO   | PRI | NULL    |       |
| FACTORY_NAME | varchar(50)  | NO   |     | NULL    |       |
| ADDRESS      | varchar(100) | YES  |     | NULL    |       |
| TLNO         | varchar(20)  | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
- 컬럼 뜻: 공장 ID · 공장 이름 · 주소 · 전화번호
- 내가 이해한 문제: 주소가 강원도로 시작하는 공장의 ID · 이름 · 주소를 공장 ID 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `%`를 빠뜨려 주소 전체가 '강원도'인 행만 찾음

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
주소가 강원도로 시작하는 공장의 ID · 이름 · 주소를 공장 ID 순서로 조회하려고 해.
FOOD_FACTORY 테이블 구조:
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| FACTORY_ID   | varchar(10)  | NO   | PRI | NULL    |       |
| FACTORY_NAME | varchar(50)  | NO   |     | NULL    |       |
| ADDRESS      | varchar(100) | YES  |     | NULL    |       |
| TLNO         | varchar(20)  | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
```sql
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도'
ORDER BY FACTORY_ID;
```
- 기대한 결과: 3행, 앞 2행: (FT19980003, (주)맛있는라면, 강원도 정선군 남면 칠현로 679) / (FT20100003, (주)맛있는음료, 강원도 원주시 문막읍 문막공단길 154) …
- 실제 결과: 0행 (결과가 비어 있음)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 12. Python 개발자 찾기

- Level 1 · 프로그래머스 276013 · https://school.programmers.co.kr/learn/courses/30/lessons/276013

### 정답 SQL

```sql
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE SKILL_1 = 'Python'
   OR SKILL_2 = 'Python'
   OR SKILL_3 = 'Python'
ORDER BY ID;
```

- 결과: 2행
- 풀이 핵심: 스킬 컬럼 세 개를 `OR`로 이어 비교함. 정답 파일은 `'Python' IN (SKILL_1, SKILL_2, SKILL_3)`으로 같은 결과를 냄

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
DEVELOPER_INFOS 테이블 구조:
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| ID         | varchar(10) | YES  | UNI | NULL    |       |
| FIRST_NAME | varchar(10) | YES  |     | NULL    |       |
| LAST_NAME  | varchar(10) | YES  |     | NULL    |       |
| EMAIL      | varchar(32) | YES  | UNI | NULL    |       |
| SKILL_1    | varchar(10) | YES  |     | NULL    |       |
| SKILL_2    | varchar(10) | YES  |     | NULL    |       |
| SKILL_3    | varchar(10) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: ID · 이름 · 성 · 이메일 · 첫 번째 스킬 · 두 번째 스킬 · 세 번째 스킬
- 내가 이해한 문제: 스킬 세 칸 중 하나라도 Python인 개발자의 ID · 이메일 · 이름 · 성을 ID 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 첫 번째 스킬만 비교해 두 번째 · 세 번째 스킬이 Python인 개발자가 빠짐

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
스킬 세 칸 중 하나라도 Python인 개발자의 ID · 이메일 · 이름 · 성을 ID 순서로 조회하려고 해.
DEVELOPER_INFOS 테이블 구조:
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| ID         | varchar(10) | YES  | UNI | NULL    |       |
| FIRST_NAME | varchar(10) | YES  |     | NULL    |       |
| LAST_NAME  | varchar(10) | YES  |     | NULL    |       |
| EMAIL      | varchar(32) | YES  | UNI | NULL    |       |
| SKILL_1    | varchar(10) | YES  |     | NULL    |       |
| SKILL_2    | varchar(10) | YES  |     | NULL    |       |
| SKILL_3    | varchar(10) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+
```sql
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE SKILL_1 = 'Python'
ORDER BY ID;
```
- 기대한 결과: 2행 (D162, cade_cunningham@grepp.co, Cade, Cunningham) / (D165, jerami_edwards@grepp.co, Jerami, Edwards)
- 실제 결과: 0행 (결과가 비어 있음)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 13. 최솟값 구하기

- Level 2 · 프로그래머스 59038 · https://school.programmers.co.kr/learn/courses/30/lessons/59038

### 정답 SQL

```sql
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 0, 1;
```

- 결과: 1행
- 풀이 핵심: 보호 시작일 오름차순의 첫 행. 정답 파일은 `MIN`을 씀

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 가장 먼저 들어온 동물의 보호 시작일 하나를 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 정렬 방향을 반대로 써 가장 최근 날짜가 나옴

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
가장 먼저 들어온 동물의 보호 시작일 하나를 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 0, 1;
```
- 기대한 결과: 1행 (2013-10-14 15:38:00)
- 실제 결과: 1행 (2018-02-03 10:40:00)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 14. 가격이 제일 비싼 식품의 정보 출력하기

- Level 2 · 프로그래머스 131115 · https://school.programmers.co.kr/learn/courses/30/lessons/131115

### 정답 SQL

```sql
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 0, 1;
```

- 결과: 1행
- 풀이 핵심: 가격 내림차순으로 정렬한 뒤 `LIMIT 0, 1`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
FOOD_PRODUCT 테이블 구조:
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| PRODUCT_ID   | varchar(10) | NO   | PRI | NULL    |       |
| PRODUCT_NAME | varchar(50) | NO   | PRI | NULL    |       |
| PRODUCT_CD   | varchar(10) | YES  |     | NULL    |       |
| CATEGORY     | varchar(10) | YES  |     | NULL    |       |
| PRICE        | int(11)     | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 식품 ID · 식품 이름 · 식품 코드 · 식품분류 · 식품 가격
- 내가 이해한 문제: 가격이 가장 비싼 식품 하나의 ID · 이름 · 코드 · 분류 · 가격을 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 정렬 방향을 반대로 써 가장 싼 식품이 나옴

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
가격이 가장 비싼 식품 하나의 ID · 이름 · 코드 · 분류 · 가격을 조회하려고 해.
FOOD_PRODUCT 테이블 구조:
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| PRODUCT_ID   | varchar(10) | NO   | PRI | NULL    |       |
| PRODUCT_NAME | varchar(50) | NO   | PRI | NULL    |       |
| PRODUCT_CD   | varchar(10) | YES  |     | NULL    |       |
| CATEGORY     | varchar(10) | YES  |     | NULL    |       |
| PRICE        | int(11)     | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
```sql
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE
LIMIT 0, 1;
```
- 기대한 결과: 1행 (P0051, 맛있는배추김치, CD_KC00001, 김치, 19000)
- 실제 결과: 1행 (P0061, 맛있는생수, CD_BR00001, 음료, 1100)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 15. 루시와 엘라 찾기

- Level 2 · 프로그래머스 59046 · https://school.programmers.co.kr/learn/courses/30/lessons/59046

### 정답 SQL

```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;
```

- 결과: 8행
- 풀이 핵심: 여러 값 중 하나와 같은지는 `IN (…)`으로 한 번에 비교함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 이름이 Lucy · Ella · Pickle · Rogan · Sabrina · Mitty 중 하나인 동물의 아이디 · 이름 · 성별 및 중성화 여부를 아이디 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `OR` 뒤에 `NAME =`을 빠뜨려 Lucy만 나옴. 에러 없이 틀린 결과가 나와 찾기 어려운 실수

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
이름이 Lucy · Ella · Pickle · Rogan · Sabrina · Mitty 중 하나인 동물의 아이디 · 이름 · 성별 및 중성화 여부를 아이디 순서로 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME = 'Lucy' OR 'Ella' OR 'Pickle'
   OR 'Rogan' OR 'Sabrina' OR 'Mitty'
ORDER BY ANIMAL_ID;
```
- 기대한 결과: 8행, 앞 2행: (A373219, Ella, Spayed Female) / (A377750, Lucy, Spayed Female) …
- 실제 결과: 3행, 앞 2행: (A377750, Lucy, Spayed Female) / (A399421, Lucy, Spayed Female) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 16. 이름에 el이 들어가는 동물 찾기

- Level 2 · 프로그래머스 59047 · https://school.programmers.co.kr/learn/courses/30/lessons/59047

### 정답 SQL

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog'
  AND NAME LIKE '%el%'
ORDER BY NAME, ANIMAL_ID;
```

- 결과: 4행
- 풀이 핵심: 두 조건을 `AND`로 묶음. 수업용 DB는 대소문자를 구분하지 않아 `LIKE '%el%'`가 'El'도 찾음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 개 중에서 이름에 el이 들어가는(대소문자 구분 없음) 동물의 아이디와 이름을 이름 순으로 조회. 이름이 같으면 아이디 순서

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · 별칭 · WHERE · 검색 연산자 · ORDER BY · LIMIT 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 개 조건을 빠뜨려 고양이까지 나옴

````md
## 맥락
SQL 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
개 중에서 이름에 el이 들어가는(대소문자 구분 없음) 동물의 아이디와 이름을 이름 순으로 조회하려고 해.
ANIMAL_INS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| INTAKE_CONDITION | varchar(7)  | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_INTAKE  | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%'
ORDER BY NAME, ANIMAL_ID;
```
- 기대한 결과: 4행, 앞 2행: (A355753, Elijah) / (A382192, Maxwell 2) …
- 실제 결과: 7행, 앞 2행: (A354597, Ariel) / (A355753, Elijah) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

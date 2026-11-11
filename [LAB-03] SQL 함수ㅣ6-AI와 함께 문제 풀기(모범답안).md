# [LAB-03] SQL 함수ㅣ6-AI와 함께 문제 풀기 모범답안

「[LAB-03] SQL 함수ㅣ6-AI와 함께 문제 풀기(AI 학습활동)」 덱의 문제 14개에 대한 정답 SQL과, 두 템플릿(방향 묻기 · 원인 묻기)을 빈칸 없이 채운 프롬프트를 담았다.

## 문제 1. 나이 정보가 없는 회원 수 구하기

- Level 1 · 프로그래머스 131528 · https://school.programmers.co.kr/learn/courses/30/lessons/131528

### 정답 SQL

```sql
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;
```

- 결과: 1행
- 풀이 핵심: NULL인 행을 `IS NULL`로 거른 뒤 `COUNT(*)`로 행 수를 셈

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
USER_INFO 테이블 구조:
+---------+------------+------+-----+---------+-------+
| Field   | Type       | Null | Key | Default | Extra |
+---------+------------+------+-----+---------+-------+
| USER_ID | int(11)    | NO   | PRI | NULL    |       |
| GENDER  | tinyint(1) | YES  |     | NULL    |       |
| AGE     | int(11)    | YES  |     | NULL    |       |
| JOINED  | date       | NO   |     | NULL    |       |
+---------+------------+------+-----+---------+-------+
- 컬럼 뜻: 회원 ID · 성별(0 남자, 1 여자, 비어 있을 수 있음) · 나이 · 가입일
- 내가 이해한 문제: 나이가 비어 있는(NULL) 회원이 몇 명인지 USERS라는 컬럼 이름으로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `COUNT(AGE)`로 세어 0이 나옴. `COUNT(컬럼)`은 NULL을 세지 않음

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
나이가 비어 있는(NULL) 회원이 몇 명인지 USERS라는 컬럼 이름으로 조회하려고 해.
USER_INFO 테이블 구조:
+---------+------------+------+-----+---------+-------+
| Field   | Type       | Null | Key | Default | Extra |
+---------+------------+------+-----+---------+-------+
| USER_ID | int(11)    | NO   | PRI | NULL    |       |
| GENDER  | tinyint(1) | YES  |     | NULL    |       |
| AGE     | int(11)    | YES  |     | NULL    |       |
| JOINED  | date       | NO   |     | NULL    |       |
+---------+------------+------+-----+---------+-------+
```sql
SELECT COUNT(AGE) AS USERS
FROM USER_INFO
WHERE AGE IS NULL;
```
- 기대한 결과: 1행 (4)
- 실제 결과: 1행 (0)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 2. 평균 일일 대여 요금 구하기

- Level 1 · 프로그래머스 151136 · https://school.programmers.co.kr/learn/courses/30/lessons/151136

### 정답 SQL

```sql
SELECT ROUND(AVG(DAILY_FEE)) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';
```

- 결과: 1행
- 풀이 핵심: `AVG`로 평균을 내고 `ROUND`로 정수가 되게 반올림함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: SUV의 평균 일일 대여 요금을 소수 첫째 자리에서 반올림해 AVERAGE_FEE라는 컬럼 이름으로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `ROUND`를 빠뜨려 소수점 아래가 그대로 나옴

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
SUV의 평균 일일 대여 요금을 소수 첫째 자리에서 반올림해 AVERAGE_FEE라는 컬럼 이름으로 조회하려고 해.
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
SELECT AVG(DAILY_FEE) AS AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE CAR_TYPE = 'SUV';
```
- 기대한 결과: 1행 (93727)
- 실제 결과: 1행 (93727.2727)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 3. 경기도에 위치한 식품창고 목록 출력하기

- Level 1 · 프로그래머스 131114 · https://school.programmers.co.kr/learn/courses/30/lessons/131114

### 정답 SQL

```sql
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID;
```

- 결과: 5행
- 풀이 핵심: NULL을 다른 값으로 바꿀 때는 `IFNULL(컬럼, 대신할 값)`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
FOOD_WAREHOUSE 테이블 구조:
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| WAREHOUSE_ID   | varchar(10)  | NO   | PRI | NULL    |       |
| WAREHOUSE_NAME | varchar(20)  | NO   | UNI | NULL    |       |
| ADDRESS        | varchar(100) | YES  |     | NULL    |       |
| TLNO           | varchar(20)  | YES  |     | NULL    |       |
| FREEZER_YN     | varchar(1)   | YES  |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
- 컬럼 뜻: 창고 ID · 창고 이름 · 창고 주소 · 전화번호 · 냉동시설 여부
- 내가 이해한 문제: 주소가 경기도로 시작하는 창고의 ID · 이름 · 주소 · 냉동시설 여부를 창고 ID 순서로 조회. 냉동시설 여부가 NULL이면 N으로 표시

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `IFNULL`을 빠뜨려 NULL이 그대로 나옴

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
주소가 경기도로 시작하는 창고의 ID · 이름 · 주소 · 냉동시설 여부를 창고 ID 순서로 조회하려고 해.
FOOD_WAREHOUSE 테이블 구조:
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| WAREHOUSE_ID   | varchar(10)  | NO   | PRI | NULL    |       |
| WAREHOUSE_NAME | varchar(20)  | NO   | UNI | NULL    |       |
| ADDRESS        | varchar(100) | YES  |     | NULL    |       |
| TLNO           | varchar(20)  | YES  |     | NULL    |       |
| FREEZER_YN     | varchar(1)   | YES  |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
```sql
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID;
```
- 기대한 결과: 5행, 2번째 행부터: (WH0003, 창고_경기2, 경기도 이천시 마장면 덕평로 811, N) / (WH0004, 창고_경기3, 경기도 김포시 대곶면 율생중앙로205번길, N) …
- 실제 결과: 5행, 2번째 행부터: (WH0003, 창고_경기2, 경기도 이천시 마장면 덕평로 811, NULL) / (WH0004, 창고_경기3, 경기도 김포시 대곶면 율생중앙로205번길, N) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 4. 12세 이하인 여자 환자 목록 출력하기

- Level 1 · 프로그래머스 132201 · https://school.programmers.co.kr/learn/courses/30/lessons/132201

### 정답 SQL

```sql
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME;
```

- 결과: 5행
- 풀이 핵심: 조건 두 개는 `AND`, 전화번호는 `IFNULL(TLNO, 'NONE')`, 정렬은 나이 내림차순 + 이름 오름차순

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
PATIENT 테이블 구조:
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| PT_NO   | varchar(10) | NO   | PRI | NULL    |       |
| PT_NAME | varchar(20) | YES  |     | NULL    |       |
| GEND_CD | varchar(1)  | YES  |     | NULL    |       |
| AGE     | int(11)     | YES  |     | NULL    |       |
| TLNO    | varchar(50) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 환자번호 · 환자이름 · 성별코드 · 나이 · 전화번호
- 내가 이해한 문제: 12세 이하 여자 환자의 이름 · 번호 · 성별코드 · 나이 · 전화번호를 나이 많은 순, 같으면 이름 순으로 조회. 전화번호가 없으면 NONE

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 나이 정렬의 `DESC`를 빠뜨림

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
12세 이하 여자 환자의 이름 · 번호 · 성별코드 · 나이 · 전화번호를 나이 많은 순, 같으면 이름 순으로 조회하려고 해.
PATIENT 테이블 구조:
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| PT_NO   | varchar(10) | NO   | PRI | NULL    |       |
| PT_NAME | varchar(20) | YES  |     | NULL    |       |
| GEND_CD | varchar(1)  | YES  |     | NULL    |       |
| AGE     | int(11)     | YES  |     | NULL    |       |
| TLNO    | varchar(50) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
```sql
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE, PT_NAME;
```
- 기대한 결과: 5행, 앞 2행: (한나, PT22000009, W, 12, 01032323117) / (안나, PT22000018, W, 11, NONE) …
- 실제 결과: 5행, 앞 2행: (뽀뽀, PT22000006, W, 8, NONE) / (스티치, PT22000022, W, 9, NONE) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 5. 흉부외과 또는 일반외과 의사 목록 출력하기

- Level 1 · 프로그래머스 132203 · https://school.programmers.co.kr/learn/courses/30/lessons/132203

### 정답 SQL

```sql
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')
ORDER BY HIRE_YMD DESC, DR_NAME;
```

- 결과: 7행
- 풀이 핵심: 두 값 중 하나는 `IN ('CS', 'GS')`, 날짜는 `DATE_FORMAT(…, '%Y-%m-%d')`로 모양을 맞춤

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
DOCTOR 테이블 구조:
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| DR_NAME  | varchar(20) | NO   | PRI | NULL    |       |
| DR_ID    | varchar(10) | NO   | PRI | NULL    |       |
| LCNS_NO  | varchar(30) | YES  |     | NULL    |       |
| HIRE_YMD | date        | YES  |     | NULL    |       |
| MCDP_CD  | varchar(6)  | YES  |     | NULL    |       |
| TLNO     | varchar(50) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 의사이름 · 의사ID · 면허번호 · 고용일자 · 진료과코드 · 전화번호
- 내가 이해한 문제: 진료과가 CS이거나 GS인 의사의 이름 · ID · 진료과 · 고용일자를 고용일자 최근 순, 같으면 이름 순으로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: '또는'을 `AND`로 써서 결과가 비어 있음. 한 행의 진료과가 CS이면서 GS일 수는 없음

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
진료과가 CS이거나 GS인 의사의 이름 · ID · 진료과 · 고용일자를 고용일자 최근 순, 같으면 이름 순으로 조회하려고 해.
DOCTOR 테이블 구조:
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| DR_NAME  | varchar(20) | NO   | PRI | NULL    |       |
| DR_ID    | varchar(10) | NO   | PRI | NULL    |       |
| LCNS_NO  | varchar(30) | YES  |     | NULL    |       |
| HIRE_YMD | date        | YES  |     | NULL    |       |
| MCDP_CD  | varchar(6)  | YES  |     | NULL    |       |
| TLNO     | varchar(50) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
```sql
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
FROM DOCTOR
WHERE MCDP_CD = 'CS' AND MCDP_CD = 'GS'
ORDER BY HIRE_YMD DESC, DR_NAME;
```
- 기대한 결과: 7행, 앞 2행: (니모, DR20200012, CS, 2020-03-01) / (윈더, DR20190029, CS, 2019-03-01) …
- 실제 결과: 0행 (결과가 비어 있음)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 6. 조건에 맞는 도서 리스트 출력하기

- Level 1 · 프로그래머스 144853 · https://school.programmers.co.kr/learn/courses/30/lessons/144853

### 정답 SQL

```sql
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = 2021
  AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE;
```

- 결과: 1행
- 풀이 핵심: 연도는 `YEAR(PUBLISHED_DATE) = 2021`, 두 조건은 `AND`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
BOOK 테이블 구조:
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| BOOK_ID        | int(11)      | NO   | PRI | NULL    |       |
| CATEGORY       | varchar(255) | NO   |     | NULL    |       |
| AUTHOR_ID      | int(11)      | NO   |     | NULL    |       |
| PRICE          | int(11)      | NO   |     | NULL    |       |
| PUBLISHED_DATE | date         | NO   |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
- 컬럼 뜻: 도서 ID · 카테고리 · 저자 ID · 판매가(원) · 출판일
- 내가 이해한 문제: 2021년에 출판된 인문 도서의 ID와 출판일을 출판일 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 두 조건을 `OR`로 이어 2021년 도서와 인문 도서가 모두 나옴

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
2021년에 출판된 인문 도서의 ID와 출판일을 출판일 순서로 조회하려고 해.
BOOK 테이블 구조:
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| BOOK_ID        | int(11)      | NO   | PRI | NULL    |       |
| CATEGORY       | varchar(255) | NO   |     | NULL    |       |
| AUTHOR_ID      | int(11)      | NO   |     | NULL    |       |
| PRICE          | int(11)      | NO   |     | NULL    |       |
| PUBLISHED_DATE | date         | NO   |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
```sql
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = 2021
   OR CATEGORY = '인문'
ORDER BY PUBLISHED_DATE;
```
- 기대한 결과: 1행 (3, 2021-10-24)
- 실제 결과: 3행, 앞 2행: (2, 2021-06-10) / (7, 2021-08-20) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 7. 자동차 대여 기록에서 장기/단기 대여 구분하기

- Level 1 · 프로그래머스 151138 · https://school.programmers.co.kr/learn/courses/30/lessons/151138

### 정답 SQL

```sql
SELECT HISTORY_ID, CAR_ID,
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       CASE WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여'
            ELSE '단기 대여' END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE >= '2022-09-01' AND START_DATE < '2022-10-01'
ORDER BY HISTORY_ID DESC;
```

- 결과: 61행
- 풀이 핵심: 대여 기간은 시작일과 종료일을 모두 세므로 `DATEDIFF(END_DATE, START_DATE) + 1`. 구분은 `CASE WHEN`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블 구조:
+------------+---------+------+-----+---------+-------+
| Field      | Type    | Null | Key | Default | Extra |
+------------+---------+------+-----+---------+-------+
| HISTORY_ID | int(11) | NO   | PRI | NULL    |       |
| CAR_ID     | int(11) | NO   |     | NULL    |       |
| START_DATE | date    | NO   |     | NULL    |       |
| END_DATE   | date    | NO   |     | NULL    |       |
+------------+---------+------+-----+---------+-------+
- 컬럼 뜻: 대여 기록 ID · 자동차 ID · 대여 시작일 · 대여 종료일
- 내가 이해한 문제: 대여 시작일이 2022년 9월인 기록을 대여 기간 30일 이상이면 장기 대여, 아니면 단기 대여로 표시해 기록 ID 큰 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `DATEDIFF`에 1을 더하지 않아 딱 30일 빌린 기록이 단기 대여로 나옴

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
대여 시작일이 2022년 9월인 기록을 대여 기간 30일 이상이면 장기 대여, 아니면 단기 대여로 표시해 기록 ID 큰 순서로 조회하려고 해.
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블 구조:
+------------+---------+------+-----+---------+-------+
| Field      | Type    | Null | Key | Default | Extra |
+------------+---------+------+-----+---------+-------+
| HISTORY_ID | int(11) | NO   | PRI | NULL    |       |
| CAR_ID     | int(11) | NO   |     | NULL    |       |
| START_DATE | date    | NO   |     | NULL    |       |
| END_DATE   | date    | NO   |     | NULL    |       |
+------------+---------+------+-----+---------+-------+
```sql
SELECT HISTORY_ID, CAR_ID,
       DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
       DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
       CASE WHEN DATEDIFF(END_DATE, START_DATE) >= 30 THEN '장기 대여'
            ELSE '단기 대여' END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE >= '2022-09-01' AND START_DATE < '2022-10-01'
ORDER BY HISTORY_ID DESC;
```
- 기대한 결과: 61행, 앞 2행: (669, 25, 2022-09-29, 2022-10-28, 장기 대여) / (668, 13, 2022-09-28, 2022-09-28, 단기 대여) …
- 실제 결과: 61행, 앞 2행: (669, 25, 2022-09-29, 2022-10-28, 단기 대여) / (668, 13, 2022-09-28, 2022-09-28, 단기 대여) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 8. 동물 수 구하기

- Level 2 · 프로그래머스 59406 · https://school.programmers.co.kr/learn/courses/30/lessons/59406

### 정답 SQL

```sql
SELECT COUNT(*) AS count
FROM ANIMAL_INS;
```

- 결과: 1행
- 풀이 핵심: 행 수는 `COUNT(*)`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 보호소에 들어온 동물이 모두 몇 마리인지 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `COUNT(NAME)`으로 세어 이름이 없는 동물이 빠짐

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
보호소에 들어온 동물이 모두 몇 마리인지 조회하려고 해.
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
SELECT COUNT(NAME) AS count
FROM ANIMAL_INS;
```
- 기대한 결과: 1행 (100)
- 실제 결과: 1행 (99)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 9. NULL 처리하기

- Level 2 · 프로그래머스 59410 · https://school.programmers.co.kr/learn/courses/30/lessons/59410

### 정답 SQL

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

- 결과: 100행
- 풀이 핵심: `IFNULL(NAME, 'No name')`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 모든 동물의 생물 종 · 이름 · 성별 및 중성화 여부를 아이디 순서로 조회. 이름이 없으면 No name으로 표시

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `IF`의 조건을 `NAME = NULL`로 써서 NULL이 그대로 나옴

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
모든 동물의 생물 종 · 이름 · 성별 및 중성화 여부를 아이디 순서로 조회하려고 해.
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
SELECT ANIMAL_TYPE, IF(NAME = NULL, 'No name', NAME) AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```
- 기대한 결과: 100행, 33번째 행부터: (Dog, No name, Spayed Female) / (Dog, Sniket, Neutered Male) …
- 실제 결과: 100행, 33번째 행부터: (Dog, NULL, Spayed Female) / (Dog, Sniket, Neutered Male) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 10. DATETIME에서 DATE로 형 변환

- Level 2 · 프로그래머스 59414 · https://school.programmers.co.kr/learn/courses/30/lessons/59414

### 정답 SQL

```sql
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

- 결과: 100행
- 풀이 핵심: `DATE_FORMAT(DATETIME, '%Y-%m-%d')`. 형식 문자는 대소문자에 따라 뜻이 다름

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 모든 동물의 아이디 · 이름 · 들어온 날짜(시각 없이 년-월-일)를 아이디 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 형식 문자를 대문자 `%M` · `%D`로 써서 월 이름과 서수가 나옴

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
모든 동물의 아이디 · 이름 · 들어온 날짜(시각 없이 년-월-일)를 아이디 순서로 조회하려고 해.
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
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%M-%D') AS 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```
- 기대한 결과: 100행, 앞 2행: (A349996, Sugar, 2018-01-22) / (A350276, Jewel, 2017-08-13) …
- 실제 결과: 100행, 앞 2행: (A349996, Sugar, 2018-January-22nd) / (A350276, Jewel, 2017-August-13th) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 11. 3월에 태어난 여성 회원 목록 출력하기

- Level 2 · 프로그래머스 131120 · https://school.programmers.co.kr/learn/courses/30/lessons/131120

### 정답 SQL

```sql
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3
  AND GENDER = 'W'
  AND TLNO IS NOT NULL
ORDER BY MEMBER_ID;
```

- 결과: 1행
- 풀이 핵심: 월은 `MONTH(DATE_OF_BIRTH) = 3`, 연락처가 없는 회원은 `TLNO IS NOT NULL`로 뺌

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
MEMBER_PROFILE 테이블 구조:
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| MEMBER_ID     | varchar(100) | NO   | PRI | NULL    |       |
| MEMBER_NAME   | varchar(50)  | YES  |     | NULL    |       |
| TLNO          | varchar(50)  | YES  |     | NULL    |       |
| GENDER        | varchar(1)   | YES  |     | NULL    |       |
| DATE_OF_BIRTH | date         | YES  |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+
- 컬럼 뜻: 회원 ID · 회원 이름 · 회원 연락처 · 성별 · 생년월일
- 내가 이해한 문제: 생일이 3월인 여성 회원 중 연락처가 있는 회원의 ID · 이름 · 성별 · 생년월일을 회원 ID 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 연락처가 NULL인 회원을 빼는 조건을 빠뜨림

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
생일이 3월인 여성 회원 중 연락처가 있는 회원의 ID · 이름 · 성별 · 생년월일을 회원 ID 순서로 조회하려고 해.
MEMBER_PROFILE 테이블 구조:
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| MEMBER_ID     | varchar(100) | NO   | PRI | NULL    |       |
| MEMBER_NAME   | varchar(50)  | YES  |     | NULL    |       |
| TLNO          | varchar(50)  | YES  |     | NULL    |       |
| GENDER        | varchar(1)   | YES  |     | NULL    |       |
| DATE_OF_BIRTH | date         | YES  |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+
```sql
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3
  AND GENDER = 'W'
ORDER BY MEMBER_ID;
```
- 기대한 결과: 1행 (seoyeons@naver.com, 박서연, W, 1992-03-16)
- 실제 결과: 2행 (seoyeons@naver.com, 박서연, W, 1992-03-16) / (yoonsy94@gmail.com, 윤서연, W, 1994-03-19)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 12. 중성화 여부 파악하기

- Level 2 · 프로그래머스 59409 · https://school.programmers.co.kr/learn/courses/30/lessons/59409

### 정답 SQL

```sql
SELECT ANIMAL_ID, NAME,
       CASE WHEN SEX_UPON_INTAKE LIKE 'Neutered%' OR SEX_UPON_INTAKE LIKE 'Spayed%'
            THEN 'O' ELSE 'X' END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

- 결과: 100행
- 풀이 핵심: `CASE WHEN … LIKE 'Neutered%' OR … LIKE 'Spayed%' THEN 'O' ELSE 'X' END`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 모든 동물의 아이디 · 이름 · 중성화 여부를 아이디 순서로 조회. 성별 및 중성화 여부에 Neutered나 Spayed가 들어 있으면 O, 아니면 X

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `LIKE`에 `%`를 빠뜨려 모든 동물이 X로 나옴

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
모든 동물의 아이디 · 이름 · 중성화 여부를 아이디 순서로 조회하려고 해.
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
SELECT ANIMAL_ID, NAME,
       CASE WHEN SEX_UPON_INTAKE LIKE 'Neutered' OR SEX_UPON_INTAKE LIKE 'Spayed'
            THEN 'O' ELSE 'X' END AS 중성화
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```
- 기대한 결과: 100행, 앞 2행: (A349996, Sugar, O) / (A350276, Jewel, O) …
- 실제 결과: 100행, 앞 2행: (A349996, Sugar, X) / (A350276, Jewel, X) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 13. 조건에 부합하는 중고거래 상태 조회하기

- Level 2 · 프로그래머스 164672 · https://school.programmers.co.kr/learn/courses/30/lessons/164672

### 정답 SQL

```sql
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
       CASE STATUS WHEN 'SALE' THEN '판매중'
                   WHEN 'RESERVED' THEN '예약중'
                   WHEN 'DONE' THEN '거래완료' END AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = '2022-10-05'
ORDER BY BOARD_ID DESC;
```

- 결과: 5행
- 풀이 핵심: 값마다 바꿀 글자가 정해져 있으면 `CASE STATUS WHEN … THEN …`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
USED_GOODS_BOARD 테이블 구조:
+--------------+---------------+------+-----+---------+-------+
| Field        | Type          | Null | Key | Default | Extra |
+--------------+---------------+------+-----+---------+-------+
| BOARD_ID     | varchar(5)    | NO   | PRI | NULL    |       |
| WRITER_ID    | varchar(50)   | YES  |     | NULL    |       |
| TITLE        | varchar(100)  | YES  |     | NULL    |       |
| CONTENTS     | varchar(1000) | YES  |     | NULL    |       |
| PRICE        | int(11)       | YES  |     | NULL    |       |
| CREATED_DATE | date          | YES  |     | NULL    |       |
| STATUS       | varchar(10)   | YES  |     | NULL    |       |
| VIEWS        | int(11)       | YES  |     | NULL    |       |
+--------------+---------------+------+-----+---------+-------+
- 컬럼 뜻: 게시글 ID · 작성자 ID · 게시글 제목 · 게시글 내용 · 가격 · 작성일 · 거래상태 · 조회수
- 내가 이해한 문제: 2022년 10월 5일에 등록된 게시글의 ID · 작성자 ID · 제목 · 가격 · 거래상태를 게시글 ID 큰 순서로 조회. 거래상태는 SALE 판매중, RESERVED 예약중, DONE 거래완료로 표시

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: DONE에 대한 `WHEN`을 빠뜨려 거래완료가 NULL로 나옴

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
2022년 10월 5일에 등록된 게시글의 ID · 작성자 ID · 제목 · 가격 · 거래상태를 게시글 ID 큰 순서로 조회하려고 해.
USED_GOODS_BOARD 테이블 구조:
+--------------+---------------+------+-----+---------+-------+
| Field        | Type          | Null | Key | Default | Extra |
+--------------+---------------+------+-----+---------+-------+
| BOARD_ID     | varchar(5)    | NO   | PRI | NULL    |       |
| WRITER_ID    | varchar(50)   | YES  |     | NULL    |       |
| TITLE        | varchar(100)  | YES  |     | NULL    |       |
| CONTENTS     | varchar(1000) | YES  |     | NULL    |       |
| PRICE        | int(11)       | YES  |     | NULL    |       |
| CREATED_DATE | date          | YES  |     | NULL    |       |
| STATUS       | varchar(10)   | YES  |     | NULL    |       |
| VIEWS        | int(11)       | YES  |     | NULL    |       |
+--------------+---------------+------+-----+---------+-------+
```sql
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
       CASE STATUS WHEN 'SALE' THEN '판매중'
                   WHEN 'RESERVED' THEN '예약중' END AS STATUS
FROM USED_GOODS_BOARD
WHERE CREATED_DATE = '2022-10-05'
ORDER BY BOARD_ID DESC;
```
- 기대한 결과: 5행, 2번째 행부터: (B0012, hwahwa2, 에어팟 프로 팔아요, 125000, 거래완료) / (B0011, sangyoung58, 아이폰14프로 256기가 자급제팔아요, 1500000, 거래완료) …
- 실제 결과: 5행, 2번째 행부터: (B0012, hwahwa2, 에어팟 프로 팔아요, 125000, NULL) / (B0011, sangyoung58, 아이폰14프로 256기가 자급제팔아요, 1500000, NULL) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 14. 조건별로 분류하여 주문상태 출력하기

- Level 3 · 프로그래머스 131113 · https://school.programmers.co.kr/learn/courses/30/lessons/131113

### 정답 SQL

```sql
SELECT ORDER_ID, PRODUCT_ID,
       DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
       CASE WHEN OUT_DATE IS NULL THEN '출고미정'
            WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
            ELSE '출고대기' END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;
```

- 결과: 30행
- 풀이 핵심: `CASE WHEN`의 조건은 위에서부터 차례로 검사함. NULL은 `IS NULL`로 검사

### 방향 묻기 프롬프트

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
FOOD_ORDER 테이블 구조:
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| ORDER_ID     | varchar(10) | NO   | PRI | NULL    |       |
| PRODUCT_ID   | varchar(5)  | NO   |     | NULL    |       |
| AMOUNT       | int(11)     | YES  |     | NULL    |       |
| PRODUCE_DATE | date        | YES  |     | NULL    |       |
| IN_DATE      | date        | YES  |     | NULL    |       |
| OUT_DATE     | date        | YES  |     | NULL    |       |
| FACTORY_ID   | varchar(10) | YES  |     | NULL    |       |
| WAREHOUSE_ID | varchar(10) | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 주문 ID · 제품 ID · 주문양 · 생산일자 · 입고일자 · 출고일자 · 공장 ID · 창고 ID
- 내가 이해한 문제: 모든 주문의 ID · 제품 ID · 출고일자 · 출고여부를 주문 ID 순서로 조회. 출고일자가 2022-05-01까지면 출고완료, 그 뒤면 출고대기, 없으면 출고미정

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · 검색 연산자 · ORDER BY · LIMIT · SQL 함수(문자열 · 숫자 · 날짜 · 형변환 · 조건 · 집계) 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: NULL을 `=`로 검사해 출고일자가 없는 주문이 출고대기로 나옴

````md
## 맥락
SQL 함수를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
모든 주문의 ID · 제품 ID · 출고일자 · 출고여부를 주문 ID 순서로 조회하려고 해.
FOOD_ORDER 테이블 구조:
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| ORDER_ID     | varchar(10) | NO   | PRI | NULL    |       |
| PRODUCT_ID   | varchar(5)  | NO   |     | NULL    |       |
| AMOUNT       | int(11)     | YES  |     | NULL    |       |
| PRODUCE_DATE | date        | YES  |     | NULL    |       |
| IN_DATE      | date        | YES  |     | NULL    |       |
| OUT_DATE     | date        | YES  |     | NULL    |       |
| FACTORY_ID   | varchar(10) | YES  |     | NULL    |       |
| WAREHOUSE_ID | varchar(10) | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
```sql
SELECT ORDER_ID, PRODUCT_ID,
       DATE_FORMAT(OUT_DATE, '%Y-%m-%d') AS OUT_DATE,
       CASE WHEN OUT_DATE = NULL THEN '출고미정'
            WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
            ELSE '출고대기' END AS 출고여부
FROM FOOD_ORDER
ORDER BY ORDER_ID;
```
- 기대한 결과: 30행, 6번째 행부터: (OD00000041, P0081, NULL, 출고미정) / (OD00000042, P0082, 2022-03-20, 출고완료) …
- 실제 결과: 30행, 6번째 행부터: (OD00000041, P0081, NULL, 출고대기) / (OD00000042, P0082, 2022-03-20, 출고완료) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

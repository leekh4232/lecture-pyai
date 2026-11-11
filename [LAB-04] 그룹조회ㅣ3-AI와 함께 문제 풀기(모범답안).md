# [LAB-04] 그룹조회ㅣ3-AI와 함께 문제 풀기 모범답안

「[LAB-04] 그룹조회ㅣ3-AI와 함께 문제 풀기(AI 학습활동)」 덱의 문제 13개에 대한 정답 SQL과, 두 템플릿(방향 묻기 · 원인 묻기)을 빈칸 없이 채운 프롬프트를 담았다.

## 문제 1. 고양이와 개는 몇 마리 있을까

- Level 2 · 프로그래머스 59040 · https://school.programmers.co.kr/learn/courses/30/lessons/59040

### 정답 SQL

```sql
SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
```

- 결과: 2행
- 풀이 핵심: 종마다 따로 세려면 `GROUP BY ANIMAL_TYPE`으로 묶은 뒤 `COUNT(*)`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 고양이와 개가 각각 몇 마리인지 생물 종 이름 순서(고양이 먼저)로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `GROUP BY`를 빠뜨려 전체가 한 묶음이 됨. Cat 한 행에 전체 마릿수가 나옴

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
고양이와 개가 각각 몇 마리인지 생물 종 이름 순서(고양이 먼저)로 조회하려고 해.
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
SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS
ORDER BY ANIMAL_TYPE;
```
- 기대한 결과: 2행 (Cat, 15) / (Dog, 85)
- 실제 결과: 1행 (Cat, 100)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 2. 중복 제거하기

- Level 2 · 프로그래머스 59408 · https://school.programmers.co.kr/learn/courses/30/lessons/59408

### 정답 SQL

```sql
SELECT COUNT(DISTINCT NAME) AS count
FROM ANIMAL_INS;
```

- 결과: 1행
- 풀이 핵심: `COUNT(DISTINCT NAME)`은 중복을 한 번만 세고 NULL은 세지 않음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 이름이 없는 동물은 빼고, 같은 이름은 하나로 쳐서 이름이 몇 개인지 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `DISTINCT`를 `COUNT` 앞에 써서 중복 이름까지 모두 셈. `DISTINCT`가 결과 행에 걸림

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
이름이 없는 동물은 빼고, 같은 이름은 하나로 쳐서 이름이 몇 개인지 조회하려고 해.
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
SELECT DISTINCT COUNT(NAME) AS count
FROM ANIMAL_INS;
```
- 기대한 결과: 1행 (96)
- 실제 결과: 1행 (99)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 3. 카테고리 별 상품 개수 구하기

- Level 2 · 프로그래머스 131529 · https://school.programmers.co.kr/learn/courses/30/lessons/131529

### 정답 SQL

```sql
SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE, 2)
ORDER BY CATEGORY;
```

- 결과: 11행
- 풀이 핵심: 잘라낸 값 `LEFT(PRODUCT_CODE, 2)`로 묶어야 같은 카테고리가 한 묶음이 됨

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
PRODUCT 테이블 구조:
+--------------+---------+------+-----+---------+-------+
| Field        | Type    | Null | Key | Default | Extra |
+--------------+---------+------+-----+---------+-------+
| PRODUCT_ID   | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_CODE | char(8) | NO   | UNI | NULL    |       |
| PRICE        | int(11) | NO   |     | NULL    |       |
+--------------+---------+------+-----+---------+-------+
- 컬럼 뜻: 상품 ID · 상품코드(8자리, 앞 2자리는 카테고리 코드) · 판매가
- 내가 이해한 문제: 상품코드 앞 2자리(카테고리 코드)마다 상품이 몇 개인지 카테고리 코드 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `GROUP BY`에 자르기 전 `PRODUCT_CODE`를 써서 상품마다 한 묶음이 됨. 같은 카테고리가 여러 행으로 나오고 개수가 모두 1

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
상품코드 앞 2자리(카테고리 코드)마다 상품이 몇 개인지 카테고리 코드 순서로 조회하려고 해.
PRODUCT 테이블 구조:
+--------------+---------+------+-----+---------+-------+
| Field        | Type    | Null | Key | Default | Extra |
+--------------+---------+------+-----+---------+-------+
| PRODUCT_ID   | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_CODE | char(8) | NO   | UNI | NULL    |       |
| PRICE        | int(11) | NO   |     | NULL    |       |
+--------------+---------+------+-----+---------+-------+
```sql
SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRODUCT_CODE
ORDER BY CATEGORY;
```
- 기대한 결과: 11행, 앞 2행: (A2, 3) / (A3, 4) …
- 실제 결과: 30행, 앞 2행: (A2, 1) / (A2, 1) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 4. 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기

- Level 2 · 프로그래머스 151137 · https://school.programmers.co.kr/learn/courses/30/lessons/151137

### 정답 SQL

```sql
SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%'
   OR OPTIONS LIKE '%열선시트%'
   OR OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE;
```

- 결과: 5행
- 풀이 핵심: 옵션 조건은 묶기 전에 `WHERE`에서 `LIKE`와 `OR`로 거르고, 남은 행을 `CAR_TYPE`으로 묶어 셈

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 통풍시트 · 열선시트 · 가죽시트 중 하나라도 옵션에 있는 자동차가 종류별로 몇 대인지 자동차 종류 순서로 조회. 자동차 수의 컬럼 이름은 CARS

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `GROUP BY`에 `OPTIONS`까지 넣어 옵션 조합마다 따로 묶임. 같은 종류가 여러 행으로 나뉨

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
통풍시트 · 열선시트 · 가죽시트 중 하나라도 옵션에 있는 자동차가 종류별로 몇 대인지 자동차 종류 순서로 조회하려고 해.
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
SELECT CAR_TYPE, COUNT(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%통풍시트%'
   OR OPTIONS LIKE '%열선시트%'
   OR OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE, OPTIONS
ORDER BY CAR_TYPE;
```
- 기대한 결과: 5행, 앞 2행: (SUV, 6) / (리무진, 2) …
- 실제 결과: 18행, 앞 2행: (SUV, 3) / (SUV, 1) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 5. 진료과별 총 예약 횟수 출력하기

- Level 2 · 프로그래머스 132202 · https://school.programmers.co.kr/learn/courses/30/lessons/132202

### 정답 SQL

```sql
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD >= '2022-05-01' AND APNT_YMD < '2022-06-01'
GROUP BY MCDP_CD
ORDER BY COUNT(*), MCDP_CD;
```

- 결과: 2행
- 풀이 핵심: 5월은 `WHERE`에서 6월 1일 미만까지로 거르고, `MCDP_CD`로 묶어 `COUNT(*)`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
APPOINTMENT 테이블 구조:
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| APNT_YMD      | timestamp   | YES  |     | NULL    |       |
| APNT_NO       | int(11)     | NO   | PRI | NULL    |       |
| PT_NO         | varchar(10) | NO   |     | NULL    |       |
| MCDP_CD       | varchar(6)  | YES  |     | NULL    |       |
| MDDR_ID       | varchar(10) | YES  |     | NULL    |       |
| APNT_CNCL_YN  | varchar(1)  | YES  |     | NULL    |       |
| APNT_CNCL_YMD | date        | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 진료예약일시 · 진료예약번호 · 환자번호 · 진료과코드 · 의사ID · 예약취소여부 · 예약취소날짜
- 내가 이해한 문제: 2022년 5월에 잡힌 예약이 진료과코드마다 몇 건인지 건수 적은 순, 같으면 진료과코드 순으로 조회. 컬럼 이름은 진료과코드 · 5월예약건수

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `COUNT(APNT_CNCL_YN)`으로 세어 예약취소여부가 NULL인 예약이 빠짐. GS가 1건으로 줄어 순서도 바뀜

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
2022년 5월에 잡힌 예약이 진료과코드마다 몇 건인지 건수 적은 순, 같으면 진료과코드 순으로 조회하려고 해.
APPOINTMENT 테이블 구조:
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| APNT_YMD      | timestamp   | YES  |     | NULL    |       |
| APNT_NO       | int(11)     | NO   | PRI | NULL    |       |
| PT_NO         | varchar(10) | NO   |     | NULL    |       |
| MCDP_CD       | varchar(6)  | YES  |     | NULL    |       |
| MDDR_ID       | varchar(10) | YES  |     | NULL    |       |
| APNT_CNCL_YN  | varchar(1)  | YES  |     | NULL    |       |
| APNT_CNCL_YMD | date        | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
```sql
SELECT MCDP_CD AS '진료과코드', COUNT(APNT_CNCL_YN) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD >= '2022-05-01' AND APNT_YMD < '2022-06-01'
GROUP BY MCDP_CD
ORDER BY COUNT(APNT_CNCL_YN), MCDP_CD;
```
- 기대한 결과: 2행 (FM, 2) / (GS, 2)
- 실제 결과: 2행 (GS, 1) / (FM, 2)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 6. 연도 별 평균 미세먼지 농도 조회하기

- Level 2 · 프로그래머스 284530 · https://school.programmers.co.kr/learn/courses/30/lessons/284530

### 정답 SQL

```sql
SELECT YEAR(YM) AS YEAR,
       ROUND(AVG(PM_VAL1), 2) AS PM10,
       ROUND(AVG(PM_VAL2), 2) AS `PM2.5`
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY YEAR(YM)
ORDER BY YEAR;
```

- 결과: 1행
- 풀이 핵심: 연도는 `YEAR(YM)`으로 묶고, 소수 셋째 자리에서 반올림은 `ROUND(값, 2)`. 마침표가 든 별칭은 백틱으로 감쌈

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
AIR_POLLUTION 테이블 구조:
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| LOCATION1 | varchar(100) | YES  |     | NULL    |       |
| LOCATION2 | varchar(100) | YES  |     | NULL    |       |
| YM        | date         | YES  |     | NULL    |       |
| PM_VAL1   | int(11)      | YES  |     | NULL    |       |
| PM_VAL2   | int(11)      | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
- 컬럼 뜻: 지역구분1 · 지역구분2 · 측정일 · 미세먼지 오염도 · 초미세먼지 오염도
- 내가 이해한 문제: 수원 지역의 연도별 평균 미세먼지 · 평균 초미세먼지 오염도를 소수 셋째 자리에서 반올림해 연도 순서로 조회. 컬럼 이름은 YEAR · PM10 · PM2.5

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: '셋째 자리에서 반올림'을 `ROUND(값, 3)`으로 써서 소수 셋째 자리까지 나옴

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
수원 지역의 연도별 평균 미세먼지 · 평균 초미세먼지 오염도를 소수 셋째 자리에서 반올림해 연도 순서로 조회하려고 해.
AIR_POLLUTION 테이블 구조:
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| LOCATION1 | varchar(100) | YES  |     | NULL    |       |
| LOCATION2 | varchar(100) | YES  |     | NULL    |       |
| YM        | date         | YES  |     | NULL    |       |
| PM_VAL1   | int(11)      | YES  |     | NULL    |       |
| PM_VAL2   | int(11)      | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
```sql
SELECT YEAR(YM) AS YEAR,
       ROUND(AVG(PM_VAL1), 3) AS PM10,
       ROUND(AVG(PM_VAL2), 3) AS `PM2.5`
FROM AIR_POLLUTION
WHERE LOCATION2 = '수원'
GROUP BY YEAR(YM)
ORDER BY YEAR;
```
- 기대한 결과: 1행 (2018, 41.00, 20.25)
- 실제 결과: 1행 (2018, 41.000, 20.250)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 7. 가격대 별 상품 개수 구하기

- Level 2 · 프로그래머스 131530 · https://school.programmers.co.kr/learn/courses/30/lessons/131530

### 정답 SQL

```sql
SELECT FLOOR(PRICE / 10000) * 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP;
```

- 결과: 8행
- 풀이 핵심: `FLOOR(PRICE / 10000) * 10000`으로 구간의 최소금액을 만들고 그 값으로 묶음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
PRODUCT 테이블 구조:
+--------------+---------+------+-----+---------+-------+
| Field        | Type    | Null | Key | Default | Extra |
+--------------+---------+------+-----+---------+-------+
| PRODUCT_ID   | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_CODE | char(8) | NO   | UNI | NULL    |       |
| PRICE        | int(11) | NO   |     | NULL    |       |
+--------------+---------+------+-----+---------+-------+
- 컬럼 뜻: 상품 ID · 상품코드(8자리, 앞 2자리는 카테고리 코드) · 판매가
- 내가 이해한 문제: 판매가를 만원 단위 가격대(구간의 최소금액)로 나눠 가격대마다 상품이 몇 개인지 가격대 순서로 조회. 컬럼 이름은 PRICE_GROUP · PRODUCTS

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `FLOOR` 대신 `ROUND`를 써서 만원 단위에서 5천원 이상인 상품이 위 가격대로 올라감

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
판매가를 만원 단위 가격대(구간의 최소금액)로 나눠 가격대마다 상품이 몇 개인지 가격대 순서로 조회하려고 해.
PRODUCT 테이블 구조:
+--------------+---------+------+-----+---------+-------+
| Field        | Type    | Null | Key | Default | Extra |
+--------------+---------+------+-----+---------+-------+
| PRODUCT_ID   | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_CODE | char(8) | NO   | UNI | NULL    |       |
| PRICE        | int(11) | NO   |     | NULL    |       |
+--------------+---------+------+-----+---------+-------+
```sql
SELECT ROUND(PRICE / 10000) * 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP;
```
- 기대한 결과: 8행, 앞 2행: (10000, 2) / (20000, 2) …
- 실제 결과: 8행, 앞 2행: (20000, 4) / (30000, 2) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 8. 노선별 평균 역 사이 거리 조회하기

- Level 2 · 프로그래머스 284531 · https://school.programmers.co.kr/learn/courses/30/lessons/284531

### 정답 SQL

```sql
SELECT ROUTE,
       CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE,
       CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY ROUND(SUM(D_BETWEEN_DIST), 1) DESC;
```

- 결과: 2행
- 풀이 핵심: 합과 평균은 모두 `D_BETWEEN_DIST`로 구함. 'km'를 붙이면 문자열이 되므로 정렬은 숫자 식으로 함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
SUBWAY_DISTANCE 테이블 구조:
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| LINE           | varchar(10)  | YES  |     | NULL    |       |
| NO             | int(11)      | YES  |     | NULL    |       |
| ROUTE          | varchar(50)  | YES  |     | NULL    |       |
| STATION_NAME   | varchar(100) | YES  |     | NULL    |       |
| D_BETWEEN_DIST | float(10,3)  | YES  |     | NULL    |       |
| D_CUMULATIVE   | float(10,3)  | YES  |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
- 컬럼 뜻: 호선 · 순번 · 노선 · 역 이름 · 역 사이 거리 · 노선별 누계 거리
- 내가 이해한 문제: 노선마다 역 사이 거리의 합(총 누계 거리)과 평균을 km를 붙여 총 누계 거리가 긴 순서로 조회. 합은 소수 둘째 자리, 평균은 소수 셋째 자리에서 반올림

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 총 누계 거리를 `SUM(D_CUMULATIVE)`로 구해 이미 누적된 거리를 또 더함. 총 누계 거리가 훨씬 크게 나옴

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
노선마다 역 사이 거리의 합(총 누계 거리)과 평균을 km를 붙여 총 누계 거리가 긴 순서로 조회하려고 해.
SUBWAY_DISTANCE 테이블 구조:
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| LINE           | varchar(10)  | YES  |     | NULL    |       |
| NO             | int(11)      | YES  |     | NULL    |       |
| ROUTE          | varchar(50)  | YES  |     | NULL    |       |
| STATION_NAME   | varchar(100) | YES  |     | NULL    |       |
| D_BETWEEN_DIST | float(10,3)  | YES  |     | NULL    |       |
| D_CUMULATIVE   | float(10,3)  | YES  |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
```sql
SELECT ROUTE,
       CONCAT(ROUND(SUM(D_CUMULATIVE), 1), 'km') AS TOTAL_DISTANCE,
       CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY ROUND(SUM(D_CUMULATIVE), 1) DESC;
```
- 기대한 결과: 2행 (신정지선, 6.0km, 1.50km) / (성수지선, 5.4km, 1.35km)
- 실제 결과: 2행 (신정지선, 231.1km, 1.50km) / (성수지선, 210.4km, 1.35km)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 9. 입양 시각 구하기(1)

- Level 2 · 프로그래머스 59412 · https://school.programmers.co.kr/learn/courses/30/lessons/59412

### 정답 SQL

```sql
SELECT CAST(DATE_FORMAT(DATETIME, '%H') AS SIGNED) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE CAST(DATE_FORMAT(DATETIME, '%H') AS SIGNED) BETWEEN 9 AND 19
GROUP BY CAST(DATE_FORMAT(DATETIME, '%H') AS SIGNED)
ORDER BY HOUR;
```

- 결과: 11행
- 풀이 핵심: 시는 `CAST(DATE_FORMAT(DATETIME, '%H') AS SIGNED)`로 꺼내 숫자로 바꾸고, 그 값으로 거른 뒤 묶음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ANIMAL_OUTS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_OUTCOME | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 아이디 · 생물 종 · 입양일 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 입양일의 시(9시부터 19시까지)마다 입양이 몇 건인지 시간대 순서로 조회. 컬럼 이름은 HOUR · COUNT

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `SELECT`에서 붙인 별칭 `HOUR`를 `WHERE`에 써서 에러가 남. `WHERE`는 `SELECT`보다 먼저 실행됨

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
입양일의 시(9시부터 19시까지)마다 입양이 몇 건인지 시간대 순서로 조회하려고 해.
ANIMAL_OUTS 테이블 구조:
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| ANIMAL_ID        | varchar(7)  | NO   | PRI | NULL    |       |
| ANIMAL_TYPE      | varchar(3)  | NO   |     | NULL    |       |
| DATETIME         | datetime    | NO   |     | NULL    |       |
| NAME             | varchar(12) | YES  |     | NULL    |       |
| SEX_UPON_OUTCOME | varchar(13) | NO   |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
```sql
SELECT CAST(DATE_FORMAT(DATETIME, '%H') AS SIGNED) AS HOUR, COUNT(*) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR BETWEEN 9 AND 19
GROUP BY HOUR
ORDER BY HOUR;
```
- 기대한 결과: 11행, 앞 2행: (9, 1) / (10, 2) …
- 실제 결과: ERROR 1054 (42S22): Unknown column 'HOUR' in 'WHERE'

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 10. 동명 동물 수 찾기

- Level 2 · 프로그래머스 59041 · https://school.programmers.co.kr/learn/courses/30/lessons/59041

### 정답 SQL

```sql
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME;
```

- 결과: 2행
- 풀이 핵심: 묶은 뒤의 조건(횟수 2 이상)은 `WHERE`가 아니라 `HAVING`에 씀. `COUNT(NAME)`은 NULL을 세지 않음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 이름이 없는 동물은 빼고, 두 번 이상 쓰인 이름과 쓰인 횟수를 이름 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 집계 함수 조건을 `WHERE`에 써서 에러가 남. `WHERE`는 묶기 전에 행 하나씩 검사함

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
이름이 없는 동물은 빼고, 두 번 이상 쓰인 이름과 쓰인 횟수를 이름 순서로 조회하려고 해.
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
SELECT NAME, COUNT(NAME) AS COUNT
FROM ANIMAL_INS
WHERE COUNT(NAME) >= 2
GROUP BY NAME
ORDER BY NAME;
```
- 기대한 결과: 2행 (Lucy, 3) / (Raven, 2)
- 실제 결과: ERROR 1111 (HY000): Invalid use of group function

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 11. 재구매가 일어난 상품과 회원 리스트 구하기

- Level 2 · 프로그래머스 131536 · https://school.programmers.co.kr/learn/courses/30/lessons/131536

### 정답 SQL

```sql
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) >= 2
ORDER BY USER_ID, PRODUCT_ID DESC;
```

- 결과: 2행
- 풀이 핵심: 회원과 상품 두 컬럼으로 함께 묶고, 묶음의 행이 2개 이상이면 재구매이므로 `HAVING COUNT(*) >= 2`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
ONLINE_SALE 테이블 구조:
+----------------+---------+------+-----+---------+-------+
| Field          | Type    | Null | Key | Default | Extra |
+----------------+---------+------+-----+---------+-------+
| ONLINE_SALE_ID | int(11) | NO   | PRI | NULL    |       |
| USER_ID        | int(11) | NO   | MUL | NULL    |       |
| PRODUCT_ID     | int(11) | NO   |     | NULL    |       |
| SALES_AMOUNT   | int(11) | NO   |     | NULL    |       |
| SALES_DATE     | date    | NO   |     | NULL    |       |
+----------------+---------+------+-----+---------+-------+
- 컬럼 뜻: 온라인 상품 판매 ID · 회원 ID · 상품 ID · 판매량 · 판매일
- 내가 이해한 문제: 같은 회원이 같은 상품을 두 번 이상 산 경우의 회원 ID와 상품 ID를 회원 ID 순, 같으면 상품 ID 큰 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: '두 번 이상'을 `> 2`로 써서 세 번 이상 산 경우만 남음. 결과가 비어 있음

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
같은 회원이 같은 상품을 두 번 이상 산 경우의 회원 ID와 상품 ID를 회원 ID 순, 같으면 상품 ID 큰 순서로 조회하려고 해.
ONLINE_SALE 테이블 구조:
+----------------+---------+------+-----+---------+-------+
| Field          | Type    | Null | Key | Default | Extra |
+----------------+---------+------+-----+---------+-------+
| ONLINE_SALE_ID | int(11) | NO   | PRI | NULL    |       |
| USER_ID        | int(11) | NO   | MUL | NULL    |       |
| PRODUCT_ID     | int(11) | NO   |     | NULL    |       |
| SALES_AMOUNT   | int(11) | NO   |     | NULL    |       |
| SALES_DATE     | date    | NO   |     | NULL    |       |
+----------------+---------+------+-----+---------+-------+
```sql
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 2
ORDER BY USER_ID, PRODUCT_ID DESC;
```
- 기대한 결과: 2행 (15, 12) / (119, 12)
- 실제 결과: 0행 (결과가 비어 있음)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 12. 자동차 평균 대여 기간 구하기

- Level 2 · 프로그래머스 157342 · https://school.programmers.co.kr/learn/courses/30/lessons/157342

### 정답 SQL

```sql
SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
HAVING AVERAGE_DURATION >= 7
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;
```

- 결과: 23행
- 풀이 핵심: 대여 기간은 `DATEDIFF(END_DATE, START_DATE) + 1`. 평균에 대한 조건은 묶은 뒤라 `HAVING`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 평균 대여 기간이 7일 이상인 자동차의 ID와 평균 대여 기간을 평균 대여 기간 긴 순, 같으면 자동차 ID 큰 순서로 조회. 평균은 소수 둘째 자리에서 반올림

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 평균에 걸 조건을 `WHERE`에서 대여 기록 하나하나에 걸어 7일 미만 기록이 빠진 채 평균이 계산됨. 평균이 커지고 자동차 수도 늘어남

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
평균 대여 기간이 7일 이상인 자동차의 ID와 평균 대여 기간을 평균 대여 기간 긴 순, 같으면 자동차 ID 큰 순서로 조회하려고 해.
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
SELECT CAR_ID, ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE DATEDIFF(END_DATE, START_DATE) + 1 >= 7
GROUP BY CAR_ID
ORDER BY AVERAGE_DURATION DESC, CAR_ID DESC;
```
- 기대한 결과: 23행, 앞 2행: (26, 101.0) / (22, 46.0) …
- 실제 결과: 27행, 앞 2행: (29, 101.0) / (26, 101.0) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 13. 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기

- Level 3 · 프로그래머스 157340 · https://school.programmers.co.kr/learn/courses/30/lessons/157340

### 정답 SQL

```sql
SELECT CAR_ID,
       CASE WHEN SUM('2022-10-16' BETWEEN START_DATE AND END_DATE) > 0 THEN '대여중'
            ELSE '대여 가능' END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;
```

- 결과: 29행
- 풀이 핵심: 자동차 한 대에 기록이 여러 건이라 `CAR_ID`로 묶고, `SUM(조건)`으로 10월 16일이 낀 기록이 한 건이라도 있는지 봄

### 방향 묻기 프롬프트

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 자동차마다 2022년 10월 16일에 대여 중이면 대여중, 아니면 대여 가능으로 표시해 자동차 ID 큰 순서로 조회. 반납일이 10월 16일이어도 대여중

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · DISTINCT · 윈도우 함수 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 묶지 않고 `DISTINCT`로 기록마다 판정해 같은 자동차가 대여중 · 대여 가능 두 행으로 나옴

````md
## 맥락
SQL 그룹 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
자동차마다 2022년 10월 16일에 대여 중이면 대여중, 아니면 대여 가능으로 표시해 자동차 ID 큰 순서로 조회하려고 해.
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
SELECT DISTINCT CAR_ID,
       CASE WHEN '2022-10-16' BETWEEN START_DATE AND END_DATE THEN '대여중'
            ELSE '대여 가능' END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
ORDER BY CAR_ID DESC;
```
- 기대한 결과: 29행, 2번째 행부터: (29, 대여중) / (28, 대여중) …
- 실제 결과: 49행, 2번째 행부터: (29, 대여 가능) / (29, 대여중) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

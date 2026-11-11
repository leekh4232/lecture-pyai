# [LAB-06] 고급 데이터 조회ㅣ6-AI와 함께 문제 풀기 모범답안

「[LAB-06] 고급 데이터 조회ㅣ6-AI와 함께 문제 풀기(AI 학습활동)」 덱의 문제 17개에 대한 정답 SQL과, 두 템플릿(방향 묻기 · 원인 묻기)을 빈칸 없이 채운 프롬프트를 담았다.

## 문제 1. 과일로 만든 아이스크림 고르기

- Level 1 · 프로그래머스 133025 · https://school.programmers.co.kr/learn/courses/30/lessons/133025

### 정답 SQL

```sql
SELECT F.FLAVOR
FROM FIRST_HALF F
JOIN ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR
WHERE F.TOTAL_ORDER > 3000
  AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY F.TOTAL_ORDER DESC;
```

- 결과: 1행
- 풀이 핵심: 두 테이블을 `FLAVOR`로 `JOIN`한 뒤 조건 두 개를 `AND`로 이음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
FIRST_HALF 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| SHIPMENT_ID | int(11)      | NO   |     | NULL    |       |
| FLAVOR      | varchar(300) | NO   | PRI | NULL    |       |
| TOTAL_ORDER | int(11)      | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
ICECREAM_INFO 테이블 구조:
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| FLAVOR          | varchar(300) | NO   | PRI | NULL    |       |
| INGREDIENT_TYPE | varchar(300) | NO   |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
- FIRST_HALF 컬럼 뜻: 출하 번호 · 아이스크림 맛 · 상반기 아이스크림 총주문량
- ICECREAM_INFO 컬럼 뜻: 아이스크림 맛 · 성분 타입(주 성분이 설탕이면 sugar_based, 과일이면 fruit_based)
- 내가 이해한 문제: 상반기 총주문량이 3,000보다 많고 주 성분이 과일인 아이스크림의 맛을 총주문량이 큰 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `SELECT`의 `FLAVOR`에 별칭을 붙이지 않아 에러가 남. 두 테이블에 모두 있는 컬럼이라 어느 쪽인지 모름

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
상반기 총주문량이 3,000보다 많고 주 성분이 과일인 아이스크림의 맛을 총주문량이 큰 순서로 조회하려고 해.
FIRST_HALF 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| SHIPMENT_ID | int(11)      | NO   |     | NULL    |       |
| FLAVOR      | varchar(300) | NO   | PRI | NULL    |       |
| TOTAL_ORDER | int(11)      | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
ICECREAM_INFO 테이블 구조:
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| FLAVOR          | varchar(300) | NO   | PRI | NULL    |       |
| INGREDIENT_TYPE | varchar(300) | NO   |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
```sql
SELECT FLAVOR
FROM FIRST_HALF F
JOIN ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR
WHERE F.TOTAL_ORDER > 3000
  AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY F.TOTAL_ORDER DESC;
```
- 기대한 결과: 1행 (strawberry)
- 실제 결과: ERROR 1052 (23000): Column 'FLAVOR' in SELECT is ambiguous

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 2. 조건에 부합하는 중고거래 댓글 조회하기

- Level 1 · 프로그래머스 164673 · https://school.programmers.co.kr/learn/courses/30/lessons/164673

### 정답 SQL

```sql
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS,
       DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
WHERE B.CREATED_DATE >= '2022-10-01' AND B.CREATED_DATE < '2022-11-01'
ORDER BY R.CREATED_DATE, B.TITLE;
```

- 결과: 17행
- 풀이 핵심: 게시글과 댓글을 `BOARD_ID`로 `JOIN`. 2022년 10월 조건은 게시글 작성일(`B.CREATED_DATE`)에 걺

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
USED_GOODS_REPLY 테이블 구조:
+--------------+---------------+------+-----+---------+-------+
| Field        | Type          | Null | Key | Default | Extra |
+--------------+---------------+------+-----+---------+-------+
| REPLY_ID     | varchar(10)   | NO   | PRI | NULL    |       |
| BOARD_ID     | varchar(5)    | YES  |     | NULL    |       |
| WRITER_ID    | varchar(50)   | YES  |     | NULL    |       |
| CONTENTS     | varchar(1000) | YES  |     | NULL    |       |
| CREATED_DATE | date          | YES  |     | NULL    |       |
+--------------+---------------+------+-----+---------+-------+
- USED_GOODS_BOARD 컬럼 뜻: 게시글 ID · 작성자 ID · 게시글 제목 · 게시글 내용 · 가격 · 작성일 · 거래상태 · 조회수
- USED_GOODS_REPLY 컬럼 뜻: 댓글 ID · 게시글 ID · 작성자 ID · 댓글 내용 · 작성일
- 내가 이해한 문제: 2022년 10월에 작성된 게시글에 달린 댓글의 게시글 제목 · 게시글 ID · 댓글 ID · 댓글 작성자 ID · 댓글 내용 · 댓글 작성일을 댓글 작성일 순, 같으면 게시글 제목 순으로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `JOIN` 대신 `LEFT JOIN`을 써서 댓글이 없는 게시글까지 댓글 칸이 NULL인 채로 나옴

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
2022년 10월에 작성된 게시글에 달린 댓글의 게시글 제목 · 게시글 ID · 댓글 ID · 댓글 작성자 ID · 댓글 내용 · 댓글 작성일을 댓글 작성일 순, 같으면 게시글 제목 순으로 조회하려고 해.
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
USED_GOODS_REPLY 테이블 구조:
+--------------+---------------+------+-----+---------+-------+
| Field        | Type          | Null | Key | Default | Extra |
+--------------+---------------+------+-----+---------+-------+
| REPLY_ID     | varchar(10)   | NO   | PRI | NULL    |       |
| BOARD_ID     | varchar(5)    | YES  |     | NULL    |       |
| WRITER_ID    | varchar(50)   | YES  |     | NULL    |       |
| CONTENTS     | varchar(1000) | YES  |     | NULL    |       |
| CREATED_DATE | date          | YES  |     | NULL    |       |
+--------------+---------------+------+-----+---------+-------+
```sql
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS,
       DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD B
LEFT JOIN USED_GOODS_REPLY R ON B.BOARD_ID = R.BOARD_ID
WHERE B.CREATED_DATE >= '2022-10-01' AND B.CREATED_DATE < '2022-11-01'
ORDER BY R.CREATED_DATE, B.TITLE;
```
- 기대한 결과: 17행, 앞 2행: (반려견 배변패드 팝니다, B0001, R000000001, s2s2123, 구매하겠습니다. 쪽지 드립니다., 2022-10-02) / (국내산 볶음참깨, B0002, R000000002, hoho1112, 쪽지 주세요., 2022-10-03) …
- 실제 결과: 51행, 앞 2행: (S22 팔아요, B0031, NULL, NULL, NULL, NULL) / (갤럭시버즈, B0041, NULL, NULL, NULL, NULL) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 3. 조건에 맞는 도서와 저자 리스트 출력하기

- Level 2 · 프로그래머스 144854 · https://school.programmers.co.kr/learn/courses/30/lessons/144854

### 정답 SQL

```sql
SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK B
JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE B.CATEGORY = '경제'
ORDER BY B.PUBLISHED_DATE;
```

- 결과: 2행
- 풀이 핵심: 도서와 저자를 `AUTHOR_ID`로 `JOIN`해 저자명을 붙임

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
AUTHOR 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| AUTHOR_ID   | int(11)      | NO   | PRI | NULL    |       |
| AUTHOR_NAME | varchar(255) | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
- BOOK 컬럼 뜻: 도서 ID · 카테고리 · 저자 ID · 판매가(원) · 출판일
- AUTHOR 컬럼 뜻: 저자 ID · 저자명
- 내가 이해한 문제: 경제 카테고리 도서의 도서 ID · 저자명 · 출판일을 출판일 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `JOIN` 조건을 `B.BOOK_ID = A.AUTHOR_ID`로 잘못 이어 도서 ID와 같은 번호의 저자가 붙음

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
경제 카테고리 도서의 도서 ID · 저자명 · 출판일을 출판일 순서로 조회하려고 해.
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
AUTHOR 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| AUTHOR_ID   | int(11)      | NO   | PRI | NULL    |       |
| AUTHOR_NAME | varchar(255) | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
```sql
SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK B
JOIN AUTHOR A ON B.BOOK_ID = A.AUTHOR_ID
WHERE B.CATEGORY = '경제'
ORDER BY B.PUBLISHED_DATE;
```
- 기대한 결과: 2행 (1, 홍길동, 2020-01-10) / (2, 홍길동, 2021-06-10)
- 실제 결과: 2행 (1, 홍길동, 2020-01-10) / (2, 김영호, 2021-06-10)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 4. 성분으로 구분한 아이스크림 총 주문량

- Level 2 · 프로그래머스 133026 · https://school.programmers.co.kr/learn/courses/30/lessons/133026

### 정답 SQL

```sql
SELECT I.INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF F
JOIN ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR
GROUP BY I.INGREDIENT_TYPE
ORDER BY TOTAL_ORDER;
```

- 결과: 2행
- 풀이 핵심: `JOIN`으로 성분 타입을 붙이고 `GROUP BY I.INGREDIENT_TYPE`으로 묶어 `SUM`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
FIRST_HALF 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| SHIPMENT_ID | int(11)      | NO   |     | NULL    |       |
| FLAVOR      | varchar(300) | NO   | PRI | NULL    |       |
| TOTAL_ORDER | int(11)      | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
ICECREAM_INFO 테이블 구조:
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| FLAVOR          | varchar(300) | NO   | PRI | NULL    |       |
| INGREDIENT_TYPE | varchar(300) | NO   |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
- FIRST_HALF 컬럼 뜻: 출하 번호 · 아이스크림 맛 · 상반기 아이스크림 총주문량
- ICECREAM_INFO 컬럼 뜻: 아이스크림 맛 · 성분 타입(주 성분이 설탕이면 sugar_based, 과일이면 fruit_based)
- 내가 이해한 문제: 성분 타입별 상반기 총주문량을 TOTAL_ORDER라는 컬럼 이름으로, 총주문량이 작은 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `GROUP BY`를 빠뜨려 전체 합계 한 행만 나옴

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
성분 타입별 상반기 총주문량을 TOTAL_ORDER라는 컬럼 이름으로, 총주문량이 작은 순서로 조회하려고 해.
FIRST_HALF 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| SHIPMENT_ID | int(11)      | NO   |     | NULL    |       |
| FLAVOR      | varchar(300) | NO   | PRI | NULL    |       |
| TOTAL_ORDER | int(11)      | NO   |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
ICECREAM_INFO 테이블 구조:
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| FLAVOR          | varchar(300) | NO   | PRI | NULL    |       |
| INGREDIENT_TYPE | varchar(300) | NO   |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
```sql
SELECT I.INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER
FROM FIRST_HALF F
JOIN ICECREAM_INFO I ON F.FLAVOR = I.FLAVOR
ORDER BY TOTAL_ORDER;
```
- 기대한 결과: 2행 (fruit_based, 5550) / (sugar_based, 13400)
- 실제 결과: 1행 (sugar_based, 18950)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 5. 상품 별 오프라인 매출 구하기

- Level 2 · 프로그래머스 131533 · https://school.programmers.co.kr/learn/courses/30/lessons/131533

### 정답 SQL

```sql
SELECT P.PRODUCT_CODE, SUM(P.PRICE * O.SALES_AMOUNT) AS SALES
FROM PRODUCT P
JOIN OFFLINE_SALE O ON P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, P.PRODUCT_CODE;
```

- 결과: 28행
- 풀이 핵심: 상품과 판매를 `PRODUCT_ID`로 `JOIN`하고 상품코드로 묶어 `SUM(P.PRICE * O.SALES_AMOUNT)`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
PRODUCT 테이블 구조:
+--------------+---------+------+-----+---------+-------+
| Field        | Type    | Null | Key | Default | Extra |
+--------------+---------+------+-----+---------+-------+
| PRODUCT_ID   | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_CODE | char(8) | NO   | UNI | NULL    |       |
| PRICE        | int(11) | NO   |     | NULL    |       |
+--------------+---------+------+-----+---------+-------+
OFFLINE_SALE 테이블 구조:
+-----------------+---------+------+-----+---------+-------+
| Field           | Type    | Null | Key | Default | Extra |
+-----------------+---------+------+-----+---------+-------+
| OFFLINE_SALE_ID | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_ID      | int(11) | NO   | MUL | NULL    |       |
| SALES_AMOUNT    | int(11) | NO   |     | NULL    |       |
| SALES_DATE      | date    | NO   |     | NULL    |       |
+-----------------+---------+------+-----+---------+-------+
- PRODUCT 컬럼 뜻: 상품 ID · 상품코드(8자리, 앞 2자리는 카테고리 코드) · 판매가
- OFFLINE_SALE 컬럼 뜻: 오프라인 상품 판매 ID · 상품 ID · 판매량 · 판매일
- 내가 이해한 문제: 상품코드별 매출액(판매가 × 판매량) 합계를 매출액 큰 순서, 같으면 상품코드 순으로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `JOIN`에 `ON` 조건을 빠뜨려 모든 상품이 모든 판매 기록과 짝지어져 매출액이 크게 부풀려짐

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
상품코드별 매출액(판매가 × 판매량) 합계를 매출액 큰 순서, 같으면 상품코드 순으로 조회하려고 해.
PRODUCT 테이블 구조:
+--------------+---------+------+-----+---------+-------+
| Field        | Type    | Null | Key | Default | Extra |
+--------------+---------+------+-----+---------+-------+
| PRODUCT_ID   | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_CODE | char(8) | NO   | UNI | NULL    |       |
| PRICE        | int(11) | NO   |     | NULL    |       |
+--------------+---------+------+-----+---------+-------+
OFFLINE_SALE 테이블 구조:
+-----------------+---------+------+-----+---------+-------+
| Field           | Type    | Null | Key | Default | Extra |
+-----------------+---------+------+-----+---------+-------+
| OFFLINE_SALE_ID | int(11) | NO   | PRI | NULL    |       |
| PRODUCT_ID      | int(11) | NO   | MUL | NULL    |       |
| SALES_AMOUNT    | int(11) | NO   |     | NULL    |       |
| SALES_DATE      | date    | NO   |     | NULL    |       |
+-----------------+---------+------+-----+---------+-------+
```sql
SELECT P.PRODUCT_CODE, SUM(P.PRICE * O.SALES_AMOUNT) AS SALES
FROM PRODUCT P
JOIN OFFLINE_SALE O
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, P.PRODUCT_CODE;
```
- 기대한 결과: 28행, 앞 2행: (D1000000, 504000) / (D3000001, 425000) …
- 실제 결과: 30행, 앞 2행: (D3000001, 9095000) / (D3000000, 8774000) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 6. 대여 기록이 존재하는 자동차 리스트 구하기

- Level 3 · 프로그래머스 157341 · https://school.programmers.co.kr/learn/courses/30/lessons/157341

### 정답 SQL

```sql
SELECT DISTINCT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
WHERE C.CAR_TYPE = '세단'
  AND MONTH(H.START_DATE) = 10
ORDER BY C.CAR_ID DESC;
```

- 결과: 3행
- 풀이 핵심: `JOIN`하면 대여 기록마다 행이 생기므로 `DISTINCT`로 중복을 없앰

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블 구조:
+------------+---------+------+-----+---------+-------+
| Field      | Type    | Null | Key | Default | Extra |
+------------+---------+------+-----+---------+-------+
| HISTORY_ID | int(11) | NO   | PRI | NULL    |       |
| CAR_ID     | int(11) | NO   |     | NULL    |       |
| START_DATE | date    | NO   |     | NULL    |       |
| END_DATE   | date    | NO   |     | NULL    |       |
+------------+---------+------+-----+---------+-------+
- CAR_RENTAL_COMPANY_CAR 컬럼 뜻: 자동차 ID · 자동차 종류 · 일일 대여 요금(원) · 옵션 목록(콤마로 구분)
- CAR_RENTAL_COMPANY_RENTAL_HISTORY 컬럼 뜻: 대여 기록 ID · 자동차 ID · 대여 시작일 · 대여 종료일
- 내가 이해한 문제: 세단 중 10월에 대여를 시작한 기록이 있는 자동차 ID를 중복 없이 자동차 ID 큰 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `DISTINCT`를 빠뜨려 10월에 여러 번 빌린 자동차가 여러 번 나옴

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
세단 중 10월에 대여를 시작한 기록이 있는 자동차 ID를 중복 없이 자동차 ID 큰 순서로 조회하려고 해.
CAR_RENTAL_COMPANY_CAR 테이블 구조:
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| CAR_ID    | int(11)      | NO   | PRI | NULL    |       |
| CAR_TYPE  | varchar(255) | NO   |     | NULL    |       |
| DAILY_FEE | int(11)      | NO   |     | NULL    |       |
| OPTIONS   | varchar(255) | NO   |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
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
SELECT C.CAR_ID
FROM CAR_RENTAL_COMPANY_CAR C
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
WHERE C.CAR_TYPE = '세단'
  AND MONTH(H.START_DATE) = 10
ORDER BY C.CAR_ID DESC;
```
- 기대한 결과: 3행, 3번째 행부터: (3)
- 실제 결과: 6행, 3번째 행부터: (10) / (10) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 7. 있었는데요 없었습니다

- Level 3 · 프로그래머스 59043 · https://school.programmers.co.kr/learn/courses/30/lessons/59043

### 정답 SQL

```sql
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME < I.DATETIME
ORDER BY I.DATETIME;
```

- 결과: 2행
- 풀이 핵심: 두 테이블을 `ANIMAL_ID`로 `JOIN`한 뒤 `O.DATETIME < I.DATETIME`으로 두 날짜를 비교함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- ANIMAL_INS 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- ANIMAL_OUTS 컬럼 뜻: 아이디 · 생물 종 · 입양일 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 입양일이 보호 시작일보다 빠른 동물의 아이디와 이름을 보호 시작일 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 비교 방향을 거꾸로 써서 정상으로 입양 간 동물이 모두 나옴

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
입양일이 보호 시작일보다 빠른 동물의 아이디와 이름을 보호 시작일 순서로 조회하려고 해.
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
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME > I.DATETIME
ORDER BY I.DATETIME;
```
- 기대한 결과: 2행 (A362383, *Morado) / (A381217, Cherokee)
- 실제 결과: 94행, 앞 2행: (A399552, Jack) / (A379998, Disciple) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 8. 없어진 기록 찾기

- Level 3 · 프로그래머스 59042 · https://school.programmers.co.kr/learn/courses/30/lessons/59042

### 정답 SQL

```sql
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O
LEFT JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID;
```

- 결과: 4행
- 풀이 핵심: 입양 기록을 왼쪽에 두고 `LEFT JOIN`한 뒤 짝이 없어 NULL이 된 행을 `I.ANIMAL_ID IS NULL`로 고름

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- ANIMAL_INS 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- ANIMAL_OUTS 컬럼 뜻: 아이디 · 생물 종 · 입양일 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 입양 간 기록은 있는데 보호소에 들어온 기록이 없는 동물의 아이디와 이름을 아이디 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `LEFT JOIN` 대신 `JOIN`(INNER JOIN)을 써서 짝 없는 행이 빠져 결과가 비어 있음

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
입양 간 기록은 있는데 보호소에 들어온 기록이 없는 동물의 아이디와 이름을 아이디 순서로 조회하려고 해.
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
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS O
JOIN ANIMAL_INS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID;
```
- 기대한 결과: 4행, 앞 2행: (A349480, Daisy) / (A349733, Allie) …
- 실제 결과: 0행 (결과가 비어 있음)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 9. 오랜 기간 보호한 동물(1)

- Level 3 · 프로그래머스 59044 · https://school.programmers.co.kr/learn/courses/30/lessons/59044

### 정답 SQL

```sql
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME
LIMIT 3;
```

- 결과: 3행
- 풀이 핵심: 보호 기록을 왼쪽에 두고 `LEFT JOIN`, `O.ANIMAL_ID IS NULL`로 입양 안 간 동물만 남긴 뒤 `LIMIT 3`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- ANIMAL_INS 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- ANIMAL_OUTS 컬럼 뜻: 아이디 · 생물 종 · 입양일 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 아직 입양을 못 간 동물 중 보호 시작일이 가장 이른 3마리의 이름과 보호 시작일을 보호 시작일 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 짝이 없는지를 `O.NAME IS NULL`로 검사해 이름 없이 입양 간 동물까지 섞여 나옴

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
아직 입양을 못 간 동물 중 보호 시작일이 가장 이른 3마리의 이름과 보호 시작일을 보호 시작일 순서로 조회하려고 해.
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
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I
LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.NAME IS NULL
ORDER BY I.DATETIME
LIMIT 3;
```
- 기대한 결과: 3행, 앞 2행: (Shelly, 2015-01-29 15:01:00) / (Jackie, 2016-01-03 16:25:00) …
- 실제 결과: 3행, 앞 2행: (NULL, 2014-06-08 13:20:00) / (Shelly, 2015-01-29 15:01:00) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 10. 오랜 기간 보호한 동물(2)

- Level 3 · 프로그래머스 59411 · https://school.programmers.co.kr/learn/courses/30/lessons/59411

### 정답 SQL

```sql
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC
LIMIT 2;
```

- 결과: 2행
- 풀이 핵심: `JOIN` 뒤 `DATEDIFF(O.DATETIME, I.DATETIME)`로 보호 기간을 구해 내림차순 정렬하고 `LIMIT 2`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- ANIMAL_INS 컬럼 뜻: 아이디 · 생물 종 · 보호 시작일 · 보호 시작 시 상태 · 이름 · 성별 및 중성화 여부
- ANIMAL_OUTS 컬럼 뜻: 아이디 · 생물 종 · 입양일 · 이름 · 성별 및 중성화 여부
- 내가 이해한 문제: 입양 간 동물 중 보호 기간(입양일 - 보호 시작일)이 가장 길었던 2마리의 아이디와 이름을 보호 기간이 긴 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `DATEDIFF`의 두 날짜 순서를 바꿔 써서 보호 기간이 가장 짧은 동물이 나옴

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
입양 간 동물 중 보호 기간(입양일 - 보호 시작일)이 가장 길었던 2마리의 아이디와 이름을 보호 기간이 긴 순서로 조회하려고 해.
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
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
JOIN ANIMAL_OUTS O ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY DATEDIFF(I.DATETIME, O.DATETIME) DESC
LIMIT 2;
```
- 기대한 결과: 2행 (A362707, Girly Girl) / (A370507, Emily)
- 실제 결과: 2행 (A362383, *Morado) / (A381217, Cherokee)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 11. 카테고리 별 도서 판매량 집계하기

- Level 3 · 프로그래머스 144855 · https://school.programmers.co.kr/learn/courses/30/lessons/144855

### 정답 SQL

```sql
SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK B
JOIN BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID
WHERE S.SALES_DATE >= '2022-01-01' AND S.SALES_DATE < '2022-02-01'
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY;
```

- 결과: 5행
- 풀이 핵심: 도서와 판매를 `BOOK_ID`로 `JOIN`하고 1월만 거른 뒤 `GROUP BY B.CATEGORY`로 묶어 `SUM`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
BOOK_SALES 테이블 구조:
+------------+---------+------+-----+---------+-------+
| Field      | Type    | Null | Key | Default | Extra |
+------------+---------+------+-----+---------+-------+
| BOOK_ID    | int(11) | NO   |     | NULL    |       |
| SALES_DATE | date    | NO   |     | NULL    |       |
| SALES      | int(11) | NO   |     | NULL    |       |
+------------+---------+------+-----+---------+-------+
- BOOK 컬럼 뜻: 도서 ID · 카테고리 · 저자 ID · 판매가(원) · 출판일
- BOOK_SALES 컬럼 뜻: 도서 ID · 판매일 · 판매량
- 내가 이해한 문제: 2022년 1월 판매량을 카테고리별로 합산해 카테고리와 총 판매량(TOTAL_SALES)을 카테고리 이름 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `GROUP BY`를 `B.BOOK_ID`로 잡아 카테고리가 도서마다 따로 여러 번 나옴

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
2022년 1월 판매량을 카테고리별로 합산해 카테고리와 총 판매량(TOTAL_SALES)을 카테고리 이름 순서로 조회하려고 해.
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
BOOK_SALES 테이블 구조:
+------------+---------+------+-----+---------+-------+
| Field      | Type    | Null | Key | Default | Extra |
+------------+---------+------+-----+---------+-------+
| BOOK_ID    | int(11) | NO   |     | NULL    |       |
| SALES_DATE | date    | NO   |     | NULL    |       |
| SALES      | int(11) | NO   |     | NULL    |       |
+------------+---------+------+-----+---------+-------+
```sql
SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK B
JOIN BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID
WHERE S.SALES_DATE >= '2022-01-01' AND S.SALES_DATE < '2022-02-01'
GROUP BY B.BOOK_ID
ORDER BY B.CATEGORY;
```
- 기대한 결과: 5행, 앞 2행: (경제, 101) / (기술, 151) …
- 실제 결과: 7행, 앞 2행: (경제, 66) / (경제, 35) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 12. 조건에 맞는 사용자와 총 거래금액 조회하기

- Level 3 · 프로그래머스 164668 · https://school.programmers.co.kr/learn/courses/30/lessons/164668

### 정답 SQL

```sql
SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS = 'DONE'
GROUP BY U.USER_ID, U.NICKNAME
HAVING SUM(B.PRICE) >= 700000
ORDER BY TOTAL_SALES;
```

- 결과: 3행
- 풀이 핵심: 행 조건(`STATUS = 'DONE'`)은 `WHERE`, 묶은 뒤의 합계 조건(`SUM(B.PRICE) >= 700000`)은 `HAVING`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
USED_GOODS_USER 테이블 구조:
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| USER_ID         | varchar(50)  | NO   | PRI | NULL    |       |
| NICKNAME        | varchar(100) | YES  |     | NULL    |       |
| CITY            | varchar(100) | YES  |     | NULL    |       |
| STREET_ADDRESS1 | varchar(100) | YES  |     | NULL    |       |
| STREET_ADDRESS2 | varchar(100) | YES  |     | NULL    |       |
| TLNO            | varchar(20)  | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
- USED_GOODS_BOARD 컬럼 뜻: 게시글 ID · 작성자 ID · 게시글 제목 · 게시글 내용 · 가격 · 작성일 · 거래상태 · 조회수
- USED_GOODS_USER 컬럼 뜻: 회원 ID · 닉네임 · 시 · 도로명 주소 · 상세 주소 · 전화번호
- 내가 이해한 문제: 거래가 완료된 게시글의 가격 합계가 70만 원 이상인 회원의 회원 ID · 닉네임 · 총거래금액을 총거래금액 작은 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 합계 조건을 `HAVING` 대신 `WHERE`에 넣어 에러가 남

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
거래가 완료된 게시글의 가격 합계가 70만 원 이상인 회원의 회원 ID · 닉네임 · 총거래금액을 총거래금액 작은 순서로 조회하려고 해.
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
USED_GOODS_USER 테이블 구조:
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| USER_ID         | varchar(50)  | NO   | PRI | NULL    |       |
| NICKNAME        | varchar(100) | YES  |     | NULL    |       |
| CITY            | varchar(100) | YES  |     | NULL    |       |
| STREET_ADDRESS1 | varchar(100) | YES  |     | NULL    |       |
| STREET_ADDRESS2 | varchar(100) | YES  |     | NULL    |       |
| TLNO            | varchar(20)  | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
```sql
SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD B
JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS = 'DONE' AND SUM(B.PRICE) >= 700000
GROUP BY U.USER_ID, U.NICKNAME
ORDER BY TOTAL_SALES;
```
- 기대한 결과: 3행, 앞 2행: (zkzkdh1, 후후후, 700000) / (dhfkzmf09, 찐찐, 860000) …
- 실제 결과: ERROR 1111 (HY000): Invalid use of group function

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 13. 헤비 유저가 소유한 장소

- Level 3 · 프로그래머스 77487 · https://school.programmers.co.kr/learn/courses/30/lessons/77487

### 정답 SQL

```sql
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(*) >= 2
)
ORDER BY ID;
```

- 결과: 5행
- 풀이 핵심: 서브쿼리에서 `GROUP BY HOST_ID` + `HAVING COUNT(*) >= 2`로 헤비 유저를 찾고 바깥에서 `IN`으로 고름

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
PLACES 테이블 구조:
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| ID      | int(11)     | NO   | PRI | NULL    |       |
| NAME    | varchar(61) | NO   |     | NULL    |       |
| HOST_ID | int(11)     | NO   |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
- 컬럼 뜻: 공간 아이디 · 공간 이름 · 공간을 소유한 유저의 아이디
- 내가 이해한 문제: 공간을 둘 이상 등록한 유저(헤비 유저)가 등록한 공간의 아이디 · 이름 · 소유 유저 아이디를 아이디 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 서브쿼리 앞에 `IN` 대신 `=`를 써서 에러가 남. 헤비 유저가 여러 명이라 서브쿼리가 여러 행을 돌려줌

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
공간을 둘 이상 등록한 유저(헤비 유저)가 등록한 공간의 아이디 · 이름 · 소유 유저 아이디를 아이디 순서로 조회하려고 해.
PLACES 테이블 구조:
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| ID      | int(11)     | NO   | PRI | NULL    |       |
| NAME    | varchar(61) | NO   |     | NULL    |       |
| HOST_ID | int(11)     | NO   |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
```sql
SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID = (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(*) >= 2
)
ORDER BY ID;
```
- 기대한 결과: 5행, 앞 2행: (4431977, BOUTIQUE STAYS - Somerset Terrace, Pet Friendly, 760849) / (5194998, BOUTIQUE STAYS - Elwood Beaches 3, Pet Friendly, 760849) …
- 실제 결과: ERROR 1242 (21000): Subquery returns more than 1 row

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 14. 조건에 맞는 사용자 정보 조회하기

- Level 3 · 프로그래머스 164670 · https://school.programmers.co.kr/learn/courses/30/lessons/164670

### 정답 SQL

```sql
SELECT USER_ID, NICKNAME,
       CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소,
       CONCAT(LEFT(TLNO, 3), '-', SUBSTRING(TLNO, 4, 4), '-', RIGHT(TLNO, 4)) AS 전화번호
FROM USED_GOODS_USER
WHERE USER_ID IN (
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(*) >= 3
)
ORDER BY USER_ID DESC;
```

- 결과: 11행
- 풀이 핵심: 서브쿼리에서 `GROUP BY WRITER_ID` + `HAVING COUNT(*) >= 3`으로 회원을 고르고, 주소와 전화번호는 `CONCAT` · `LEFT` · `SUBSTRING` · `RIGHT`로 만듦

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
USED_GOODS_USER 테이블 구조:
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| USER_ID         | varchar(50)  | NO   | PRI | NULL    |       |
| NICKNAME        | varchar(100) | YES  |     | NULL    |       |
| CITY            | varchar(100) | YES  |     | NULL    |       |
| STREET_ADDRESS1 | varchar(100) | YES  |     | NULL    |       |
| STREET_ADDRESS2 | varchar(100) | YES  |     | NULL    |       |
| TLNO            | varchar(20)  | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
- USED_GOODS_BOARD 컬럼 뜻: 게시글 ID · 작성자 ID · 게시글 제목 · 게시글 내용 · 가격 · 작성일 · 거래상태 · 조회수
- USED_GOODS_USER 컬럼 뜻: 회원 ID · 닉네임 · 시 · 도로명 주소 · 상세 주소 · 전화번호
- 내가 이해한 문제: 게시글을 3건 이상 등록한 회원의 회원 ID · 닉네임 · 전체 주소 · 전화번호를 회원 ID 큰 순서로 조회. 전체 주소는 시 · 도로명 주소 · 상세 주소를 띄어 이어 붙이고, 전화번호는 xxx-xxxx-xxxx 모양

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: '3건 이상'을 `HAVING COUNT(*) > 3`으로 써서 딱 3건 등록한 회원이 빠짐

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
게시글을 3건 이상 등록한 회원의 회원 ID · 닉네임 · 전체 주소 · 전화번호를 회원 ID 큰 순서로 조회하려고 해.
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
USED_GOODS_USER 테이블 구조:
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| USER_ID         | varchar(50)  | NO   | PRI | NULL    |       |
| NICKNAME        | varchar(100) | YES  |     | NULL    |       |
| CITY            | varchar(100) | YES  |     | NULL    |       |
| STREET_ADDRESS1 | varchar(100) | YES  |     | NULL    |       |
| STREET_ADDRESS2 | varchar(100) | YES  |     | NULL    |       |
| TLNO            | varchar(20)  | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
```sql
SELECT USER_ID, NICKNAME,
       CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소,
       CONCAT(LEFT(TLNO, 3), '-', SUBSTRING(TLNO, 4, 4), '-', RIGHT(TLNO, 4)) AS 전화번호
FROM USED_GOODS_USER
WHERE USER_ID IN (
    SELECT WRITER_ID
    FROM USED_GOODS_BOARD
    GROUP BY WRITER_ID
    HAVING COUNT(*) > 3
)
ORDER BY USER_ID DESC;
```
- 기대한 결과: 11행, 4번째 행부터: (s2s2123, 이회장, 성남시 분당구 정자로 2 1005동 1004호, 010-2211-6664) / (miyeon89, 러브러브, 성남시 분당구 내정로 152 C동 204호, 010-3211-6456) …
- 실제 결과: 7행, 4번째 행부터: (miyeon89, 러브러브, 성남시 분당구 내정로 152 C동 204호, 010-3211-6456) / (hong02, 자바한명, 성남시 분당구 정자일로 210 4동 501호, 010-2203-9488) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 15. 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기

- Level 3 · 프로그래머스 164671 · https://school.programmers.co.kr/learn/courses/30/lessons/164671

### 정답 SQL

```sql
SELECT CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 0, 1
)
ORDER BY FILE_ID DESC;
```

- 결과: 2행
- 풀이 핵심: 서브쿼리에서 조회수 내림차순 `LIMIT 0, 1`로 게시글 ID 하나를 구하고, 경로는 `CONCAT`으로 이어 붙임

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
USED_GOODS_FILE 테이블 구조:
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| FILE_ID   | varchar(10)  | NO   | PRI | NULL    |       |
| FILE_EXT  | varchar(5)   | YES  |     | NULL    |       |
| FILE_NAME | varchar(256) | YES  |     | NULL    |       |
| BOARD_ID  | varchar(10)  | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
- USED_GOODS_BOARD 컬럼 뜻: 게시글 ID · 작성자 ID · 게시글 제목 · 게시글 내용 · 가격 · 작성일 · 거래상태 · 조회수
- USED_GOODS_FILE 컬럼 뜻: 파일 ID · 파일 확장자 · 파일 이름 · 게시글 ID
- 내가 이해한 문제: 조회수가 가장 높은 게시글의 첨부파일 경로(/home/grep/src/게시글 ID/파일 ID 파일 이름 파일 확장자)를 파일 ID 큰 순서로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 서브쿼리가 게시글 ID가 아니라 가장 큰 조회수를 돌려줘 게시글 ID와 비교하게 되어 결과가 비어 있음

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
조회수가 가장 높은 게시글의 첨부파일 경로(/home/grep/src/게시글 ID/파일 ID 파일 이름 파일 확장자)를 파일 ID 큰 순서로 조회하려고 해.
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
USED_GOODS_FILE 테이블 구조:
+-----------+--------------+------+-----+---------+-------+
| Field     | Type         | Null | Key | Default | Extra |
+-----------+--------------+------+-----+---------+-------+
| FILE_ID   | varchar(10)  | NO   | PRI | NULL    |       |
| FILE_EXT  | varchar(5)   | YES  |     | NULL    |       |
| FILE_NAME | varchar(256) | YES  |     | NULL    |       |
| BOARD_ID  | varchar(10)  | YES  |     | NULL    |       |
+-----------+--------------+------+-----+---------+-------+
```sql
SELECT CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (
    SELECT MAX(VIEWS)
    FROM USED_GOODS_BOARD
)
ORDER BY FILE_ID DESC;
```
- 기대한 결과: 2행 (/home/grep/src/B0008/MOV_000008photo1.avi) / (/home/grep/src/B0008/IMG_000011photo.png)
- 실제 결과: 0행 (결과가 비어 있음)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 16. 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기

- Level 3 · 프로그래머스 151139 · https://school.programmers.co.kr/learn/courses/30/lessons/151139

### 정답 SQL

```sql
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE >= '2022-08-01' AND START_DATE < '2022-11-01'
  AND CAR_ID IN (
      SELECT CAR_ID
      FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
      WHERE START_DATE >= '2022-08-01' AND START_DATE < '2022-11-01'
      GROUP BY CAR_ID
      HAVING COUNT(*) >= 5
  )
GROUP BY MONTH(START_DATE), CAR_ID
ORDER BY MONTH, CAR_ID DESC;
```

- 결과: 42행
- 풀이 핵심: 서브쿼리에서 기간 안 대여가 5회 이상인 자동차를 고르고, 바깥에서 같은 기간을 다시 걸러 월 · 자동차로 묶어 `COUNT(*)`

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

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
- 내가 이해한 문제: 대여 시작일이 2022년 8월~10월인 기록이 5회 이상인 자동차의 월별 대여 횟수(RECORDS)를 월 순서, 같으면 자동차 ID 큰 순서로 조회. 대여 횟수가 0인 달은 결과에서 뺌

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 서브쿼리 없이 월별로 묶은 뒤 `HAVING COUNT(*) >= 5`를 걸어 석 달 합계가 아니라 한 달에 5회 이상인 경우만 남음

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
대여 시작일이 2022년 8월~10월인 기록이 5회 이상인 자동차의 월별 대여 횟수(RECORDS)를 월 순서, 같으면 자동차 ID 큰 순서로 조회하려고 해.
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
SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE >= '2022-08-01' AND START_DATE < '2022-11-01'
GROUP BY MONTH(START_DATE), CAR_ID
HAVING COUNT(*) >= 5
ORDER BY MONTH, CAR_ID DESC;
```
- 기대한 결과: 42행, 앞 2행: (8, 28, 3) / (8, 27, 5) …
- 실제 결과: 12행, 앞 2행: (8, 27, 5) / (8, 25, 5) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 17. 즐겨찾기가 가장 많은 식당 정보 출력하기

- Level 3 · 프로그래머스 131123 · https://school.programmers.co.kr/learn/courses/30/lessons/131123

### 정답 SQL

```sql
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE (FOOD_TYPE, FAVORITES) IN (
    SELECT FOOD_TYPE, MAX(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC;
```

- 결과: 5행
- 풀이 핵심: 서브쿼리에서 음식 종류별 최대 즐겨찾기수를 구하고, 바깥에서 `(FOOD_TYPE, FAVORITES)` 두 값을 함께 `IN`으로 비교함

### 방향 묻기 프롬프트

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
REST_INFO 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| REST_ID     | varchar(5)   | NO   | PRI | NULL    |       |
| REST_NAME   | varchar(50)  | YES  |     | NULL    |       |
| FOOD_TYPE   | varchar(20)  | YES  |     | NULL    |       |
| VIEWS       | int(11)      | YES  |     | NULL    |       |
| FAVORITES   | int(11)      | YES  |     | NULL    |       |
| PARKING_LOT | varchar(1)   | YES  |     | NULL    |       |
| ADDRESS     | varchar(100) | YES  |     | NULL    |       |
| TEL         | varchar(100) | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
- 컬럼 뜻: 식당 ID · 식당 이름 · 음식 종류 · 조회수 · 즐겨찾기수 · 주차장 유무 · 주소 · 전화번호
- 내가 이해한 문제: 음식 종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류 · 식당 ID · 식당 이름 · 즐겨찾기수를 음식 종류 내림차순으로 조회

## 질문
내 이해가 맞는지 봐 주고, 필요한 절과 순서를 알려줘.

## 제약
- SELECT · WHERE · ORDER BY · LIMIT · SQL 함수 · GROUP BY · HAVING · JOIN · UNION · 서브쿼리 범위 안에서만

## 출력 형식
| 순서 | 절 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 즐겨찾기수만 `IN`으로 비교해 다른 음식 종류의 최댓값과 우연히 같은 식당까지 나옴

````md
## 맥락
SQL 고급 데이터 조회를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
음식 종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류 · 식당 ID · 식당 이름 · 즐겨찾기수를 음식 종류 내림차순으로 조회하려고 해.
REST_INFO 테이블 구조:
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| REST_ID     | varchar(5)   | NO   | PRI | NULL    |       |
| REST_NAME   | varchar(50)  | YES  |     | NULL    |       |
| FOOD_TYPE   | varchar(20)  | YES  |     | NULL    |       |
| VIEWS       | int(11)      | YES  |     | NULL    |       |
| FAVORITES   | int(11)      | YES  |     | NULL    |       |
| PARKING_LOT | varchar(1)   | YES  |     | NULL    |       |
| ADDRESS     | varchar(100) | YES  |     | NULL    |       |
| TEL         | varchar(100) | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
```sql
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO
WHERE FAVORITES IN (
    SELECT MAX(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC;
```
- 기대한 결과: 5행, 2번째 행부터: (중식, 00015, 만정, 20) / (일식, 00004, 스시사카우스, 230) …
- 실제 결과: 6행, 2번째 행부터: (한식, 00016, 오대산산채전문점, 230) / (중식, 00015, 만정, 20) …

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

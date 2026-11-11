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

<p class="sub">[LAB-06] 고급 데이터 조회 (6) / ITWILL - 주영아·이광호 강사</p>

---
layout: section
---

# SQL 코딩 테스트

앞서 배운 상황별 템플릿으로 프롬프트를 직접 작성하여 문제를 풀어보세요

---
class: tight
---

## #01. 문제 1 — 과일로 만든 아이스크림 고르기

다음은 아이스크림 가게의 상반기 주문 정보를 담은 `FIRST_HALF` 테이블과 아이스크림 성분에 대한 정보를 담은 `ICECREAM_INFO` 테이블입니다. `FIRST_HALF` 테이블 구조는 다음과 같으며, `SHIPMENT_ID`, `FLAVOR`, `TOTAL_ORDER` 는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량을 나타냅니다. `FIRST_HALF` 테이블의 기본 키는 `FLAVOR`입니다.

`ICECREAM_INFO` 테이블 구조는 다음과 같으며, `FLAVOR`, `INGREDITENT_TYPE` 은 각각 아이스크림 맛, 아이스크림의 성분 타입을 나타냅니다. `INGREDIENT_TYPE`에는 아이스크림의 주 성분이 설탕이면 `sugar_based`라고 입력되고, 아이스크림의 주 성분이 과일이면 `fruit_based`라고 입력됩니다. `ICECREAM_INFO`의 기본 키는 `FLAVOR`입니다. `ICECREAM_INFO`테이블의 `FLAVOR`는 `FIRST_HALF` 테이블의 `FLAVOR`의 외래 키입니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 133025">

상반기 아이스크림 총주문량이 3,000보다 높으면서 아이스크림의 주 성분이 과일인 아이스크림의 맛을 총주문량이 큰 순서대로 조회하는 SQL 문을 작성해주세요.

</Callout>

---

### #01-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">FIRST_HALF</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| SHIPMENT_ID | INT(N) | FALSE |
| FLAVOR | VARCHAR(N) | FALSE |
| TOTAL_ORDER | INT(N) | FALSE |

</div>
<div>

<div class="kicker">ICECREAM_INFO</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| FLAVOR | VARCHAR(N) | FALSE |
| INGREDIENT_TYPE | VARCHAR(N) | FALSE |

</div>
</Grid>

---

### #01-2. 입출력 예시 (2)

예를 들어 `FIRST_HALF` 테이블이 다음과 같고

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

### #01-3. 입출력 예시 (3)

`ICECREAM_INFO` 테이블이 다음과 같다면

<Grid cols="2" align="start">
<div>

| FLAVOR | INGREDIENT_TYPE |
| --- | --- |
| chocolate | sugar_based |
| vanilla | sugar_based |
| mint_chocolate | sugar_based |
| caramel | sugar_based |
| white_chocolate | sugar_based |
| peach | fruit_based |

</div>
<div>

| FLAVOR | INGREDIENT_TYPE |
| --- | --- |
| watermelon | fruit_based |
| mango | fruit_based |
| strawberry | fruit_based |
| melon | fruit_based |
| orange | fruit_based |
| pineapple | fruit_based |

</div>
</Grid>

---

### #01-4. 입출력 예시 (4)

상반기 아이스크림 총주문량이 3,000보다 높은 아이스크림 맛은 chocolate, strawberry, melon, white_chocolate입니다. 이 중에 아이스크림의 주 성분이 과일인 아이스크림 맛은 strawberry와 melon이고 총주문량이 큰 순서대로 아이스크림 맛을 조회하면 melon, strawberry 순으로 조회되어야 합니다. 따라서 SQL 문을 실행하면 다음과 같이 나와야 합니다.

| FLAVOR |
| --- |
| melon |
| strawberry |

---
class: tight
---

## #02. 문제 2 — 조건에 부합하는 중고거래 댓글 조회하기

다음은 중고거래 게시판 정보를 담은 `USED_GOODS_BOARD` 테이블과 중고거래 게시판 첨부파일 정보를 담은 `USED_GOODS_REPLY` 테이블입니다. `USED_GOODS_BOARD` 테이블은 다음과 같으며 `BOARD_ID`, `WRITER_ID`, `TITLE`, `CONTENTS`, `PRICE`, `CREATED_DATE`, `STATUS`, `VIEWS`은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.

`USED_GOODS_REPLY` 테이블은 다음과 같으며 `REPLY_ID`, `BOARD_ID`, `WRITER_ID`, `CONTENTS`, `CREATED_DATE`는 각각 댓글 ID, 게시글 ID, 작성자 ID, 댓글 내용, 작성일을 의미합니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 164673">

`USED_GOODS_BOARD`와 `USED_GOODS_REPLY` 테이블에서 2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요. 결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #02-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">USED_GOODS_BOARD</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| BOARD_ID | VARCHAR(5) | FALSE |
| WRITER_ID | VARCHAR(50) | FALSE |
| TITLE | VARCHAR(100) | FALSE |
| CONTENTS | VARCHAR(1000) | FALSE |
| PRICE | NUMBER | FALSE |
| CREATED_DATE | DATE | FALSE |
| STATUS | VARCHAR(10) | FALSE |
| VIEWS | NUMBER | FALSE |

</div>
<div>

<div class="kicker">USED_GOODS_REPLY</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| REPLY_ID | VARCHAR(10) | FALSE |
| BOARD_ID | VARCHAR(5) | FALSE |
| WRITER_ID | VARCHAR(50) | FALSE |
| CONTENTS | VARCHAR(1000) | TRUE |
| CREATED_DATE | DATE | FALSE |

</div>
</Grid>

---

### #02-2. 입출력 예시 (2)

`USED_GOODS_BOARD` 테이블이 다음과 같고

| BOARD_ID | WRITER_ID | TITLE | CONTENTS | PRICE | CREATED_DATE | STATUS | VIEWS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B0001 | kwag98 | 반려견 배변패드 팝니다 | 정말 저렴히 판매합니다. 전부 미개봉 새상품입니다. | 12000 | 2022-10-01 | DONE | 250 |
| B0002 | lee871201 | 국내산 볶음참깨 | 직접 농사지은 참깨입니다. | 3000 | 2022-10-02 | DONE | 121 |
| B0003 | goung12 | 배드민턴 라켓 | 사놓고 방치만 해서 팝니다. | 9000 | 2022-10-02 | SALE | 212 |
| B0004 | keel1990 | 디올 귀걸이 | 신세계강남점에서 구입. 정품 아닐시 백퍼센트 환불 | 130000 | 2022-10-02 | SALE | 199 |
| B0005 | haphli01 | 스팸클래식 팔아요 | 유통기한 2025년까지에요 | 10000 | 2022-10-02 | SALE | 121 |

---

### #02-3. 입출력 예시 (3)

`USED_GOODS_REPLY` 테이블이 다음과 같을 때

| REPLY_ID | BOARD_ID | WRITER_ID | CONTENTS | CREATED_DATE |
| --- | --- | --- | --- | --- |
| R000000001 | B0001 | s2s2123 | 구매하겠습니다. 쪽지 드립니다. | 2022-10-02 |
| R000000002 | B0002 | hoho1112 | 쪽지 주세요. | 2022-10-03 |
| R000000003 | B0006 | hwahwa2 | 삽니다. 연락주세요. | 2022-10-03 |
| R000000004 | B0007 | hong02 | 예약중 | 2022-10-06 |
| R000000005 | B0009 | hanju23 | 구매완료 | 2022-10-07 |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| TITLE | BOARD_ID | REPLY_ID | WRITER_ID | CONTENTS | CREATED_DATE |
| --- | --- | --- | --- | --- | --- |
| 반려견 배변패드 팝니다 | B0001 | R000000001 | s2s2123 | 구매하겠습니다. 쪽지 드립니다. | 2022-10-02 |
| 국내산 볶음참깨 | B0002 | R000000002 | hoho1112 | 쪽지 주세요. | 2022-10-03 |

---
class: tight
---

## #03. 문제 3 — 조건에 맞는 도서와 저자 리스트 출력하기

다음은 어느 한 서점에서 판매중인 도서들의 도서 정보(`BOOK`), 저자 정보(`AUTHOR`) 테이블입니다.

`BOOK` 테이블은 각 도서의 정보를 담은 테이블로 아래와 같은 구조로 되어있습니다.

`AUTHOR` 테이블은 도서의 저자의 정보를 담은 테이블로 아래와 같은 구조로 되어있습니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 144854">

`'경제'` 카테고리에 속하는 도서들의 도서 ID(`BOOK_ID`), 저자명(`AUTHOR_NAME`), 출판일(`PUBLISHED_DATE`) 리스트를 출력하는 SQL문을 작성해주세요.     결과는 출판일을 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #03-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">BOOK</div>

| Column name | Type | Nullable | Description |
| --- | --- | --- | --- |
| BOOK_ID | INTEGER | FALSE | 도서 ID |
| CATEGORY | VARCHAR(N) | FALSE | 카테고리 (경제, 인문, 소설, 생활, 기술) |
| AUTHOR_ID | INTEGER | FALSE | 저자 ID |
| PRICE | INTEGER | FALSE | 판매가 (원) |
| PUBLISHED_DATE | DATE | FALSE | 출판일 |

</div>
<div>

<div class="kicker">AUTHOR</div>

| Column name | Type | Nullable | Description |
| --- | --- | --- | --- |
| AUTHOR_ID | INTEGER | FALSE | 저자 ID |
| AUTHOR_NAME | VARCHAR(N) | FALSE | 저자명 |

</div>
</Grid>

---

### #03-2. 입출력 예시 (2)

예를 들어 `BOOK` 테이블과 `AUTHOR` 테이블이 다음과 같다면

| BOOK_ID | CATEGORY | AUTHOR_ID | PRICE | PUBLISHED_DATE |
| --- | --- | --- | --- | --- |
| 1 | 인문 | 1 | 10000 | 2020-01-01 |
| 2 | 경제 | 1 | 9000 | 2021-04-11 |
| 3 | 경제 | 2 | 11000 | 2021-02-05 |

| AUTHOR_ID | AUTHOR_NAME |
| --- | --- |
| 1 | 홍길동 |
| 2 | 김영호 |

---

### #03-3. 입출력 예시 (3)

`'경제'` 카테고리에 속하는 도서는 도서 ID가 2, 3인 도서이고, 출판일을 기준으로 오름차순으로 정렬하면 다음과 같은 결과가 나와야 합니다.

| BOOK_ID | AUTHOR_NAME | PUBLISHED_DATE |
| --- | --- | --- |
| 3 | 김영호 | 2021-02-05 |
| 2 | 홍길동 | 2021-04-11 |

---
class: tight
---

## #04. 문제 4 — 성분으로 구분한 아이스크림 총 주문량

다음은 아이스크림 가게의 상반기 주문 정보를 담은 `FIRST_HALF` 테이블과 아이스크림 성분에 대한 정보를 담은 `ICECREAM_INFO` 테이블입니다. `FIRST_HALF` 테이블 구조는 다음과 같으며, `SHIPMENT_ID`, `FLAVOR`, `TOTAL_ORDER` 는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량을 나타냅니다. `FIRST_HALF` 테이블의 기본 키는 `FLAVOR`입니다.

`ICECREAM_INFO` 테이블 구조는 다음과 같으며, `FLAVOR`, `INGREDITENT_TYPE` 은 각각 아이스크림 맛, 아이스크림의 성분 타입을 나타냅니다. `INGREDIENT_TYPE`에는 아이스크림의 주 성분이 설탕이면 `sugar_based`라고 입력되고, 아이스크림의 주 성분이 과일이면 `fruit_based`라고 입력됩니다. `ICECREAM_INFO`의 기본 키는 `FLAVOR`입니다. `ICECREAM_INFO`테이블의 `FLAVOR`는 `FIRST_HALF` 테이블의 `FLAVOR`의 외래 키입니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 133026">

상반기 동안 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림의 총주문량을 총주문량이 작은 순서대로 조회하는 SQL 문을 작성해주세요. 이때 총주문량을 나타내는 컬럼명은 TOTAL_ORDER로 지정해주세요.

</Callout>

---

### #04-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">FIRST_HALF</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| SHIPMENT_ID | INT(N) | FALSE |
| FLAVOR | VARCHAR(N) | FALSE |
| TOTAL_ORDER | INT(N) | FALSE |

</div>
<div>

<div class="kicker">ICECREAM_INFO</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| FLAVOR | VARCHAR(N) | FALSE |
| INGREDIENT_TYPE | VARCHAR(N) | FALSE |

</div>
</Grid>

---

### #04-2. 입출력 예시 (2)

예를 들어 `FIRST_HALF` 테이블이 다음과 같고

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

### #04-3. 입출력 예시 (3)

`ICECREAM_INFO` 테이블이 다음과 같다면

<Grid cols="2" align="start">
<div>

| FLAVOR | INGREDIENT_TYPE |
| --- | --- |
| chocolate | sugar_based |
| vanilla | sugar_based |
| mint_chocolate | sugar_based |
| caramel | sugar_based |
| white_chocolate | sugar_based |
| peach | fruit_based |

</div>
<div>

| FLAVOR | INGREDIENT_TYPE |
| --- | --- |
| watermelon | fruit_based |
| mango | fruit_based |
| strawberry | fruit_based |
| melon | fruit_based |
| orange | fruit_based |
| pineapple | fruit_based |

</div>
</Grid>

---

### #04-4. 입출력 예시 (4)

상반기에 아이스크림의 주 성분이 설탕인 아이스크림들에 대한 총주문량을 구하면 3,200 + 2,800 + 1,700 + 2,600 + 3,100 = 13,400입니다. 아이스크림의 주 성분이 과일인 아이스크림들에 대한 총주문량을 구하면 3,100 + 2,450 + 2,150 + 2,900 + 3,150 + 2,900 + 2,900 = 19,550입니다. 따라서 총주문량이 작은 순서대로 조회하는 SQL 문을 실행하면 다음과 같이 나와야 합니다.

| INGREDIENT_TYPE | TOTAL_ORDER |
| --- | --- |
| sugar_based | 13400 |
| fruit_based | 19550 |

---
class: tight
---

## #05. 문제 5 — 상품 별 오프라인 매출 구하기

다음은 어느 의류 쇼핑몰에서 판매중인 상품들의 상품 정보를 담은 `PRODUCT` 테이블과 오프라인 상품 판매 정보를 담은 `OFFLINE_SALE` 테이블 입니다. `PRODUCT` 테이블은 아래와 같은 구조로 `PRODUCT_ID`, `PRODUCT_CODE`, `PRICE`는 각각 상품 ID, 상품코드, 판매가를 나타냅니다.

상품 별로 중복되지 않는 8자리 상품코드 값을 가지며, 앞 2자리는 카테고리 코드를 의미합니다.

`OFFLINE_SALE` 테이블은 아래와 같은 구조로 되어있으며 `OFFLINE_SALE_ID`, `PRODUCT_ID`, `SALES_AMOUNT`, `SALES_DATE`는 각각 오프라인 상품 판매 ID, 상품 ID, 판매량, 판매일을 나타냅니다.

동일한 날짜, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 131533">

`PRODUCT` 테이블과 `OFFLINE_SALE` 테이블에서 상품코드 별 매출액(판매가 * 판매량) 합계를 출력하는 SQL문을 작성해주세요. 결과는 매출액을 기준으로 내림차순 정렬해주시고 매출액이 같다면 상품코드를 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #05-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">PRODUCT</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| PRODUCT_ID | INTEGER | FALSE |
| PRODUCT_CODE | VARCHAR(8) | FALSE |
| PRICE | INTEGER | FALSE |

</div>
<div>

<div class="kicker">OFFLINE_SALE</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| OFFLINE_SALE_ID | INTEGER | FALSE |
| PRODUCT_ID | INTEGER | FALSE |
| SALES_AMOUNT | INTEGER | FALSE |
| SALES_DATE | DATE | FALSE |

</div>
</Grid>

---

### #05-2. 입출력 예시 (2)

예를 들어 `PRODUCT` 테이블이 다음과 같고

| PRODUCT_ID | PRODUCT_CODE | PRICE |
| --- | --- | --- |
| 1 | A1000011 | 15000 |
| 2 | A1000045 | 8000 |
| 3 | C3000002 | 42000 |

---

### #05-3. 입출력 예시 (3)

`OFFLINE_SALE` 테이블이 다음과 같다면

| OFFLINE_SALE_ID | PRODUCT_ID | SALES_AMOUNT | SALES_DATE |
| --- | --- | --- | --- |
| 1 | 1 | 2 | 2022-02-21 |
| 2 | 1 | 2 | 2022-03-02 |
| 3 | 3 | 3 | 2022-05-01 |
| 4 | 2 | 1 | 2022-05-24 |
| 5 | 1 | 2 | 2022-07-14 |
| 6 | 2 | 1 | 2022-09-22 |

각 상품 별 총 판매량과 판매가는 다음과 같습니다.

---

### #05-4. 입출력 예시 (4)

- `PRODUCT_CODE` 가 `A1000011`인 상품은 총 판매량이 6개, 판매가가 15,000원
- `PRODUCT_CODE` 가 `A1000045`인 상품은 총 판매량이 2개, 판매가가 8,000원
- `PRODUCT_CODE` 가 `C3000002`인 상품은 총 판매량이 3개, 판매가가 42,000원

그러므로 각 상품 별 매출액을 계산하고 정렬하면 결과가 다음과 같이 나와야 합니다.

| PRODUCT_CODE | SALES |
| --- | --- |
| C3000002 | 126000 |
| A1000011 | 90000 |
| A1000045 | 16000 |

---
class: tight
---

## #06. 문제 6 — 대여 기록이 존재하는 자동차 리스트 구하기

다음은 어느 자동차 대여 회사에서 대여 중인 자동차들의 정보를 담은 `CAR_RENTAL_COMPANY_CAR` 테이블과 자동차 대여 기록 정보를 담은 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블입니다. `CAR_RENTAL_COMPANY_CAR` 테이블은 아래와 같은 구조로 되어있으며, `CAR_ID`, `CAR_TYPE`, `DAILY_FEE`, `OPTIONS` 는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트를 나타냅니다.

자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 이 있습니다. 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트(예: '열선시트', '스마트키', '주차감지센서')로 되어있으며, 키워드 종류는 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 가 있습니다.

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블은 아래와 같은 구조로 되어있으며, `HISTORY_ID`, `CAR_ID`, `START_DATE`, `END_DATE` 는 각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일을 나타냅니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 157341">

`CAR_RENTAL_COMPANY_CAR` 테이블과 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력하는 SQL문을 작성해주세요. 자동차 ID 리스트는 중복이 없어야 하며, 자동차 ID를 기준으로 내림차순 정렬해주세요.

</Callout>

---

### #06-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">CAR_RENTAL_COMPANY_CAR</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| CAR_ID | INTEGER | FALSE |
| CAR_TYPE | VARCHAR(255) | FALSE |
| DAILY_FEE | INTEGER | FALSE |
| OPTIONS | VARCHAR(255) | FALSE |

</div>
<div>

<div class="kicker">CAR_RENTAL_COMPANY_RENTAL_HISTORY</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| HISTORY_ID | INTEGER | FALSE |
| CAR_ID | INTEGER | FALSE |
| START_DATE | DATE | FALSE |
| END_DATE | DATE | FALSE |

</div>
</Grid>

---

### #06-2. 입출력 예시 (2)

예를 들어 `CAR_RENTAL_COMPANY_CAR` 테이블이 다음과 같고

| CAR_ID | CAR_TYPE | DAILY_FEE | OPTIONS |
| --- | --- | --- | --- |
| 1 | 세단 | 16000 | 가죽시트,열선시트,후방카메라 |
| 2 | SUV | 14000 | 스마트키,네비게이션,열선시트 |
| 3 | 세단 | 22000 | 주차감지센서,후방카메라,가죽시트 |
| 4 | 세단 | 12000 | 주차감지센서 |

---

### #06-3. 입출력 예시 (3)

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블이 다음과 같다면

| HISTORY_ID | CAR_ID | START_DATE | END_DATE |
| --- | --- | --- | --- |
| 1 | 4 | 2022-09-27 | 2022-09-27 |
| 2 | 3 | 2022-10-03 | 2022-10-04 |
| 3 | 2 | 2022-10-05 | 2022-10-05 |
| 4 | 1 | 2022-10-11 | 2022-10-14 |
| 5 | 3 | 2022-10-13 | 2022-10-15 |

10월에 대여를 시작한 기록이 있는 '세단' 종류의 자동차는 자동차 ID가 1, 3 인 자동차이고, 자동차 ID를 기준으로 내림차순 정렬하면 다음과 같이 나와야 합니다.

| CAR_ID |
| --- |
| 3 |
| 1 |

---
class: tight
---

## #07. 문제 7 — 있었는데요 없었습니다

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

`ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다. `ANIMAL_OUTS` 테이블의 `ANIMAL_ID`는 `ANIMAL_INS`의 `ANIMAL_ID`의 외래 키입니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 59043">

관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.

</Callout>

---

### #07-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">ANIMAL_INS</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
<div>

<div class="kicker">ANIMAL_OUTS</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_OUTCOME | VARCHAR(N) | FALSE |

</div>
</Grid>

---

### #07-2. 입출력 예시 (2)

예를 들어, `ANIMAL_INS` 테이블과 `ANIMAL_OUTS` 테이블이 다음과 같다면

`ANIMAL_INS`

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A350276 | Cat | 2017-08-13 13:50:00 | Normal | Jewel | Spayed Female |
| A381217 | Dog | 2017-07-08 09:41:00 | Sick | Cherokee | Neutered Male |

`ANIMAL_OUTS`

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | NAME | SEX_UPON_OUTCOME |
| --- | --- | --- | --- | --- |
| A350276 | Cat | 2018-01-28 17:51:00 | Jewel | Spayed Female |
| A381217 | Dog | 2017-06-09 18:51:00 | Cherokee | Neutered Male |

---

### #07-3. 입출력 예시 (3)

SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME |
| --- | --- |
| A381217 | Cherokee |

---
class: tight
---

## #08. 문제 8 — 없어진 기록 찾기

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

`ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다. `ANIMAL_OUTS` 테이블의 `ANIMAL_ID`는 `ANIMAL_INS`의 `ANIMAL_ID`의 외래 키입니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 59042">

천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.

</Callout>

---

### #08-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">ANIMAL_INS</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
<div>

<div class="kicker">ANIMAL_OUTS</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_OUTCOME | VARCHAR(N) | FALSE |

</div>
</Grid>

---

### #08-2. 입출력 예시 (2)

예를 들어, `ANIMAL_INS` 테이블과 `ANIMAL_OUTS` 테이블이 다음과 같다면

`ANIMAL_INS`

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A352713 | Cat | 2017-04-13 16:29:00 | Normal | Gia | Spayed Female |
| A350375 | Cat | 2017-03-06 15:01:00 | Normal | Meo | Neutered Male |

---

### #08-3. 입출력 예시 (3)

`ANIMAL_OUTS`

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | NAME | SEX_UPON_OUTCOME |
| --- | --- | --- | --- | --- |
| A349733 | Dog | 2017-09-27 19:09:00 | Allie | Spayed Female |
| A352713 | Cat | 2017-04-25 12:25:00 | Gia | Spayed Female |
| A349990 | Cat | 2018-02-02 14:18:00 | Spice | Spayed Female |

`ANIMAL_OUTS` 테이블에서

- Allie의 ID는 `ANIMAL_INS`에 없으므로, Allie의 데이터는 유실되었습니다.
- Gia의 ID는 `ANIMAL_INS`에 있으므로, Gia의 데이터는 유실되지 않았습니다.
- Spice의 ID는 `ANIMAL_INS`에 없으므로, Spice의 데이터는 유실되었습니다.

---

### #08-4. 입출력 예시 (4)

따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME |
| --- | --- |
| A349733 | Allie |
| A349990 | Spice |

---
class: tight
---

## #09. 문제 9 — 오랜 기간 보호한 동물(1)

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

`ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다. `ANIMAL_OUTS` 테이블의 `ANIMAL_ID`는 `ANIMAL_INS`의 `ANIMAL_ID`의 외래 키입니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 59044">

아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.

</Callout>

---

### #09-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">ANIMAL_INS</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
<div>

<div class="kicker">ANIMAL_OUTS</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_OUTCOME | VARCHAR(N) | FALSE |

</div>
</Grid>

---

### #09-2. 입출력 예시 (2)

예를 들어, `ANIMAL_INS` 테이블과 `ANIMAL_OUTS` 테이블이 다음과 같다면

`ANIMAL_INS`

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A354597 | Cat | 2014-05-02 12:16:00 | Normal | Ariel | Spayed Female |
| A373687 | Dog | 2014-03-20 12:31:00 | Normal | Rosie | Spayed Female |
| A412697 | Dog | 2016-01-03 16:25:00 | Normal | Jackie | Neutered Male |
| A413789 | Dog | 2016-04-19 13:28:00 | Normal | Benji | Spayed Female |
| A414198 | Dog | 2015-01-29 15:01:00 | Normal | Shelly | Spayed Female |
| A368930 | Dog | 2014-06-08 13:20:00 | Normal |  | Spayed Female |

---

### #09-3. 입출력 예시 (3)

`ANIMAL_OUTS`

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | NAME | SEX_UPON_OUTCOME |
| --- | --- | --- | --- | --- |
| A354597 | Cat | 2014-05-02 12:16:00 | Ariel | Spayed Female |
| A373687 | Dog | 2014-03-20 12:31:00 | Rosie | Spayed Female |
| A368930 | Dog | 2014-06-13 15:52:00 |  | Spayed Female |

SQL문을 실행하면 다음과 같이 나와야 합니다.

| NAME | DATETIME |
| --- | --- |
| Shelly | 2015-01-29 15:01:00 |
| Jackie | 2016-01-03 16:25:00 |
| Benji | 2016-04-19 13:28:00 |

※ 입양을 가지 못한 동물이 3마리 이상인 경우만 입력으로 주어집니다.

---
class: tight
---

## #10. 문제 10 — 오랜 기간 보호한 동물(2)

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

`ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다. `ANIMAL_OUTS` 테이블의 `ANIMAL_ID`는 `ANIMAL_INS`의 `ANIMAL_ID`의 외래 키입니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 59411">

입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.

</Callout>

---

### #10-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">ANIMAL_INS</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| INTAKE_CONDITION | VARCHAR(N) | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_INTAKE | VARCHAR(N) | FALSE |

</div>
<div>

<div class="kicker">ANIMAL_OUTS</div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_OUTCOME | VARCHAR(N) | FALSE |

</div>
</Grid>

---

### #10-2. 입출력 예시 (2)

예를 들어, `ANIMAL_INS` 테이블과 `ANIMAL_OUTS` 테이블이 다음과 같다면

`ANIMAL_INS`

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A354597 | Cat | 2014-05-02 12:16:00 | Normal | Ariel | Spayed Female |
| A362707 | Dog | 2016-01-27 12:27:00 | Sick | Girly Girl | Spayed Female |
| A370507 | Cat | 2014-10-27 14:43:00 | Normal | Emily | Spayed Female |
| A414513 | Dog | 2016-06-07 09:17:00 | Normal | Rocky | Neutered Male |

---

### #10-3. 입출력 예시 (3)

`ANIMAL_OUTS`

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | NAME | SEX_UPON_OUTCOME |
| --- | --- | --- | --- | --- |
| A354597 | Cat | 2014-06-03 12:30:00 | Ariel | Spayed Female |
| A362707 | Dog | 2017-01-10 10:44:00 | Girly Girl | Spayed Female |
| A370507 | Cat | 2015-08-15 09:24:00 | Emily | Spayed Female |

SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME |
| --- | --- |
| A362707 | Girly Girl |
| A370507 | Emily |

※ 입양을 간 동물이 2마리 이상인 경우만 입력으로 주어집니다.

---
class: tight
---

## #11. 문제 11 — 카테고리 별 도서 판매량 집계하기

다음은 어느 한 서점에서 판매중인 도서들의 도서 정보(`BOOK`), 판매 정보(`BOOK_SALES`) 테이블입니다.

`BOOK` 테이블은 각 도서의 정보를 담은 테이블로 아래와 같은 구조로 되어있습니다.

`BOOK_SALES` 테이블은 각 도서의 날짜 별 판매량 정보를 담은 테이블로 아래와 같은 구조로 되어있습니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 144855">

`2022년 1월`의 카테고리 별 도서 판매량을 합산하고, 카테고리(`CATEGORY`), 총 판매량(`TOTAL_SALES`) 리스트를 출력하는 SQL문을 작성해주세요.     결과는 카테고리명을 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #11-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">BOOK</div>

| Column name | Type | Nullable | Description |
| --- | --- | --- | --- |
| BOOK_ID | INTEGER | FALSE | 도서 ID |
| CATEGORY | VARCHAR(N) | FALSE | 카테고리 (경제, 인문, 소설, 생활, 기술) |
| AUTHOR_ID | INTEGER | FALSE | 저자 ID |
| PRICE | INTEGER | FALSE | 판매가 (원) |
| PUBLISHED_DATE | DATE | FALSE | 출판일 |

</div>
<div>

<div class="kicker">BOOK_SALES</div>

| Column name | Type | Nullable | Description |
| --- | --- | --- | --- |
| BOOK_ID | INTEGER | FALSE | 도서 ID |
| SALES_DATE | DATE | FALSE | 판매일 |
| SALES | INTEGER | FALSE | 판매량 |

</div>
</Grid>

---

### #11-2. 입출력 예시 (2)

예를 들어 `BOOK` 테이블과 `BOOK_SALES` 테이블이 다음과 같다면

| BOOK_ID | CATEGORY | AUTHOR_ID | PRICE | PUBLISHED_DATE |
| --- | --- | --- | --- | --- |
| 1 | 인문 | 1 | 10000 | 2020-01-01 |
| 2 | 경제 | 1 | 9000 | 2021-02-05 |
| 3 | 경제 | 2 | 9000 | 2021-03-11 |

---

### #11-3. 입출력 예시 (3)

| BOOK_ID | SALES_DATE | SALES |
| --- | --- | --- |
| 1 | 2022-01-01 | 2 |
| 2 | 2022-01-02 | 3 |
| 1 | 2022-01-05 | 1 |
| 2 | 2022-01-20 | 5 |
| 2 | 2022-01-21 | 6 |
| 3 | 2022-01-22 | 2 |
| 2 | 2022-02-11 | 3 |

2022년 1월의 도서 별 총 판매량은 도서 ID 가 1 인 도서가 총 3권, 도서 ID 가 2 인 도서가 총 14권 이고, 도서 ID 가 3 인 도서가 총 2권 입니다.

---

### #11-4. 입출력 예시 (4)

카테고리 별로 판매량을 집계한 결과는 다음과 같습니다.

| CATEGORY | TOTAL_SALES |
| --- | --- |
| 인문 | 3 |
| 경제 | 16 |

카테고리명을 오름차순으로 정렬하면 다음과 같이 나와야 합니다.

| CATEGORY | TOTAL_SALES |
| --- | --- |
| 경제 | 16 |
| 인문 | 3 |

---
class: tight
---

## #12. 문제 12 — 조건에 맞는 사용자와 총 거래금액 조회하기

다음은 중고 거래 게시판 정보를 담은 `USED_GOODS_BOARD` 테이블과 중고 거래 게시판 사용자 정보를 담은 `USED_GOODS_USER` 테이블입니다. `USED_GOODS_BOARD` 테이블은 다음과 같으며 `BOARD_ID`, `WRITER_ID`, `TITLE`, `CONTENTS`, `PRICE`, `CREATED_DATE`, `STATUS`, `VIEWS`는 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.

`USED_GOODS_USER` 테이블은 다음과 같으며 `USER_ID`, `NICKNAME`, `CITY`, `STREET_ADDRESS1`, `STREET_ADDRESS2`, `TLNO`는 각각 회원 ID, 닉네임, 시, 도로명 주소, 상세 주소, 전화번호를 를 의미합니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 164668">

`USED_GOODS_BOARD`와 `USED_GOODS_USER` 테이블에서 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성해주세요. 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #12-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">USED_GOODS_BOARD</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| BOARD_ID | VARCHAR(5) | FALSE |
| WRITER_ID | VARCHAR(50) | FALSE |
| TITLE | VARCHAR(100) | FALSE |
| CONTENTS | VARCHAR(1000) | FALSE |
| PRICE | NUMBER | FALSE |
| CREATED_DATE | DATE | FALSE |
| STATUS | VARCHAR(10) | FALSE |
| VIEWS | NUMBER | FALSE |

</div>
<div>

<div class="kicker">USED_GOODS_USER</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| USER_ID | VARCHAR(50) | FALSE |
| NICKNAME | VARCHAR(100) | FALSE |
| CITY | VARCHAR(100) | FALSE |
| STREET_ADDRESS1 | VARCHAR(100) | FALSE |
| STREET_ADDRESS2 | VARCHAR(100) | TRUE |
| TLNO | VARCHAR(20) | FALSE |

</div>
</Grid>

---

### #12-2. 입출력 예시 (2)

`USED_GOODS_BOARD` 테이블이 다음과 같고

| BOARD_ID | WRITER_ID | TITLE | CONTENTS | PRICE | CREATED_DATE | STATUS | VIEWS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B0001 | zkzkdh1 | 캠핑의자 | 가벼워요 깨끗한 상태입니다. 2개 | 25000 | 2022-11-29 | SALE | 34 |
| B0002 | miyeon89 | 벽걸이 에어컨 | 엘지 휘센 7평 | 100000 | 2022-11-29 | SALE | 55 |
| B0003 | dhfkzmf09 | 에어팟 맥스 | 에어팟 맥스 스카이 블루 색상 판매합니다. | 450000 | 2022-11-26 | DONE | 67 |
| B0004 | sangjune1 | 파파야나인 포르쉐 푸쉬카 | 예민하신분은 피해주세요 | 30000 | 2022-11-30 | DONE | 78 |
| B0005 | zkzkdh1 | 애플워치7 | 애플워치7 실버 스텐 45미리 판매합니다. | 700000 | 2022-11-30 | DONE | 99 |

---

### #12-3. 입출력 예시 (3)

`USED_GOODS_USER` 테이블이 다음과 같을 때

| USER_ID | NICKNAME | CITY | STREET_ADDRESS1 | STREET_ADDRESS2 | TLNO |
| --- | --- | --- | --- | --- | --- |
| cjfwls91 | 점심만금식 | 성남시 | 분당구 내정로 185 | 501호 | 01036344964 |
| zkzkdh1 | 후후후 | 성남시 | 분당구 내정로 35 | 가동 1202호 | 01032777543 |
| spdlqj12 | 크크큭 | 성남시 | 분당구 수내로 206 | 2019동 801호 | 01087234922 |
| xlqpfh2 | 잉여킹 | 성남시 | 분당구 수내로 1 | 001-004 | 01064534911 |
| dhfkzmf09 | 찐찐 | 성남시 | 분당구 수내로 13 | A동 1107호 | 01053422914 |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| USER_ID | NICKNAME | TOTAL_SALES |
| --- | --- | --- |
| zkzkdh1 | 후후후 | 700000 |

---

## #13. 문제 13 — 헤비 유저가 소유한 장소

<Grid cols="2" align="start">
<div>

`PLACES` 테이블은 공간 임대 서비스에 등록된 공간의 정보를 담은 테이블입니다. `PLACES` 테이블의 구조는 다음과 같으며 `ID`, `NAME`, `HOST_ID`는 각각 공간의 아이디, 이름, 공간을 소유한 유저의 아이디를 나타냅니다. `ID`는 기본키입니다.

</div>
<div>

| NAME | TYPE |
| --- | --- |
| ID | INT |
| NAME | VARCHAR |
| HOST_ID | INT |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 77487">

이 서비스에서는 공간을 둘 이상 등록한 사람을 "헤비 유저"라고 부릅니다. 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL문을 작성해주세요.

</Callout>

---

### #13-1. 입출력 예시 (1)

예를 들어, `PLACES` 테이블이 다음과 같다면

| ID | NAME | HOST_ID |
| --- | --- | --- |
| 4431977 | BOUTIQUE STAYS - Somerset Terrace, Pet Friendly | 760849 |
| 5194998 | BOUTIQUE STAYS - Elwood Beaches 3, Pet Friendly | 760849 |
| 16045624 | Urban Jungle in the Heart of Melbourne | 30900122 |
| 17810814 | Stylish Bayside Retreat with a Luscious Garden | 760849 |
| 22740286 | FREE PARKING - The Velvet Lux in Melbourne CBD | 30900122 |
| 22868779 | ★ Fresh Fitzroy Pad with City Views! ★ | 21058208 |

---

### #13-2. 입출력 예시 (2)

- 760849번 유저는 공간을 3개 등록했으므로 이 유저는 헤비유저입니다.
- 30900122번 유저는 공간을 2개 등록했으므로 이 유저는 헤비유저입니다.
- 21058208번 유저는 공간을 1개 등록했으므로 이 유저는 헤비유저가 아닙니다.

따라서 SQL 문을 실행하면 다음과 같이 나와야 합니다.

| ID | NAME | HOST_ID |
| --- | --- | --- |
| 4431977 | BOUTIQUE STAYS - Somerset Terrace, Pet Friendly | 760849 |
| 5194998 | BOUTIQUE STAYS - Elwood Beaches 3, Pet Friendly | 760849 |
| 16045624 | Urban Jungle in the Heart of Melbourne | 30900122 |
| 17810814 | Stylish Bayside Retreat with a Luscious Garden | 760849 |
| 22740286 | FREE PARKING - The Velvet Lux in Melbourne CBD | 30900122 |

---
class: tight
---

## #14. 문제 14 — 조건에 맞는 사용자 정보 조회하기

다음은 중고 거래 게시판 정보를 담은 `USED_GOODS_BOARD` 테이블과 중고 거래 게시판 첨부파일 정보를 담은 `USED_GOODS_USER` 테이블입니다. `USED_GOODS_BOARD` 테이블은 다음과 같으며 `BOARD_ID`, `WRITER_ID`, `TITLE`, `CONTENTS`, `PRICE`, `CREATED_DATE`, `STATUS`, `VIEWS`는 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.

`USED_GOODS_USER` 테이블은 다음과 같으며 `USER_ID`, `NICKNAME`, `CITY`, `STREET_ADDRESS1`, `STREET_ADDRESS2`, `TLNO`는 각각 회원 ID, 닉네임, 시, 도로명 주소, 상세 주소, 전화번호를 의미합니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 164670">

`USED_GOODS_BOARD`와 `USED_GOODS_USER` 테이블에서 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문을 작성해주세요. 이때, 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고, 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(`-`)을 삽입하여 출력해주세요. 결과는 회원 ID를 기준으로 내림차순 정렬해주세요.

</Callout>

---

### #14-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">USED_GOODS_BOARD</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| BOARD_ID | VARCHAR(5) | FALSE |
| WRITER_ID | VARCHAR(50) | FALSE |
| TITLE | VARCHAR(100) | FALSE |
| CONTENTS | VARCHAR(1000) | FALSE |
| PRICE | NUMBER | FALSE |
| CREATED_DATE | DATE | FALSE |
| STATUS | VARCHAR(10) | FALSE |
| VIEWS | NUMBER | FALSE |

</div>
<div>

<div class="kicker">USED_GOODS_USER</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| USER_ID | VARCHAR(50) | FALSE |
| NICKANME | VARCHAR(100) | FALSE |
| CITY | VARCHAR(100) | FALSE |
| STREET_ADDRESS1 | VARCHAR(100) | FALSE |
| STREET_ADDRESS2 | VARCHAR(100) | TRUE |
| TLNO | VARCHAR(20) | FALSE |

</div>
</Grid>

---

### #14-2. 입출력 예시 (2)

`USED_GOODS_BOARD` 테이블이 다음과 같고

| BOARD_ID | WRITER_ID | TITLE | CONTENTS | PRICE | CREATED_DATE | STATUS | VIEWS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B0001 | dhfkzmf09 | 칼라거펠트 코트 | 양모 70%이상 코트입니다. | 120000 | 2022-10-14 | DONE | 104 |
| B0002 | lee871201 | 국내산 볶음참깨 | 직접 농사지은 참깨입니다. | 3000 | 2022-10-02 | DONE | 121 |
| B0003 | dhfkzmf09 | 나이키 숏패팅 | 사이즈는 M입니다. | 40000 | 2022-10-17 | DONE | 98 |
| B0004 | kwag98 | 반려견 배변패드 팝니다 | 정말 저렴히 판매합니다. 전부 미개봉 새상품입니다. | 12000 | 2022-10-01 | DONE | 250 |
| B0005 | dhfkzmf09 | PS4 | PS5 구매로인해 팝니다. | 250000 | 2022-11-03 | DONE | 111 |

---

### #14-3. 입출력 예시 (3)

`USED_GOODS_USER` 테이블이 다음과 같을 때

| USER_ID | NICKNAME | CITY | STREET_ADDRESS1 | STREET_ADDRESS2 | TLNO |
| --- | --- | --- | --- | --- | --- |
| dhfkzmf09 | 찐찐 | 성남시 | 분당구 수내로 13 | A동 1107호 | 01053422914 |
| dlPcks90 | 썹썹 | 성남시 | 분당구 수내로 74 | 401호 | 01034573944 |
| cjfwls91 | 점심만금식 | 성남시 | 분당구 내정로 185 | 501호 | 01036344964 |
| dlfghks94 | 희망 | 성남시 | 분당구 내정로 101 | 203동 102호 | 01032634154 |
| rkdhs95 | 용기 | 성남시 | 분당구 수내로 23 | 501호 | 01074564564 |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| USER_ID | NICKNAME | 전체주소 | 전화번호 |
| --- | --- | --- | --- |
| dhfkzmf09 | 찐찐 | 성남시 분당구 수내로 13 A동 1107호 | 010-5342-2914 |

---
class: tight
---

## #15. 문제 15 — 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기

다음은 중고거래 게시판 정보를 담은 `USED_GOODS_BOARD` 테이블과 중고거래 게시판 첨부파일 정보를 담은 `USED_GOODS_FILE` 테이블입니다. `USED_GOODS_BOARD` 테이블은 다음과 같으며 `BOARD_ID`, `WRITER_ID`, `TITLE`, `CONTENTS`, `PRICE`, `CREATED_DATE`, `STATUS`, `VIEWS`은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.

`USED_GOODS_FILE` 테이블은 다음과 같으며 `FILE_ID`, `FILE_EXT`, `FILE_NAME`, `BOARD_ID`는 각각 파일 ID, 파일 확장자, 파일 이름, 게시글 ID를 의미합니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 164671">

`USED_GOODS_BOARD`와 `USED_GOODS_FILE` 테이블에서 조회수가 가장 높은 중고거래 게시물에 대한 첨부파일 경로를 조회하는 SQL문을 작성해주세요. 첨부파일 경로는 FILE ID를 기준으로 내림차순 정렬해주세요. 기본적인 파일경로는 /home/grep/src/ 이며, 게시글 ID를 기준으로 디렉토리가 구분되고, 파일이름은 파일 ID, 파일 이름, 파일 확장자로 구성되도록 출력해주세요. 조회수가 가장 높은 게시물은 하나만 존재합니다.

</Callout>

---

### #15-1. 테이블 구조

<Grid cols="2" align="start">
<div>

<div class="kicker">USED_GOODS_BOARD</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| BOARD_ID | VARCHAR(5) | FALSE |
| WRITER_ID | VARCHAR(50) | FALSE |
| TITLE | VARCHAR(100) | FALSE |
| CONTENTS | VARCHAR(1000) | FALSE |
| PRICE | NUMBER | FALSE |
| CREATED_DATE | DATE | FALSE |
| STATUS | VARCHAR(10) | FALSE |
| VIEWS | NUMBER | FALSE |

</div>
<div>

<div class="kicker">USED_GOODS_FILE</div>

| Column name | Type | Nullable |
| --- | --- | --- |
| FILE_ID | VARCHAR(10) | FALSE |
| FILE_EXT | VARCHAR(5) | FALSE |
| FILE_NAME | VARCHAR(256) | FALSE |
| BOARD_ID | VARCHAR(10) | FALSE |

</div>
</Grid>

---

### #15-2. 입출력 예시 (2)

`USED_GOODS_BOARD` 테이블이 다음과 같고

| BOARD_ID | WRITER_ID | TITLE | CONTENTS | PRICE | CREATED_DATE | STATUS | VIEWS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B0001 | kwag98 | 반려견 배변패드 팝니다 | 정말 저렴히 판매합니다. 전부 미개봉 새상품입니다. | 12000 | 2022-10-01 | DONE | 250 |
| B0002 | lee871201 | 국내산 볶음참깨 | 직접 농사지은 참깨입니다. | 3000 | 2022-10-02 | DONE | 121 |
| B0003 | goung12 | 배드민턴 라켓 | 사놓고 방치만 해서 팝니다. | 9000 | 2022-10-02 | SALE | 212 |
| B0004 | keel1990 | 디올 귀걸이 | 신세계강남점에서 구입. 정품 아닐시 백퍼센트 환불 | 130000 | 2022-10-02 | SALE | 199 |
| B0005 | haphli01 | 스팸클래식 팔아요 | 유통기한 2025년까지에요 | 10000 | 2022-10-02 | SALE | 121 |

---

### #15-3. 입출력 예시 (3)

`USED_GOODS_FILE` 테이블이 다음과 같을 때

| FILE_ID | FILE_EXT | FILE_NAME | BOARD_ID |
| --- | --- | --- | --- |
| IMG_000001 | .jpg | photo1 | B0001 |
| IMG_000002 | .jpg | photo2 | B0001 |
| IMG_000003 | .png | 사진 | B0002 |
| IMG_000004 | .jpg | 사진 | B0003 |
| IMG_000005 | .jpg | photo | B0004 |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| FILE_PATH |
| --- |
| /home/grep/src/B0001/IMG_000001photo1.jpg |
| /home/grep/src/B0001/IMG_000002photo2.jpg |

---

## #16. 문제 16 — 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기

<Grid cols="2" align="start">
<div>

다음은 어느 자동차 대여 회사의 자동차 대여 기록 정보를 담은 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블입니다. `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블은 아래와 같은 구조로 되어있으며, `HISTORY_ID`, `CAR_ID`, `START_DATE`, `END_DATE` 는 각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일을 나타냅니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| HISTORY_ID | INTEGER | FALSE |
| CAR_ID | INTEGER | FALSE |
| START_DATE | DATE | FALSE |
| END_DATE | DATE | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 151139">

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수(컬럼명: `RECORDS`) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 월을 기준으로 오름차순 정렬하고, 월이 같다면 자동차 ID를 기준으로 내림차순 정렬해주세요. 특정 월의 총 대여 횟수가 0인 경우에는 결과에서 제외해주세요.

</Callout>

---

### #16-1. 입출력 예시 (1)

예를 들어 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블이 다음과 같다면

<Grid cols="2" align="start">
<div>

| HISTORY_ID | CAR_ID | START_DATE | END_DATE |
| --- | --- | --- | --- |
| 1 | 1 | 2022-07-27 | 2022-08-02 |
| 2 | 1 | 2022-08-03 | 2022-08-04 |
| 3 | 2 | 2022-08-05 | 2022-08-05 |
| 4 | 2 | 2022-08-09 | 2022-08-12 |
| 5 | 3 | 2022-09-16 | 2022-10-15 |
| 6 | 1 | 2022-08-24 | 2022-08-30 |
| 7 | 3 | 2022-10-16 | 2022-10-19 |
| 8 | 1 | 2022-09-03 | 2022-09-07 |

</div>
<div>

| HISTORY_ID | CAR_ID | START_DATE | END_DATE |
| --- | --- | --- | --- |
| 9 | 1 | 2022-09-18 | 2022-09-19 |
| 10 | 2 | 2022-09-08 | 2022-09-10 |
| 11 | 2 | 2022-10-16 | 2022-10-19 |
| 12 | 1 | 2022-09-29 | 2022-10-06 |
| 13 | 2 | 2022-10-30 | 2022-11-01 |
| 14 | 2 | 2022-11-05 | 2022-11-05 |
| 15 | 3 | 2022-11-11 | 2022-11-11 |

</div>
</Grid>

---

### #16-2. 입출력 예시 (2)

대여 시작일을 기준으로 총 대여 횟수가 5회 이상인 자동차는 자동차 ID가 1, 2인 자동차입니다. 월 별 자동차 ID별 총 대여 횟수를 구하고 월 오름차순, 자동차 ID 내림차순으로 정렬하면 다음과 같이 나와야 합니다.

| MONTH | CAR_ID | RECORDS |
| --- | --- | --- |
| 8 | 2 | 2 |
| 8 | 1 | 2 |
| 9 | 2 | 1 |
| 9 | 1 | 3 |
| 10 | 2 | 2 |

---
class: tight
---

## #17. 문제 17 — 즐겨찾기가 가장 많은 식당 정보 출력하기

<Grid cols="2" align="start">
<div>

다음은 식당의 정보를 담은 `REST_INFO` 테이블입니다. `REST_INFO` 테이블은 다음과 같으며 `REST_ID`, `REST_NAME`, `FOOD_TYPE`, `VIEWS`, `FAVORITES`, `PARKING_LOT`, `ADDRESS`, `TEL`은 식당 ID, 식당 이름, 음식 종류, 조회수, 즐겨찾기수, 주차장 유무, 주소, 전화번호를 의미합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| REST_ID | VARCHAR(5) | FALSE |
| REST_NAME | VARCHAR(50) | FALSE |
| FOOD_TYPE | VARCHAR(20) | TRUE |
| VIEWS | NUMBER | TRUE |
| FAVORITES | NUMBER | TRUE |
| PARKING_LOT | VARCHAR(1) | TRUE |
| ADDRESS | VARCHAR(100) | TRUE |
| TEL | VARCHAR(100) | TRUE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 131123">

`REST_INFO` 테이블에서 음식종류별로 즐겨찾기수가 가장 많은 식당의 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회하는 SQL문을 작성해주세요. 이때 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.

</Callout>

---

### #17-1. 입출력 예시 (1)

`REST_INFO` 테이블이 다음과 같을 때

| REST_ID | REST_NAME | FOOD_TYPE | VIEWS | FAVORITES | PARKING_LOT | ADDRESS | TEL |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00001 | 은돼지식당 | 한식 | 1150345 | 734 | N | 서울특별시 중구 다산로 149 | 010-4484-8751 |
| 00002 | 하이가쯔네 | 일식 | 120034 | 112 | N | 서울시 중구 신당동 375-21 | NULL |
| 00003 | 따띠따띠뜨 | 양식 | 1234023 | 102 | N | 서울시 강남구 신사동 627-3 1F | 02-6397-1023 |
| 00004 | 스시사카우스 | 일식 | 1522074 | 230 | N | 서울시 서울시 강남구 신사동 627-27 | 010-9394-2554 |
| 00005 | 코슌스 | 일식 | 15301 | 123 | N | 서울특별시 강남구 언주로153길 | 010-1315-8729 |

---

### #17-2. 입출력 예시 (2)

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| FOOD_TYPE | REST_ID | REST_NAME | FAVORITES |
| --- | --- | --- | --- |
| 한식 | 00001 | 은돼지식당 | 734 |
| 일식 | 00004 | 스시사카우스 | 230 |
| 양식 | 00003 | 따띠따띠뜨 | 102 |


---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-06] 고급 데이터 조회 6 · ITWILL · {teacher} 강사</p>

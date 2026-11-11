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

<p class="sub">[LAB-04] 그룹조회 (3) / ITWILL - 주영아·이광호 강사</p>

---
layout: section
---

# SQL 코딩 테스트

앞서 배운 상황별 템플릿으로 프롬프트를 직접 작성하여 문제를 풀어보세요

---

## #01. 문제 1 — 고양이와 개는 몇 마리 있을까

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59040">

동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.

</Callout>

---

### #01-1. 입출력 예시

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A373219 | Cat | 2014-07-29 11:43:00 | Normal | Ella | Spayed Female |
| A377750 | Dog | 2017-10-25 17:17:00 | Normal | Lucy | Spayed Female |
| A354540 | Cat | 2014-12-11 11:48:00 | Normal | Tux | Neutered Male |

고양이는 2마리, 개는 1마리 들어왔습니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_TYPE | count |
| --- | --- |
| Cat | 2 |
| Dog | 1 |

---

## #02. 문제 2 — 중복 제거하기

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59408">

동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

</Callout>

---

### #02-1. 입출력 예시

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A562649 | Dog | 2014-03-20 18:06:00 | Sick | NULL | Spayed Female |
| A412626 | Dog | 2016-03-13 11:17:00 | Normal | *Sam | Neutered Male |
| A563492 | Dog | 2014-10-24 14:45:00 | Normal | *Sam | Neutered Male |
| A513956 | Dog | 2017-06-14 11:54:00 | Normal | *Sweetie | Spayed Female |

보호소에 들어온 동물의 이름은 NULL(없음), `*Sam`, `*Sam`, `*Sweetie`입니다. 이 중 NULL과 중복되는 이름을 고려하면, 보호소에 들어온 동물 이름의 수는 2입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| count |
| --- |
| 2 |

※ 컬럼 이름(위 예제에서는 count)은 일치하지 않아도 됩니다.

---

## #03. 문제 3 — 카테고리 별 상품 개수 구하기

<Grid cols="2" align="start">
<div>

다음은 어느 의류 쇼핑몰에서 판매중인 상품들의 정보를 담은 `PRODUCT` 테이블입니다. `PRODUCT` 테이블은 아래와 같은 구조로 되어있으며, `PRODUCT_ID`, `PRODUCT_CODE`, `PRICE`는 각각 상품 ID, 상품코드, 판매가를 나타냅니다.

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 131529">

`PRODUCT` 테이블에서 상품 카테고리 코드(`PRODUCT_CODE` 앞 2자리) 별 상품 개수를 출력하는 SQL문을 작성해주세요. 결과는 상품 카테고리 코드를 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #03-1. 입출력 예시 (1)

예를 들어 `PRODUCT` 테이블이 다음과 같다면

| PRODUCT_ID | PRODUCT_CODE | PRICE |
| --- | --- | --- |
| 1 | A1000011 | 10000 |
| 2 | A1000045 | 9000 |
| 3 | C3000002 | 22000 |
| 4 | C3000006 | 15000 |
| 5 | C3000010 | 30000 |
| 6 | K1000023 | 17000 |

상품 카테고리 코드 별 상품은 아래와 같으므로,

---

### #03-2. 입출력 예시 (2)

- `A1`: `PRODUCT_ID`가 1, 2 인 상품
- `C3`: `PRODUCT_ID`가 3, 4, 5 인 상품
- `K1`: `PRODUCT_ID`가 6 인 상품

다음과 같은 결과가 나와야 합니다.

| CATEGORY | PRODUCTS |
| --- | --- |
| A1 | 2 |
| C3 | 3 |
| K1 | 1 |

---
class: tight
---

## #04. 문제 4 — 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기

<Grid cols="2" align="start">
<div>

다음은 어느 자동차 대여 회사에서 대여중인 자동차들의 정보를 담은 `CAR_RENTAL_COMPANY_CAR` 테이블입니다. `CAR_RENTAL_COMPANY_CAR` 테이블은 아래와 같은 구조로 되어있으며, `CAR_ID`, `CAR_TYPE`, `DAILY_FEE`, `OPTIONS` 는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트를 나타냅니다.

자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 이 있습니다. 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트(옵션 리스트 값 예시: '열선시트', '스마트키', '주차감지센서')로 되어있으며, 키워드 종류는 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 가 있습니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| CAR_ID | INTEGER | FALSE |
| CAR_TYPE | VARCHAR(255) | FALSE |
| DAILY_FEE | INTEGER | FALSE |
| OPTIONS | VARCHAR(255) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 151137">

`CAR_RENTAL_COMPANY_CAR` 테이블에서 '통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차가 자동차 종류 별로 몇 대인지 출력하는 SQL문을 작성해주세요. 이때 자동차 수에 대한 컬럼명은 `CARS`로 지정하고, 결과는 자동차 종류를 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #04-1. 입출력 예시 (1)

예를 들어 `CAR_RENTAL_COMPANY_CAR` 테이블이 다음과 같다면

| CAR_ID | CAR_TYPE | DAILY_FEE | OPTIONS |
| --- | --- | --- | --- |
| 1 | 세단 | 16000 | 가죽시트,열선시트,후방카메라 |
| 2 | SUV | 14000 | 스마트키,네비게이션,열선시트 |
| 3 | SUV | 22000 | 주차감지센서,후방카메라 |
| 4 | 트럭 | 35000 | 주차감지센서,네비게이션,열선시트 |
| 5 | SUV | 16000 | 가죽시트,네비게이션,열선시트,후방카메라,주차감지센서 |

---

### #04-2. 입출력 예시 (2)

'통풍시트', '열선시트', '가죽시트' 중 하나 이상의 옵션이 포함된 자동차는 자동차 ID가 1, 2, 4, 5인 자동차이고, 자동차 종류 별로 몇 대인지 구하고 자동차 종류를 기준으로 오름차순 정렬하면 다음과 같은 결과가 나와야 합니다.

| CAR_TYPE | CARS |
| --- | --- |
| SUV | 2 |
| 세단 | 1 |
| 트럭 | 1 |

---
class: tight
---

## #05. 문제 5 — 진료과별 총 예약 횟수 출력하기

<Grid cols="2" align="start">
<div>

다음은 종합병원의 진료 예약정보를 담은 `APPOINTMENT` 테이블 입니다.  
 `APPOINTMENT` 테이블은 다음과 같으며 `APNT_YMD`, `APNT_NO`, `PT_NO`, `MCDP_CD`, `MDDR_ID`, `APNT_CNCL_YN`, `APNT_CNCL_YMD`는 각각 진료예약일시, 진료예약번호, 환자번호, 진료과코드, 의사ID, 예약취소여부, 예약취소날짜를 나타냅니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| APNT_YMD | TIMESTAMP | FALSE |
| APNT_NO | NUMBER(5) | FALSE |
| PT_NO | VARCHAR(10) | FALSE |
| MCDP_CD | VARCHAR(6) | FALSE |
| MDDR_ID | VARCHAR(10) | FALSE |
| APNT_CNCL_YN | VARCHAR(1) | TRUE |
| APNT_CNCL_YMD | DATE | TRUE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 132202">

`APPOINTMENT` 테이블에서 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회하는 SQL문을 작성해주세요. 이때, 컬럼명은 '진료과 코드', '5월예약건수'로 지정해주시고 결과는 진료과별 예약한 환자 수를 기준으로 오름차순 정렬하고, 예약한 환자 수가 같다면 진료과 코드를 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #05-1. 입출력 예시 (1)

`APPOINTMENT` 테이블이 다음과 같을 때

| APNT_YMD | APNT_NO | PT_NO | MCDP_CD | MDDR_ID | APNT_CNCL_YN | APNT_CNCL_YMD |
| --- | --- | --- | --- | --- | --- | --- |
| 2022-04-14 09:30:00.000000 | 47 | PT22000064 | GS | DR20170123 | N | NULL |
| 2022-04-15 10:30:00.000000 | 48 | PT22000065 | OB | DR20100231 | N | NULL |
| 2022-05-15 17:30:00.000000 | 49 | PT22000086 | OB | DR20100231 | N | NULL |
| 2022-05-18 10:30:00.000000 | 52 | PT22000019 | GS | DR20100039 | N | NULL |
| 2022-05-19 12:00:00.000000 | 53 | PT22000020 | FM | DR20010112 | N | NULL |

---

### #05-2. 입출력 예시 (2)

| APNT_YMD | APNT_NO | PT_NO | MCDP_CD | MDDR_ID | APNT_CNCL_YN | APNT_CNCL_YMD |
| --- | --- | --- | --- | --- | --- | --- |
| 2022-05-22 08:30:00.000000 | 54 | PT22000021 | GS | DR20100039 | N | NULL |
| 2022-05-04 10:30:00.000000 | 56 | PT22000023 | FM | DR20090112 | N | NULL |
| 2022-05-14 15:30:00.000000 | 57 | PT22000074 | CS | DR20200012 | N | NULL |
| 2022-05-24 15:30:00.000000 | 58 | PT22000085 | CS | DR20200012 | N | NULL |
| 2022-05-28 10:00:00.000000 | 60 | PT22000092 | OS | DR20100031 | N | NULL |

---

### #05-3. 입출력 예시 (3)

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| 진료과코드 | 5월예약건수 |
| --- | --- |
| OB | 1 |
| OS | 1 |
| CS | 2 |
| FM | 2 |
| GS | 2 |

---

## #06. 문제 6 — 연도 별 평균 미세먼지 농도 조회하기

<Grid cols="2" align="start">
<div>

`AIR_POLLUTION` 테이블은 전국의 월별 미세먼지 정보를 담은 테이블입니다. `AIR_POLLUTION` 테이블의 구조는 다음과 같으며 `LOCATION1`, `LOCATION2`, `YM`, `PM_VAL1`, `PM_VAL2`은 각각 지역구분1, 지역구분2, 측정일, 미세먼지 오염도, 초미세먼지 오염도를 의미합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| LOCATION1 | VARCHAR | FALSE |
| LOCATION2 | VARCHAR | FALSE |
| YM | DATE | FALSE |
| PM_VAL1 | NUMBER | FLASE |
| PM_VAL2 | NUMBER | FLASE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 284530">

`AIR_POLLUTION` 테이블에서 수원 지역의 연도 별 평균 미세먼지 오염도와 평균 초미세먼지 오염도를 조회하는 SQL문을 작성해주세요. 이때, 평균 미세먼지 오염도와 평균 초미세먼지 오염도의 컬럼명은 각각 `PM10`, `PM2.5`로 해 주시고, 값은 소수 셋째 자리에서 반올림해주세요.    결과는 연도를 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #06-1. 입출력 예시 (1)

`AIR_POLLUTION` 테이블이 다음과 같을 때

| LOCATION1 | LOCATION2 | YM | PM_VAL1 | PM_VAL2 |
| --- | --- | --- | --- | --- |
| 경기도 | 수원 | 2018-01-01 | 48 | 27 |
| 경기도 | 수원 | 2018-02-01 | 51 | 30 |
| 경기도 | 수원 | 2018-03-01 | 52 | 21 |
| 경기도 | 수원 | 2018-04-01 | 52 | 20 |
| 경기도 | 수원 | 2018-05-01 | 45 | 19 |
| 경기도 | 수원 | 2018-06-01 | 39 | 17 |
| 경기도 | 수원 | 2018-07-01 | 27 | 15 |

---

### #06-2. 입출력 예시 (2)

| LOCATION1 | LOCATION2 | YM | PM_VAL1 | PM_VAL2 |
| --- | --- | --- | --- | --- |
| 경기도 | 수원 | 2018-08-01 | 26 | 16 |
| 경기도 | 수원 | 2018-09-01 | 21 | 12 |
| 경기도 | 수원 | 2018-10-01 | 31 | 18 |
| 경기도 | 수원 | 2018-11-01 | 56 | 21 |
| 경기도 | 수원 | 2018-12-01 | 44 | 27 |
| 서울시 | 노원 | 2018-11-01 | 25 | 45 |
| 경기도 | 용인 | 2018-02-01 | 14 | 21 |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| YEAR | PM10 | PM2.5 |
| --- | --- | --- |
| 2018 | 41 | 20.25 |

※ 공지 - 2023년 3월 4일 문제 오탈자가 수정되었습니다.

---

## #07. 문제 7 — 가격대 별 상품 개수 구하기

<Grid cols="2" align="start">
<div>

다음은 어느 의류 쇼핑몰에서 판매중인 상품들의 정보를 담은 `PRODUCT` 테이블입니다. `PRODUCT` 테이블은 아래와 같은 구조로 되어있으며, `PRODUCT_ID`, `PRODUCT_CODE`, `PRICE`는 각각 상품 ID, 상품코드, 판매가를 나타냅니다.

상품 별로 중복되지 않는 8자리 상품코드 값을 가지며 앞 2자리는 카테고리 코드를 나타냅니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| PRODUCT_ID | INTEGER | FALSE |
| PRODUCT_CODE | VARCHAR(8) | FALSE |
| PRICE | INTEGER | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 131530">

`PRODUCT` 테이블에서 만원 단위의 가격대 별로 상품 개수를 출력하는 SQL 문을 작성해주세요. 이때 컬럼명은 각각 컬럼명은 PRICE_GROUP, PRODUCTS로 지정해주시고 가격대 정보는 각 구간의 최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000)으로 표시해주세요. 결과는 가격대를 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #07-1. 입출력 예시 (1)

예를 들어 `PRODUCT` 테이블이 다음과 같다면

| PRODUCT_ID | PRODUCT_CODE | PRICE |
| --- | --- | --- |
| 1 | A1000011 | 10000 |
| 2 | A1000045 | 9000 |
| 3 | C3000002 | 22000 |
| 4 | C3000006 | 15000 |
| 5 | C3000010 | 30000 |
| 6 | K1000023 | 17000 |

만원 단위의 가격대 별로 상품을 나누면

---

### #07-2. 입출력 예시 (2)

- 가격대가 0원 ~ 1만원 미만인 상품은 `PRODUCT_ID` 가 2인 상품 1개,
- 가격대가 1만원 이상 ~ 2만원 미만인 상품들은 `PRODUCT_ID` 가 1, 4, 6인 상품 3개,
- 가격대가 2만원 이상 ~ 3만원 미만인 상품은 `PRODUCT_ID` 가 3인 상품 1개,
- 가격대가 3만원 이상 ~ 4만원 미만인 상품은 `PRODUCT_ID` 가 5인 상품 1개,

에 각각 해당하므로 다음과 같이 결과가 나와야 합니다.

| PRICE_GROUP | PRODUCTS |
| --- | --- |
| 0 | 1 |
| 10000 | 3 |
| 20000 | 1 |
| 30000 | 1 |

---
class: tight
---

## #08. 문제 8 — 노선별 평균 역 사이 거리 조회하기

<Grid cols="2" align="start">
<div>

`SUBWAY_DISTANCE` 테이블은 서울지하철 2호선의 역 간 거리 정보를 담은 테이블입니다. `SUBWAY_DISTANCE` 테이블의 구조는 다음과 같으며 `LINE`, `NO`, `ROUTE`, `STATION_NAME`, `D_BETWEEN_DIST`, `D_CUMULATIVE`는 각각 호선, 순번, 노선, 역 이름, 역 사이 거리, 노선별 누계 거리를 의미합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| LINE | VARCHAR(10) | FALSE |
| NO | NUMBER | FALSE |
| ROUTE | VARCHAR(50) | FALSE |
| STATION_NAME | VARCHAR(100) | FLASE |
| D_BETWEEN_DIST | NUMBER | FLASE |
| D_CUMULATIVE | NUMBER | FLASE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 284531">

`SUBWAY_DISTANCE` 테이블에서 노선별로 노선, 총 누계 거리, 평균 역 사이 거리를 노선별로 조회하는 SQL문을 작성해주세요. 총 누계거리는 테이블 내 존재하는 역들의 `역 사이 거리`의 총 합을 뜻합니다. 총 누계 거리와 평균 역 사이 거리의 컬럼명은 각각 `TOTAL_DISTANCE`, `AVERAGE_DISTANCE`로 해주시고, 총 누계거리는 소수 둘째자리에서, 평균 역 사이 거리는 소수 셋째 자리에서 반올림 한 뒤 단위(km)를 함께 출력해주세요.    결과는 총 누계 거리를 기준으로 내림차순 정렬해주세요.

</Callout>

---

### #08-1. 입출력 예시 (1)

`SUBWAY_DISTANCE` 테이블이 다음과 같을 때

| LINE | NO | ROUTE | STATION_NAME | D_BETWEEN_DIST | D_CUMULATIVE |
| --- | --- | --- | --- | --- | --- |
| 2호선 | 45 | 성수지선 | 용답 | 2.3 | 51.1 |
| 2호선 | 46 | 성수지선 | 신답 | 1 | 52.1 |
| 2호선 | 47 | 성수지선 | 용두(동대문구청) | 0.9 | 53 |
| 2호선 | 48 | 성수지선 | 신설동 | 1.2 | 54.2 |
| 2호선 | 49 | 신정지선 | 도림천 | 1 | 55.2 |
| 2호선 | 50 | 신정지선 | 양천구청 | 1.7 | 56.9 |
| 2호선 | 51 | 신정지선 | 신정네거리 | 1.9 | 58.8 |
| 2호선 | 52 | 신정지선 | 까치산 | 1.4 | 60.2 |

---

### #08-2. 입출력 예시 (2)

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| ROUTE | TOTAL_DISTANCE | AVERAGE_DISTANCE |
| --- | --- | --- |
| 신정지선 | 6km | 1.5km |
| 성수지선 | 5.4km | 1.35km |

---

## #09. 문제 9 — 입양 시각 구하기(1)

<Grid cols="2" align="start">
<div>

`ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.

</div>
<div>

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| ANIMAL_ID | VARCHAR(N) | FALSE |
| ANIMAL_TYPE | VARCHAR(N) | FALSE |
| DATETIME | DATETIME | FALSE |
| NAME | VARCHAR(N) | TRUE |
| SEX_UPON_OUTCOME | VARCHAR(N) | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59412">

보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

</Callout>

---

### #09-1. 입출력 예시

SQL문을 실행하면 다음과 같이 나와야 합니다.

<Grid cols="2" align="start">
<div>

| HOUR | COUNT |
| --- | --- |
| 9 | 1 |
| 10 | 2 |
| 11 | 13 |
| 12 | 10 |
| 13 | 14 |
| 14 | 9 |

</div>
<div>

| HOUR | COUNT |
| --- | --- |
| 15 | 7 |
| 16 | 10 |
| 17 | 12 |
| 18 | 16 |
| 19 | 2 |

</div>
</Grid>

---

## #10. 문제 10 — 동명 동물 수 찾기

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59041">

동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.

</Callout>

---

### #10-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A396810 | Dog | 2016-08-22 16:13:00 | Injured | Raven | Spayed Female |
| A377750 | Dog | 2017-10-25 17:17:00 | Normal | Lucy | Spayed Female |
| A355688 | Dog | 2014-01-26 13:48:00 | Normal | Shadow | Neutered Male |
| A399421 | Dog | 2015-08-25 14:08:00 | Normal | Lucy | Spayed Female |
| A400680 | Dog | 2017-06-17 13:29:00 | Normal | Lucy | Spayed Female |
| A410668 | Cat | 2015-11-19 13:41:00 | Normal | Raven | Spayed Female |

---

### #10-2. 입출력 예시 (2)

- Raven 이름은 2번 쓰였습니다.
- Lucy 이름은 3번 쓰였습니다
- Shadow 이름은 1번 쓰였습니다.

따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| NAME | COUNT |
| --- | --- |
| Lucy | 3 |
| Raven | 2 |

---

## #11. 문제 11 — 재구매가 일어난 상품과 회원 리스트 구하기

<Grid cols="2" align="start">
<div>

다음은 어느 의류 쇼핑몰의 온라인 상품 판매 정보를 담은 `ONLINE_SALE` 테이블 입니다. `ONLINE_SALE` 테이블은 아래와 같은 구조로 되어있으며 `ONLINE_SALE_ID`, `USER_ID`, `PRODUCT_ID`, `SALES_AMOUNT`, `SALES_DATE`는 각각 온라인 상품 판매 ID, 회원 ID, 상품 ID, 판매량, 판매일을 나타냅니다.

동일한 날짜, 회원 ID, 상품 ID 조합에 대해서는 하나의 판매 데이터만 존재합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| ONLINE_SALE_ID | INTEGER | FALSE |
| USER_ID | INTEGER | FALSE |
| PRODUCT_ID | INTEGER | FALSE |
| SALES_AMOUNT | INTEGER | FALSE |
| SALES_DATE | DATE | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 131536">

`ONLINE_SALE` 테이블에서 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여, 재구매한 회원 ID와 재구매한 상품 ID를 출력하는 SQL문을 작성해주세요. 결과는 회원 ID를 기준으로 오름차순 정렬해주시고 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬해주세요.

</Callout>

---

### #11-1. 입출력 예시 (1)

예를 들어 `ONLINE_SALE` 테이블이 다음과 같다면

| ONLINE_SALE_ID | USER_ID | PRODUCT_ID | SALES_AMOUNT | SALES_DATE |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | 2 | 2022-02-25 |
| 2 | 1 | 4 | 1 | 2022-03-01 |
| 4 | 2 | 4 | 2 | 2022-03-12 |
| 3 | 1 | 3 | 3 | 2022-03-31 |
| 5 | 3 | 5 | 1 | 2022-04-03 |
| 6 | 2 | 4 | 1 | 2022-04-06 |
| 2 | 1 | 4 | 2 | 2022-05-11 |

---

### #11-2. 입출력 예시 (2)

`USER_ID` 가 1인 유저가 `PRODUCT_ID` 가 3, 4인 상품들을 재구매하고, `USER_ID` 가 2인 유저가 `PRODUCT_ID` 가 4인 상품을 재구매 하였으므로, 다음과 같이 결과가 나와야합니다.

| USER_ID | PRODUCT_ID |
| --- | --- |
| 1 | 4 |
| 1 | 3 |
| 2 | 4 |

---

## #12. 문제 12 — 자동차 평균 대여 기간 구하기

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 157342">

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 평균 대여 기간이 7일 이상인 자동차들의 자동차 ID와 평균 대여 기간(컬럼명: `AVERAGE_DURATION`) 리스트를 출력하는 SQL문을 작성해주세요. 평균 대여 기간은 소수점 두번째 자리에서 반올림하고, 결과는 평균 대여 기간을 기준으로 내림차순 정렬해주시고, 평균 대여 기간이 같으면 자동차 ID를 기준으로 내림차순 정렬해주세요.

</Callout>

---

### #12-1. 입출력 예시 (1)

예를 들어 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블이 다음과 같다면

| HISTORY_ID | CAR_ID | START_DATE | END_DATE |
| --- | --- | --- | --- |
| 1 | 1 | 2022-09-27 | 2022-10-01 |
| 2 | 1 | 2022-10-03 | 2022-11-04 |
| 3 | 2 | 2022-09-05 | 2022-09-05 |
| 4 | 2 | 2022-09-08 | 2022-09-10 |
| 5 | 3 | 2022-09-16 | 2022-10-15 |
| 6 | 1 | 2022-11-07 | 2022-12-06 |

자동차 별 평균 대여 기간은

---

### #12-2. 입출력 예시 (2)

- 자동차 ID가 1인 자동차의 경우, 대여 기간이 각각 5일, 33일, 30일인 기록이 존재하므로 평균 22.7일
- 자동차 ID가 2인 자동차의 경우, 대여 기간이 각각 1일, 3일인 기록이 존재하므로 평균 2일
- 자동차 ID가 3인 자동차의 경우, 대여 기간이 30일인 기록만 존재하므로 평균 30일 입니다. 평균 대여 기간이 7일 이상인 자동차는 자동차 ID가 1, 3인 자동차이고, 평균 대여 기간 내림차순 및 자동차 ID를 기준으로 내림차순 정렬하면 다음과 같이 나와야 합니다.

| CAR_ID | AVERAGE_DURATION |
| --- | --- |
| 3 | 30.0 |
| 1 | 22.7 |

※ 공지 - 2024년 10월 2일 채점코드가 수정되었습니다. 기존에 제출한 코드가 통과하지 못할 수도 있습니다.

---

## #13. 문제 13 — 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 157340">

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고, 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼(컬럼명: `AVAILABILITY`)을 추가하여 자동차 ID와 `AVAILABILITY` 리스트를 출력하는 SQL문을 작성해주세요. 이때 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'으로 표시해주시고 결과는 자동차 ID를 기준으로 내림차순 정렬해주세요.

</Callout>

---

### #13-1. 입출력 예시 (1)

예를 들어 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블이 다음과 같다면

| HISTORY_ID | CAR_ID | START_DATE | END_DATE |
| --- | --- | --- | --- |
| 1 | 4 | 2022-09-27 | 2022-09-27 |
| 2 | 3 | 2022-10-03 | 2022-10-04 |
| 3 | 2 | 2022-10-05 | 2022-10-05 |
| 4 | 1 | 2022-10-11 | 2022-10-16 |
| 5 | 3 | 2022-10-13 | 2022-10-15 |
| 6 | 2 | 2022-10-15 | 2022-10-17 |

---

### #13-2. 입출력 예시 (2)

2022년 10월 16일에 대여 중인 자동차는 자동차 ID가 1, 2인 자동차이고, 대여 가능한 자동차는 자동차 ID가 3, 4이므로, '대여중' 또는 '대여 가능' 을 표시하는 컬럼을 추가하고, 자동차 ID를 기준으로 내림차순 정렬하면 다음과 같이 나와야 합니다.

| CAR_ID | AVAILABILITY |
| --- | --- |
| 4 | 대여 가능 |
| 3 | 대여 가능 |
| 2 | 대여중 |
| 1 | 대여중 |


---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-04] 그룹조회 3 · ITWILL · {teacher} 강사</p>

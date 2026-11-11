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

<p class="sub">[LAB-03] SQL 함수 (6) / ITWILL - 주영아·이광호 강사</p>

---
layout: section
---

# SQL 코딩 테스트

앞서 배운 상황별 템플릿으로 프롬프트를 직접 작성하여 문제를 풀어보세요

---

## #01. 문제 1 — 나이 정보가 없는 회원 수 구하기

<Grid cols="2" align="start">
<div>

다음은 어느 의류 쇼핑몰에 가입한 회원 정보를 담은 `USER_INFO` 테이블입니다. `USER_INFO` 테이블은 아래와 같은 구조로 되어있으며, `USER_ID`, `GENDER`, `AGE`, `JOINED`는 각각 회원 ID, 성별, 나이, 가입일을 나타냅니다.

`GENDER` 컬럼은 비어있거나 0 또는 1의 값을 가지며 0인 경우 남자를, 1인 경우는 여자를 나타냅니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| USER_ID | INTEGER | FALSE |
| GENDER | TINYINT(1) | TRUE |
| AGE | INTEGER | TRUE |
| JOINED | DATE | FALSE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 131528">

`USER_INFO` 테이블에서 나이 정보가 없는 회원이 몇 명인지 출력하는 SQL문을 작성해주세요. 이때 컬럼명은 USERS로 지정해주세요.

</Callout>

---

### #01-1. 입출력 예시

예를 들어 `USER_INFO` 테이블이 다음과 같다면

| USER_ID | GENDER | AGE | JOINED |
| --- | --- | --- | --- |
| 1 | 1 | 26 | 2021-06-01 |
| 2 | NULL | NULL | 2021-07-25 |
| 3 | 1 | NULL | 2021-07-30 |
| 4 | 0 | 31 | 2021-08-03 |

나이 정보가 없는 회원은 2명 이므로, 다음과 같은 결과가 나와야 합니다.

| USERS |
| --- |
| 2 |

---
class: tight
---

## #02. 문제 2 — 평균 일일 대여 요금 구하기

<Grid cols="2" align="start">
<div>

다음은 어느 자동차 대여 회사에서 대여중인 자동차들의 정보를 담은 `CAR_RENTAL_COMPANY_CAR` 테이블입니다. `CAR_RENTAL_COMPANY_CAR` 테이블은 아래와 같은 구조로 되어있으며, `CAR_ID`, `CAR_TYPE`, `DAILY_FEE`, `OPTIONS` 는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트를 나타냅니다.

자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 이 있습니다. 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트(예: '열선시트', '스마트키', '주차감지센서')로 되어있으며, 키워드 종류는 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 가 있습니다.

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 151136">

`CAR_RENTAL_COMPANY_CAR` 테이블에서 자동차 종류가 'SUV'인 자동차들의 평균 일일 대여 요금을 출력하는 SQL문을 작성해주세요. 이때 평균 일일 대여 요금은 소수 첫 번째 자리에서 반올림하고, 컬럼명은 `AVERAGE_FEE` 로 지정해주세요.

</Callout>

---

### #02-1. 입출력 예시

예를 들어 `CAR_RENTAL_COMPANY_CAR` 테이블이 다음과 같다면

| CAR_ID | CAR_TYPE | DAILY_FEE | OPTIONS |
| --- | --- | --- | --- |
| 1 | 세단 | 16000 | 가죽시트,열선시트,후방카메라 |
| 2 | SUV | 14000 | 스마트키,네비게이션,열선시트 |
| 3 | SUV | 22000 | 주차감지센서,후방카메라,가죽시트 |

'SUV' 에 해당하는 자동차들의 평균 일일 대여 요금은 18,000 원 이므로, 다음과 같은 결과가 나와야 합니다.

| AVERAGE_FEE |
| --- |
| 18000 |

---

## #03. 문제 3 — 경기도에 위치한 식품창고 목록 출력하기

<Grid cols="2" align="start">
<div>

다음은 식품창고의 정보를 담은 `FOOD_WAREHOUSE` 테이블입니다. `FOOD_WAREHOUSE` 테이블은 다음과 같으며 `WAREHOUSE_ID`, `WAREHOUSE_NAME`, `ADDRESS`, `TLNO`, `FREEZER_YN`는 창고 ID, 창고 이름, 창고 주소, 전화번호, 냉동시설 여부를 의미합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| WAREHOUSE_ID | VARCHAR(10) | FALSE |
| WAREHOUSE_NAME | VARCHAR(20) | FALSE |
| ADDRESS | VARCHAR(100) | TRUE |
| TLNO | VARCHAR(20) | TRUE |
| FREEZER_YN | VARCHAR(1) | TRUE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 131114">

`FOOD_WAREHOUSE` 테이블에서 경기도에 위치한 창고의 ID, 이름, 주소, 냉동시설 여부를 조회하는 SQL문을 작성해주세요. 이때 냉동시설 여부가 NULL인 경우, 'N'으로 출력시켜 주시고 결과는 창고 ID를 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #03-1. 입출력 예시

`FOOD_WAREHOUSE` 테이블이 다음과 같을 때

| WAREHOUSE_ID | WAREHOUSE_NAME | ADDRESS | TLNO | FREEZER_YN |
| --- | --- | --- | --- | --- |
| WH0001 | 창고_경기1 | 경기도 안산시 상록구 용담로 141 | 031-152-1332 | Y |
| WH0002 | 창고_충북1 | 충청북도 진천군 진천읍 씨제이로 110 | 043-623-9900 | Y |
| WH0003 | 창고_경기2 | 경기도 이천시 마장면 덕평로 811 | 031-221-7241 | NULL |
| WH0004 | 창고_경기3 | 경기도 김포시 대곶면 율생중앙로205번길 | 031-671-1900 | N |
| WH0005 | 창고_충남1 | 충청남도 천안시 동남구 광덕면 신덕리1길 9 | 041-876-5421 | Y |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| WAREHOUSE_ID | WAREHOUSE_NAME | ADDRESS | FREEZER_YN |
| --- | --- | --- | --- |
| WH0001 | 창고_경기1 | 경기도 안산시 상록구 용담로 141 | Y |
| WH0003 | 창고_경기2 | 경기도 이천시 마장면 덕평로 811 | N |
| WH0004 | 창고_경기3 | 경기도 김포시 대곶면 율생중앙로205번길 | N |

---

## #04. 문제 4 — 12세 이하인 여자 환자 목록 출력하기

<Grid cols="2" align="start">
<div>

다음은 종합병원에 등록된 환자정보를 담은 `PATIENT` 테이블입니다. `PATIENT` 테이블은 다음과 같으며 `PT_NO`, `PT_NAME`, `GEND_CD`, `AGE`, `TLNO`는 각각 환자번호, 환자이름, 성별코드, 나이, 전화번호를 의미합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| PT_NO | VARCHAR(10) | FALSE |
| PT_NAME | VARCHAR(20) | FALSE |
| GEND_CD | VARCHAR(1) | FALSE |
| AGE | INTEGER | FALSE |
| TLNO | VARCHAR(50) | TRUE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 132201">

`PATIENT` 테이블에서 12세 이하인 여자환자의 환자이름, 환자번호, 성별코드, 나이, 전화번호를 조회하는 SQL문을 작성해주세요. 이때 전화번호가 없는 경우, 'NONE'으로 출력시켜 주시고 결과는 나이를 기준으로 내림차순 정렬하고, 나이 같다면 환자이름을 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #04-1. 입출력 예시 (1)

`PATIENT` 테이블이 다음과 같을 때

| PT_NO | PT_NAME | GEND_CD | AGE | TLNO |
| --- | --- | --- | --- | --- |
| PT22000003 | 브라운 | M | 18 | 01031246641 |
| PT22000004 | 크롱 | M | 7 | NULL |
| PT22000006 | 뽀뽀 | W | 8 | NULL |
| PT22000009 | 한나 | W | 12 | 01032323117 |
| PT22000012 | 뿡뿡이 | M | 5 | NULL |
| PT22000013 | 크리스 | M | 30 | 01059341192 |
| PT22000014 | 토프 | W | 22 | 01039458213 |
| PT22000018 | 안나 | W | 11 | NULL |
| PT22000019 | 바라 | W | 10 | 01079068799 |
| PT22000021 | 릴로 | W | 33 | 01023290767 |

---

### #04-2. 입출력 예시 (2)

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| PT_NAME | PT_NO | GEND_CD | AGE | TLNO |
| --- | --- | --- | --- | --- |
| 한나 | PT22000009 | W | 12 | 01032323117 |
| 안나 | PT22000018 | W | 11 | NONE |
| 바라 | PT22000019 | W | 10 | 01079068799 |
| 뽀뽀 | PT22000006 | W | 8 | NONE |

---
class: tight
---

## #05. 문제 5 — 흉부외과 또는 일반외과 의사 목록 출력하기

<Grid cols="2" align="start">
<div>

다음은 종합병원에 속한 의사 정보를 담은`DOCTOR` 테이블입니다. `DOCTOR` 테이블은 다음과 같으며 `DR_NAME`, `DR_ID`, `LCNS_NO`, `HIRE_YMD`, `MCDP_CD`, `TLNO`는 각각 의사이름, 의사ID, 면허번호, 고용일자, 진료과코드, 전화번호를 나타냅니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| DR_NAME | VARCHAR(20) | FALSE |
| DR_ID | VARCHAR(10) | FALSE |
| LCNS_NO | VARCHAR(30) | FALSE |
| HIRE_YMD | DATE | FALSE |
| MCDP_CD | VARCHAR(6) | TRUE |
| TLNO | VARCHAR(50) | TRUE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 132203">

`DOCTOR` 테이블에서 진료과가 흉부외과(CS)이거나 일반외과(GS)인 의사의 이름, 의사ID, 진료과, 고용일자를 조회하는 SQL문을 작성해주세요. 이때 결과는 고용일자를 기준으로 내림차순 정렬하고, 고용일자가 같다면 이름을 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #05-1. 입출력 예시 (1)

`DOCTOR` 테이블이 다음과 같을 때

| DR_NAME | DR_ID | LCNS_NO | HIRE_YMD | MCDP_CD | TLNO |
| --- | --- | --- | --- | --- | --- |
| 루피 | DR20090029 | LC00010001 | 2009-03-01 | CS | 01085482011 |
| 패티 | DR20090001 | LC00010901 | 2009-07-01 | CS | 01085220122 |
| 뽀로로 | DR20170123 | LC00091201 | 2017-03-01 | GS | 01034969210 |
| 티거 | DR20100011 | LC00011201 | 2010-03-01 | NP | 01034229818 |
| 품바 | DR20090231 | LC00011302 | 2015-11-01 | OS | 01049840278 |
| 티몬 | DR20090112 | LC00011162 | 2010-03-01 | FM | 01094622190 |
| 니모 | DR20200012 | LC00911162 | 2020-03-01 | CS | 01089483921 |
| 오로라 | DR20100031 | LC00010327 | 2010-11-01 | OS | 01098428957 |
| 자스민 | DR20100032 | LC00010192 | 2010-03-01 | GS | 01023981922 |
| 벨 | DR20100039 | LC00010562 | 2010-07-01 | GS | 01058390758 |

---

### #05-2. 입출력 예시 (2)

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| DR_NAME | DR_ID | MCDP_CD | HIRE_YMD |
| --- | --- | --- | --- |
| 니모 | DR20200012 | CS | 2020-03-01 |
| 뽀로로 | DR20170123 | GS | 2017-03-01 |
| 벨 | DR20100039 | GS | 2010-07-01 |
| 자스민 | DR20100032 | GS | 2010-03-01 |
| 패티 | DR20090001 | CS | 2009-07-01 |
| 루피 | DR20090029 | CS | 2009-03-01 |

---
class: tight
---

## #06. 문제 6 — 조건에 맞는 도서 리스트 출력하기

<Grid cols="2" align="start">
<div>

다음은 어느 한 서점에서 판매중인 도서들의 도서 정보(`BOOK`) 테이블입니다.

`BOOK` 테이블은 각 도서의 정보를 담은 테이블로 아래와 같은 구조로 되어있습니다.

</div>
<div>

| Column name | Type | Nullable | Description |
| --- | --- | --- | --- |
| BOOK_ID | INTEGER | FALSE | 도서 ID |
| CATEGORY | VARCHAR(N) | FALSE | 카테고리 (경제, 인문, 소설, 생활, 기술) |
| AUTHOR_ID | INTEGER | FALSE | 저자 ID |
| PRICE | INTEGER | FALSE | 판매가 (원) |
| PUBLISHED_DATE | DATE | FALSE | 출판일 |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 144853">

`BOOK` 테이블에서 `2021년`에 출판된 `'인문'` 카테고리에 속하는 도서 리스트를 찾아서 도서 ID(`BOOK_ID`), 출판일 (`PUBLISHED_DATE`)을 출력하는 SQL문을 작성해주세요.     결과는 출판일을 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #06-1. 입출력 예시 (1)

예를 들어 `BOOK` 테이블이 다음과 같다면

| BOOK_ID | CATEGORY | AUTHOR_ID | PRICE | PUBLISHED_DATE |
| --- | --- | --- | --- | --- |
| 1 | 인문 | 1 | 10000 | 2020-01-01 |
| 2 | 경제 | 2 | 9000 | 2021-02-05 |
| 3 | 인문 | 2 | 11000 | 2021-04-11 |
| 4 | 인문 | 3 | 10000 | 2021-03-15 |
| 5 | 생활 | 1 | 12000 | 2021-01-10 |

---

### #06-2. 입출력 예시 (2)

조건에 속하는 도서는 도서 ID 가 3, 4인 도서이므로 다음과 같습니다.

| BOOK_ID | PUBLISHED_DATE |
| --- | --- |
| 3 | 2021-04-11 |
| 4 | 2021-03-15 |

그리고 출판일 오름차순으로 정렬하여야 하므로 다음과 같은 결과가 나와야 합니다.

| BOOK_ID | PUBLISHED_DATE |
| --- | --- |
| 4 | 2021-03-15 |
| 3 | 2021-04-11 |

---

## #07. 문제 7 — 자동차 대여 기록에서 장기/단기 대여 구분하기

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 1 · 프로그래머스 151138">

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 대여 시작일이 2022년 9월에 속하는 대여 기록에 대해서 대여 기간이 30일 이상이면 '장기 대여' 그렇지 않으면 '단기 대여' 로 표시하는 컬럼(컬럼명: `RENT_TYPE`)을 추가하여 대여기록을 출력하는 SQL문을 작성해주세요. 결과는 대여 기록 ID를 기준으로 내림차순 정렬해주세요.

</Callout>

---

### #07-1. 입출력 예시 (1)

예를 들어 `CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블이 다음과 같다면

| HISTORY_ID | CAR_ID | START_DATE | END_DATE |
| --- | --- | --- | --- |
| 1 | 4 | 2022-09-27 | 2022-11-27 |
| 2 | 3 | 2022-10-03 | 2022-11-04 |
| 3 | 2 | 2022-09-05 | 2022-09-05 |
| 4 | 1 | 2022-09-01 | 2022-09-30 |
| 5 | 3 | 2022-09-16 | 2022-10-15 |

---

### #07-2. 입출력 예시 (2)

2022년 9월의 대여 기록 중 '장기 대여' 에 해당하는 기록은 대여 기록 ID가 1, 4인 기록이고, '단기 대여' 에 해당하는 기록은 대여 기록 ID가 3, 5 인 기록이므로 대여 기록 ID를 기준으로 내림차순 정렬하면 다음과 같이 나와야 합니다.

| HISTORY_ID | CAR_ID | START_DATE | END_DATE | RENT_TYPE |
| --- | --- | --- | --- | --- |
| 5 | 3 | 2022-09-16 | 2022-10-13 | 단기 대여 |
| 4 | 1 | 2022-09-01 | 2022-09-30 | 장기 대여 |
| 3 | 2 | 2022-09-05 | 2022-09-05 | 단기 대여 |
| 1 | 4 | 2022-09-27 | 2022-10-26 | 장기 대여 |

---

## #08. 문제 8 — 동물 수 구하기

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59406">

동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.

</Callout>

---

### #08-1. 입출력 예시

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A399552 | Dog | 2013-10-14 15:38:00 | Normal | Jack | Neutered Male |
| A379998 | Dog | 2013-10-23 11:42:00 | Normal | Disciple | Intact Male |
| A370852 | Dog | 2013-11-03 15:04:00 | Normal | Katie | Spayed Female |
| A403564 | Dog | 2013-11-18 17:03:00 | Normal | Anna | Spayed Female |

동물 보호소에 들어온 동물은 4마리입니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| count |
| --- |
| 4 |

※ 컬럼 이름(위 예제에서는 count)은 일치하지 않아도 됩니다.

---
class: tight
---

## #09. 문제 9 — NULL 처리하기

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59410">

입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

</Callout>

---

### #09-1. 입출력 예시

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A350276 | Cat | 2017-08-13 13:50:00 | Normal | Jewel | Spayed Female |
| A350375 | Cat | 2017-03-06 15:01:00 | Normal | Meo | Neutered Male |
| A368930 | Dog | 2014-06-08 13:20:00 | Normal | NULL | Spayed Female |

마지막 줄의 개는 이름이 없기 때문에, 이 개의 이름은 "No name"으로 표시합니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_TYPE | NAME | SEX_UPON_INTAKE |
| --- | --- | --- |
| Cat | Jewel | Spayed Female |
| Cat | Meo | Neutered Male |
| Dog | No name | Spayed Female |

※ 컬럼 이름은 일치하지 않아도 됩니다.

---

## #10. 문제 10 — DATETIME에서 DATE로 형 변환

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59414">

`ANIMAL_INS` 테이블에 등록된 모든 레코드에 대해, 각 동물의 아이디와 이름, 들어온 날짜[1]를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.

</Callout>

---

### #10-1. 입출력 예시 (1)

예를 들어, `ANIMAL_INS` 테이블이 다음과 같다면

`ANIMAL_INS`

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A349996 | Cat | 2018-01-22 14:32:00 | Normal | Sugar | Neutered Male |
| A350276 | Cat | 2017-08-13 13:50:00 | Normal | Jewel | Spayed Female |
| A350375 | Cat | 2017-03-06 15:01:00 | Normal | Meo | Neutered Male |
| A352555 | Dog | 2014-08-08 04:20:00 | Normal | Harley | Spayed Female |
| A352713 | Cat | 2017-04-13 16:29:00 | Normal | Gia | Spayed Female |

---

### #10-2. 입출력 예시 (2)

SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME | 날짜 |
| --- | --- | --- |
| A349996 | Sugar | 2018-01-22 |
| A350276 | Jewel | 2017-08-13 |
| A350375 | Meo | 2017-03-06 |
| A352555 | Harley | 2014-08-08 |
| A352713 | Gia | 2017-04-13 |

시각(시-분-초)을 제외한 날짜(년-월-일)만 보여주세요.

---

## #11. 문제 11 — 3월에 태어난 여성 회원 목록 출력하기

<Grid cols="2" align="start">
<div>

다음은 식당 리뷰 사이트의 회원 정보를 담은 `MEMBER_PROFILE` 테이블입니다. `MEMBER_PROFILE` 테이블은 다음과 같으며 `MEMBER_ID`, `MEMBER_NAME`, `TLNO`, `GENDER`, `DATE_OF_BIRTH`는 회원 ID, 회원 이름, 회원 연락처, 성별, 생년월일을 의미합니다.

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| MEMBER_ID | VARCHAR(100) | FALSE |
| MEMBER_NAME | VARCHAR(50) | FALSE |
| TLNO | VARCHAR(50) | TRUE |
| GENDER | VARCHAR(1) | TRUE |
| DATE_OF_BIRTH | DATE | TRUE |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 131120">

`MEMBER_PROFILE` 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문을 작성해주세요. 이때 전화번호가 NULL인 경우는 출력대상에서 제외시켜 주시고, 결과는 회원ID를 기준으로 오름차순 정렬해주세요.

</Callout>

---

### #11-1. 입출력 예시

`MEMBER_PROFILE` 테이블이 다음과 같을 때

| MEMBER_ID | MEMBER_NAME | TLNO | GENDER | DATE_OF_BIRTH |
| --- | --- | --- | --- | --- |
| `jiho92@naver.com` | 이지호 | 01076432111 | W | 1992-02-12 |
| `jiyoon22@hotmail.com` | 김지윤 | 01032324117 | W | 1992-02-22 |
| `jihoon93@hanmail.net` | 김지훈 | 01023258688 | M | 1993-02-23 |
| `seoyeons@naver.com` | 박서연 | 01076482209 | W | 1993-03-16 |
| `yoonsy94@gmail.com` | 윤서연 | NULL | W | 1994-03-19 |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| MEMBER_ID | MEMBER_NAME | GENDER | DATE_OF_BIRTH |
| --- | --- | --- | --- |
| `seoyeons@naver.com` | 박서연 | W | 1993-03-16 |

---
class: tight
---

## #12. 문제 12 — 중성화 여부 파악하기

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

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 59409">

보호소의 동물이 중성화되었는지 아닌지 파악하려 합니다. 중성화된 동물은 `SEX_UPON_INTAKE` 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다. 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.

</Callout>

---

### #12-1. 입출력 예시 (1)

예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면

| ANIMAL_ID | ANIMAL_TYPE | DATETIME | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
| --- | --- | --- | --- | --- | --- |
| A355753 | Dog | 2015-09-10 13:14:00 | Normal | Elijah | Neutered Male |
| A373219 | Cat | 2014-07-29 11:43:00 | Normal | Ella | Spayed Female |
| A382192 | Dog | 2015-03-13 13:14:00 | Normal | Maxwell 2 | Intact Male |

- 중성화한 동물: Elijah, Ella
- 중성화하지 않은 동물: Maxwell 2

---

### #12-2. 입출력 예시 (2)

따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.

| ANIMAL_ID | NAME | 중성화 |
| --- | --- | --- |
| A355753 | Elijah | O |
| A373219 | Ella | O |
| A382192 | Maxwell 2 | X |

※ 컬럼 이름은 일치하지 않아도 됩니다.

---
class: tight
---

## #13. 문제 13 — 조건에 부합하는 중고거래 상태 조회하기

<Grid cols="2" align="start">
<div>

다음은 중고거래 게시판 정보를 담은 `USED_GOODS_BOARD` 테이블입니다. `USED_GOODS_BOARD` 테이블은 다음과 같으며 `BOARD_ID`, `WRITER_ID`, `TITLE`, `CONTENTS`, `PRICE`, `CREATED_DATE`, `STATUS`, `VIEWS`은 게시글 ID, 작성자 ID, 게시글 제목, 게시글 내용, 가격, 작성일, 거래상태, 조회수를 의미합니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 2 · 프로그래머스 164672">

`USED_GOODS_BOARD` 테이블에서 2022년 10월 5일에 등록된 중고거래 게시물의 게시글 ID, 작성자 ID, 게시글 제목, 가격, 거래상태를 조회하는 SQL문을 작성해주세요. 거래상태가 SALE 이면 판매중, RESERVED이면 예약중, DONE이면 거래완료 분류하여 출력해주시고, 결과는 게시글 ID를 기준으로 내림차순 정렬해주세요.

</Callout>

</div>
<div>

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
</Grid>

---

### #13-1. 입출력 예시

`USED_GOODS_BOARD` 테이블이 다음과 같을 때

| BOARD_ID | WRITER_ID | TITLE | CONTENTS | PRICE | CREATED_DATE | STATUS | VIEWS |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B0007 | s2s2123 | 커피글라인더 | 새상품처럼 깨끗합니다. | 7000 | 2022-10-04 | DONE | 210 |
| B0008 | hong02 | 자전거 판매합니다 | 출퇴근용으로 구매했다가 사용하지 않아서 내놔요 | 40000 | 2022-10-04 | SALE | 301 |
| B0009 | yawoong67 | 선반 팝니다 | 6단 선반. 환불 반품 안됩니다. | 12000 | 2022-10-05 | DONE | 202 |
| B0010 | keel1990 | 철제선반5단 | 철제선반 5단 조립식 팜 | 10000 | 2022-10-05 | SALE | 194 |

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| BOARD_ID | WRITER_ID | TITLE | PRICE | STATUS |
| --- | --- | --- | --- | --- |
| B0010 | keel1990 | 철제선반5단 | 10000 | 판매중 |
| B0009 | yawoong67 | 선반 팝니다 | 12000 | 거래완료 |

---
class: tight
---

## #14. 문제 14 — 조건별로 분류하여 주문상태 출력하기

<Grid cols="2" align="start">
<div>

다음은 식품공장의 주문정보를 담은 `FOOD_ORDER` 테이블입니다. `FOOD_ORDER` 테이블은 다음과 같으며 `ORDER_ID`, `PRODUCT_ID`, `AMOUNT`, `PRODUCE_DATE`, `IN_DATE`,`OUT_DATE`,`FACTORY_ID`, `WAREHOUSE_ID`는 각각 주문 ID, 제품 ID, 주문양, 생산일자, 입고일자, 출고일자, 공장 ID, 창고 ID를 의미합니다.

<Callout kind="plain" color="py" icon="📝" title="문제" tag="Level 3 · 프로그래머스 131113">

`FOOD_ORDER` 테이블에서 2022년 5월 1일을 기준으로 주문 ID, 제품 ID, 출고일자, 출고여부를 조회하는 SQL문을 작성해주세요. 출고여부는 2022년 5월 1일까지 출고완료로 이 후 날짜는 출고 대기로 미정이면 출고미정으로 출력해주시고, 결과는 주문 ID를 기준으로 오름차순 정렬해주세요.

</Callout>

</div>
<div>

| Column name | Type | Nullable |
| --- | --- | --- |
| ORDER_ID | VARCHAR(10) | FALSE |
| PRODUCT_ID | VARCHAR(5) | FALSE |
| AMOUNT | NUMBER | FALSE |
| PRODUCE_DATE | DATE | TRUE |
| IN_DATE | DATE | TRUE |
| OUT_DATE | DATE | TRUE |
| FACTORY_ID | VARCHAR(10) | FALSE |
| WAREHOUSE_ID | VARCHAR(10) | FALSE |

</div>
</Grid>

---

### #14-1. 입출력 예시 (1)

`FOOD_ORDER` 테이블이 다음과 같을 때

| ORDER_ID | PRODUCT_ID | AMOUNT | PRODUCE_DATE | IN_DATE | OUT_DATE | FACTORY_ID | WAREHOUSE_ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OD00000051 | P0002 | 4000 | 2022-04-01 | 2022-04-21 | 2022-04-21 | FT19970003 | WH0005 |
| OD00000052 | P0003 | 2500 | 2022-04-10 | 2022-04-27 | 2022-04-27 | FT19970003 | WH0006 |
| OD00000053 | P0005 | 6200 | 2022-04-15 | 2022-04-30 | 2022-05-01 | FT19940003 | WH0003 |
| OD00000054 | P0006 | 1000 | 2022-04-21 | 2022-04-30 | NULL | FT19940003 | WH0009 |
| OD00000055 | P0008 | 1500 | 2022-04-25 | 2022-05-11 | 2022-05-11 | FT19980003 | WH0009 |

---

### #14-2. 입출력 예시 (2)

SQL을 실행하면 다음과 같이 출력되어야 합니다.

| ORDER_ID | PRODUCT_ID | OUT_DATE | 출고여부 |
| --- | --- | --- | --- |
| OD00000051 | P0002 | 2022-04-21 | 출고완료 |
| OD00000052 | P0003 | 2022-04-27 | 출고완료 |
| OD00000053 | P0005 | 2022-05-01 | 출고완료 |
| OD00000054 | P0006 |  | 출고미정 |
| OD00000055 | P0008 | 2022-05-11 | 출고대기 |


---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-03] SQL 함수 6 · ITWILL · {teacher} 강사</p>

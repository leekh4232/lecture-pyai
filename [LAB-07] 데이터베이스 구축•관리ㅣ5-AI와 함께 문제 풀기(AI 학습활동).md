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

<p class="sub">[LAB-07] 데이터베이스 구축•관리 (5) / ITWILL - 주영아·이광호 강사</p>

---
layout: section
---

# SQL 코딩 테스트

앞서 배운 상황별 템플릿으로 프롬프트를 직접 작성하여 문제를 풀어보세요

---
class: tight
---

## #01. 문제 1 — 카페 메뉴 테이블 만들기

<Grid cols="2" align="start">
<div>

카페의 메뉴 정보를 담을 `LAB07_menus` 테이블을 만들려고 합니다. `name`, `price`, `category`, `is_hot`, `released_date`, `description`은 메뉴 이름, 가격(원), 분류, 따뜻한 음료 여부, 출시일, 메뉴 설명을 의미합니다.

</div>
<div>

| 컬럼 이름 | 자료형 | 제약 조건 |
| --- | --- | --- |
| name | VARCHAR(30) | NOT NULL |
| price | INT | NOT NULL |
| category | VARCHAR(20) | NOT NULL, 기본값 '커피' |
| is_hot | BOOLEAN | NOT NULL, 기본값 1 |
| released_date | DATE | 없음 |
| description | TEXT | 없음 |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

표의 자료형과 제약 조건대로 `LAB07_menus` 테이블을 만드는 SQL문을 작성해주세요. 각 컬럼에는 뜻을 COMMENT로 붙이고, 문자셋은 utf8mb4, 콜레이션은 utf8mb4_bin으로 지정해주세요.

</Callout>

---

### #01-1. 입출력 예시

SQL을 실행한 뒤 `DESC LAB07_menus;`를 실행하면 다음과 같이 출력되어야 합니다.

| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| name | varchar(30) | NO |  | NULL |  |
| price | int(11) | NO |  | NULL |  |
| category | varchar(20) | NO |  | 커피 |  |
| is_hot | tinyint(1) | NO |  | 1 |  |
| released_date | date | YES |  | NULL |  |
| description | text | YES |  | NULL |  |

---
class: tight
---

## #02. 문제 2 — 동아리 테이블에 기본키 정하기

<Grid cols="2" align="start">
<div>

학교 동아리 정보를 담을 `LAB07_clubs` 테이블을 만들려고 합니다. `id`, `name`, `room`, `max_members`, `founded_date`는 동아리 번호, 동아리 이름, 동아리방, 최대 인원, 창립일을 의미합니다.

</div>
<div>

| 컬럼 이름 | 자료형 | 제약 조건 |
| --- | --- | --- |
| id | INT | PRIMARY KEY, AUTO_INCREMENT |
| name | VARCHAR(30) | NOT NULL |
| room | VARCHAR(20) | 없음 |
| max_members | TINYINT | NOT NULL, 기본값 20 |
| founded_date | DATE | 없음 |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

표의 자료형과 제약 조건대로 `LAB07_clubs` 테이블을 만드는 SQL문을 작성해주세요. 동아리 번호는 동아리를 추가할 때마다 1씩 자동으로 늘어나야 합니다. 각 컬럼에는 뜻을 COMMENT로 붙이고, 문자셋은 utf8mb4, 콜레이션은 utf8mb4_bin으로 지정해주세요.

</Callout>

---

### #02-1. 입출력 예시

SQL을 실행한 뒤 `DESC LAB07_clubs;`를 실행하면 다음과 같이 출력되어야 합니다.

| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| id | int(11) | NO | PRI | NULL | auto_increment |
| name | varchar(30) | NO |  | NULL |  |
| room | varchar(20) | YES |  | NULL |  |
| max_members | tinyint(4) | NO |  | 20 |  |
| founded_date | date | YES |  | NULL |  |

---
class: tight
---

## #03. 문제 3 — 동아리 회원 테이블을 동아리와 연결하기

<Grid cols="2" align="start">
<div>

동아리에 가입한 회원 정보를 담을 `LAB07_club_members` 테이블을 만들려고 합니다. `id`, `club_id`, `name`, `role`, `joined_date`는 회원 번호, 소속 동아리, 회원 이름, 역할, 가입일을 의미합니다. `club_id`는 문제 2에서 만든 `LAB07_clubs` 테이블의 `id`를 가리킵니다.

</div>
<div>

| 컬럼 이름 | 자료형 | 제약 조건 |
| --- | --- | --- |
| id | INT | PRIMARY KEY, AUTO_INCREMENT |
| club_id | INT | NOT NULL, FOREIGN KEY → LAB07_clubs(id) |
| name | VARCHAR(20) | NOT NULL |
| role | ENUM('회장', '총무', '부원') | NOT NULL, 기본값 '부원' |
| joined_date | DATE | NOT NULL |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

표의 자료형과 제약 조건대로 `LAB07_club_members` 테이블을 만드는 SQL문을 작성해주세요. `club_id`는 `LAB07_clubs` 테이블의 `id`를 참조하는 외래키로 지정해주세요. 각 컬럼에는 뜻을 COMMENT로 붙이고, 문자셋은 utf8mb4, 콜레이션은 utf8mb4_bin으로 지정해주세요.

</Callout>

---

### #03-1. 입출력 예시

SQL을 실행한 뒤 `DESC LAB07_club_members;`를 실행하면 다음과 같이 출력되어야 합니다.

| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| id | int(11) | NO | PRI | NULL | auto_increment |
| club_id | int(11) | NO | MUL | NULL |  |
| name | varchar(20) | NO |  | NULL |  |
| role | enum('회장','총무','부원') | NO |  | 부원 |  |
| joined_date | date | NO |  | NULL |  |

---
class: tight
---

## #04. 문제 4 — 카페 메뉴 테이블 고치기

<Grid cols="2" align="start">
<div>

다음은 문제 1에서 만든 `LAB07_menus` 테이블입니다. `name`, `price`, `category`, `is_hot`, `released_date`, `description`은 메뉴 이름, 가격(원), 분류, 따뜻한 음료 여부, 출시일, 메뉴 설명을 의미합니다.

</div>
<div>

| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| name | varchar(30) | NO |  | NULL |  |
| price | int(11) | NO |  | NULL |  |
| category | varchar(20) | NO |  | 커피 |  |
| is_hot | tinyint(1) | NO |  | 1 |  |
| released_date | date | YES |  | NULL |  |
| description | text | YES |  | NULL |  |

</div>
</Grid>

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

`LAB07_menus` 테이블을 다음과 같이 고치는 SQL문을 작성해주세요. 첫째, 열량을 저장할 `calorie` 컬럼을 SMALLINT 자료형, 기본값 0으로 추가합니다. 둘째, 긴 메뉴 이름도 저장할 수 있게 `name` 컬럼을 VARCHAR(50)으로 바꿉니다. 이때 `name`은 계속 NULL을 허용하지 않아야 합니다. 바뀌는 컬럼에도 뜻을 COMMENT로 붙여주세요.

</Callout>

---

### #04-1. 입출력 예시

SQL을 실행한 뒤 `DESC LAB07_menus;`를 실행하면 다음과 같이 출력되어야 합니다.

| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| name | varchar(50) | NO |  | NULL |  |
| price | int(11) | NO |  | NULL |  |
| category | varchar(20) | NO |  | 커피 |  |
| is_hot | tinyint(1) | NO |  | 1 |  |
| released_date | date | YES |  | NULL |  |
| description | text | YES |  | NULL |  |
| calorie | smallint(6) | YES |  | 0 |  |

---

## #05. 문제 5 — ERD를 보고 스터디룸 예약 테이블 만들기

스터디카페의 회원 · 스터디룸 · 예약을 DBML로 그린 ERD입니다. 예약 하나는 회원 한 명과 스터디룸 하나를 가리킵니다. ERD는 다음 쪽에 있습니다.

| 관계 | 자식 컬럼 | 부모 컬럼 |
| --- | --- | --- |
| 회원 1 : N 예약 | LAB07_reservations.member_id | LAB07_members.id |
| 스터디룸 1 : N 예약 | LAB07_reservations.room_id | LAB07_rooms.id |

<Callout kind="plain" color="py" icon="📝" title="문제" tag="직접 만든 문제">

ERD대로 `LAB07_members`, `LAB07_rooms`, `LAB07_reservations` 세 테이블을 만드는 SQL문을 작성해주세요. ERD의 `ref`는 외래키로, `note`는 COMMENT로 옮기고, 문자셋은 utf8mb4, 콜레이션은 utf8mb4_bin으로 지정해주세요. 다른 테이블을 참조하는 테이블은 참조되는 테이블보다 나중에 만들어야 합니다.

</Callout>

---
class: dense
---

### #05-1. ERD

<Grid cols="2" align="start">
<div>

```text
Table LAB07_members {
  id int [pk, increment, note: "회원 번호"]
  name varchar(20) [not null, note: "회원 이름"]
  phone varchar(20) [not null, unique, note: "전화번호"]
}
Table LAB07_rooms {
  id int [pk, increment, note: "스터디룸 번호"]
  room_name varchar(20) [not null, note: "스터디룸 이름"]
  capacity tinyint [not null, default: 4, note: "정원"]
}
```

</div>
<div>

```text
Table LAB07_reservations {
  id int [pk, increment, note: "예약 번호"]
  member_id int [not null, note: "예약한 회원", ref: > LAB07_members.id]
  room_id int [not null, note: "예약한 스터디룸", ref: > LAB07_rooms.id]
  reserved_date date [not null, note: "이용 날짜"]
  start_time time [not null, note: "시작 시각"]
  hours tinyint [not null, default: 1, note: "이용 시간"]
}
```

</div>
</Grid>

---

### #05-2. 입출력 예시 (1)

SQL을 실행한 뒤 `DESC LAB07_members;`를 실행하면 다음과 같이 출력되어야 합니다.

| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| id | int(11) | NO | PRI | NULL | auto_increment |
| name | varchar(20) | NO |  | NULL |  |
| phone | varchar(20) | NO | UNI | NULL |  |

`DESC LAB07_rooms;`를 실행하면 다음과 같이 출력되어야 합니다.

| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| id | int(11) | NO | PRI | NULL | auto_increment |
| room_name | varchar(20) | NO |  | NULL |  |
| capacity | tinyint(4) | NO |  | 4 |  |

---

### #05-3. 입출력 예시 (2)

`DESC LAB07_reservations;`를 실행하면 다음과 같이 출력되어야 합니다.

| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| id | int(11) | NO | PRI | NULL | auto_increment |
| member_id | int(11) | NO | MUL | NULL |  |
| room_id | int(11) | NO | MUL | NULL |  |
| reserved_date | date | NO |  | NULL |  |
| start_time | time | NO |  | NULL |  |
| hours | tinyint(4) | NO |  | 1 |  |


---
layout: cover
hideInToc: true
---

# 감사합니다

질문과 토론 환영

<p class="sub">[LAB-07] 데이터베이스 구축•관리 5 · ITWILL · {teacher} 강사</p>

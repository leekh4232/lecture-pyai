# [LAB-07] 데이터베이스 구축•관리ㅣ5-AI와 함께 문제 풀기 모범답안

「[LAB-07] 데이터베이스 구축•관리ㅣ5-AI와 함께 문제 풀기(AI 학습활동)」 덱의 문제 5개에 대한 정답 SQL과, 두 템플릿(방향 묻기 · 원인 묻기)을 빈칸 없이 채운 프롬프트를 담았다.

## 문제 1. 카페 메뉴 테이블 만들기

- Level 1 · 직접 만든 문제 · CREATE TABLE

### 정답 SQL

```sql
CREATE TABLE LAB07_menus (
    name VARCHAR(30) NOT NULL COMMENT '메뉴 이름',
    price INT NOT NULL COMMENT '가격(원)',
    category VARCHAR(20) NOT NULL DEFAULT '커피' COMMENT '분류',
    is_hot BOOLEAN NOT NULL DEFAULT 1 COMMENT '따뜻한 음료 여부',
    released_date DATE COMMENT '출시일',
    description TEXT COMMENT '메뉴 설명'
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='카페 메뉴';
```

- 확인 결과: `DESC LAB07_menus;`

```text
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| name          | varchar(30) | NO   |     | NULL    |       |
| price         | int(11)     | NO   |     | NULL    |       |
| category      | varchar(20) | NO   |     | 커피    |       |
| is_hot        | tinyint(1)  | NO   |     | 1       |       |
| released_date | date        | YES  |     | NULL    |       |
| description   | text        | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
```

- 풀이 핵심: 컬럼마다 `이름 자료형 제약조건 COMMENT` 순서로 쓰고, 기본값은 `DEFAULT 값`으로 정함. BOOLEAN은 DESC에서 `tinyint(1)`로 보임

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
만들 테이블: LAB07_menus (카페 메뉴)
- name VARCHAR(30) · NOT NULL · 메뉴 이름
- price INT · NOT NULL · 가격(원)
- category VARCHAR(20) · NOT NULL, 기본값 '커피' · 분류
- is_hot BOOLEAN · NOT NULL, 기본값 1 · 따뜻한 음료 여부
- released_date DATE · 제약 없음 · 출시일
- description TEXT · 제약 없음 · 메뉴 설명
- 그 밖의 조건: 컬럼마다 COMMENT, 문자셋 utf8mb4 · 콜레이션 utf8mb4_bin
- 내가 이해한 문제: 위 6개 컬럼을 가진 LAB07_menus 테이블을 CREATE TABLE로 만들고, 기본값이 있는 컬럼에는 기본값을 정함

## 질문
내 이해가 맞는지 봐 주고, 필요한 구문과 순서를 알려줘.

## 제약
- CREATE TABLE · 자료형 · 제약 조건(NOT NULL · DEFAULT · UNIQUE · PRIMARY KEY · AUTO_INCREMENT · FOREIGN KEY) · COMMENT · ALTER TABLE 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `is_hot`에 `DEFAULT 1`을 빠뜨려 기본값이 NULL로 나옴

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
카페 메뉴 테이블 LAB07_menus를 만들려고 해. is_hot은 BOOLEAN, NOT NULL, 기본값 1이어야 해.
```sql
CREATE TABLE LAB07_menus (
    name VARCHAR(30) NOT NULL COMMENT '메뉴 이름',
    price INT NOT NULL COMMENT '가격(원)',
    category VARCHAR(20) NOT NULL DEFAULT '커피' COMMENT '분류',
    is_hot BOOLEAN NOT NULL COMMENT '따뜻한 음료 여부',
    released_date DATE COMMENT '출시일',
    description TEXT COMMENT '메뉴 설명'
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='카페 메뉴';
```
- 기대한 결과: DESC에서 is_hot 행이 (tinyint(1), NO, Default 1)
- 실제 결과: DESC에서 is_hot 행이 (tinyint(1), NO, Default NULL)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 2. 동아리 테이블에 기본키 정하기

- Level 1 · 직접 만든 문제 · PRIMARY KEY

### 정답 SQL

```sql
CREATE TABLE LAB07_clubs (
    id INT AUTO_INCREMENT COMMENT '동아리 번호',
    name VARCHAR(30) NOT NULL COMMENT '동아리 이름',
    room VARCHAR(20) COMMENT '동아리방',
    max_members TINYINT NOT NULL DEFAULT 20 COMMENT '최대 인원',
    founded_date DATE COMMENT '창립일',
    PRIMARY KEY (id)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='동아리';
```

- 확인 결과: `DESC LAB07_clubs;`

```text
+--------------+-------------+------+-----+---------+----------------+
| Field        | Type        | Null | Key | Default | Extra          |
+--------------+-------------+------+-----+---------+----------------+
| id           | int(11)     | NO   | PRI | NULL    | auto_increment |
| name         | varchar(30) | NO   |     | NULL    |                |
| room         | varchar(20) | YES  |     | NULL    |                |
| max_members  | tinyint(4)  | NO   |     | 20      |                |
| founded_date | date        | YES  |     | NULL    |                |
+--------------+-------------+------+-----+---------+----------------+
```

- 풀이 핵심: 기본키는 `id INT PRIMARY KEY AUTO_INCREMENT`처럼 컬럼 뒤에 쓰거나, 마지막 줄에 `PRIMARY KEY (id)`로 따로 씀. 두 방법 모두 DESC 결과가 같음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
만들 테이블: LAB07_clubs (동아리)
- id INT · PRIMARY KEY, AUTO_INCREMENT · 동아리 번호
- name VARCHAR(30) · NOT NULL · 동아리 이름
- room VARCHAR(20) · 제약 없음 · 동아리방
- max_members TINYINT · NOT NULL, 기본값 20 · 최대 인원
- founded_date DATE · 제약 없음 · 창립일
- 그 밖의 조건: 컬럼마다 COMMENT, 문자셋 utf8mb4 · 콜레이션 utf8mb4_bin
- 내가 이해한 문제: 동아리 번호가 1씩 자동으로 늘어나는 기본키가 되도록 LAB07_clubs 테이블을 만듦

## 질문
내 이해가 맞는지 봐 주고, 필요한 구문과 순서를 알려줘.

## 제약
- CREATE TABLE · 자료형 · 제약 조건(NOT NULL · DEFAULT · UNIQUE · PRIMARY KEY · AUTO_INCREMENT · FOREIGN KEY) · COMMENT · ALTER TABLE 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `AUTO_INCREMENT`만 쓰고 `PRIMARY KEY`를 빠뜨려 테이블이 만들어지지 않음

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
동아리 테이블 LAB07_clubs를 만들려고 해. id는 1씩 자동으로 늘어나는 기본키여야 해.
```sql
CREATE TABLE LAB07_clubs (
    id INT AUTO_INCREMENT COMMENT '동아리 번호',
    name VARCHAR(30) NOT NULL COMMENT '동아리 이름',
    room VARCHAR(20) COMMENT '동아리방',
    max_members TINYINT NOT NULL DEFAULT 20 COMMENT '최대 인원',
    founded_date DATE COMMENT '창립일'
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='동아리';
```
- 기대한 결과: 테이블이 만들어지고 DESC에서 id 행이 (int(11), NO, PRI, auto_increment)
- 실제 결과: ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 3. 동아리 회원 테이블을 동아리와 연결하기

- Level 1 · 직접 만든 문제 · FOREIGN KEY

### 정답 SQL

```sql
-- 부모 테이블 LAB07_clubs(문제 2)가 먼저 있어야 함
CREATE TABLE LAB07_club_members (
    id INT AUTO_INCREMENT COMMENT '회원 번호',
    club_id INT NOT NULL COMMENT '소속 동아리',
    name VARCHAR(20) NOT NULL COMMENT '회원 이름',
    role ENUM('회장', '총무', '부원') NOT NULL DEFAULT '부원' COMMENT '역할',
    joined_date DATE NOT NULL COMMENT '가입일',
    PRIMARY KEY (id),
    FOREIGN KEY (club_id) REFERENCES LAB07_clubs(id)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='동아리 회원';
```

- 확인 결과: `DESC LAB07_club_members;`

```text
+-------------+----------------------------------+------+-----+---------+----------------+
| Field       | Type                             | Null | Key | Default | Extra          |
+-------------+----------------------------------+------+-----+---------+----------------+
| id          | int(11)                          | NO   | PRI | NULL    | auto_increment |
| club_id     | int(11)                          | NO   | MUL | NULL    |                |
| name        | varchar(20)                      | NO   |     | NULL    |                |
| role        | enum('회장','총무','부원')       | NO   |     | 부원    |                |
| joined_date | date                             | NO   |     | NULL    |                |
+-------------+----------------------------------+------+-----+---------+----------------+
```

- 풀이 핵심: 외래키는 `FOREIGN KEY (club_id) REFERENCES LAB07_clubs(id)`로 쓰고, 참조할 부모 테이블을 먼저 만들어 둠. 외래키 컬럼은 DESC의 Key 칸에 `MUL`로 보임

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
참조할 LAB07_clubs 테이블 구조:
+--------------+-------------+------+-----+---------+----------------+
| Field        | Type        | Null | Key | Default | Extra          |
+--------------+-------------+------+-----+---------+----------------+
| id           | int(11)     | NO   | PRI | NULL    | auto_increment |
| name         | varchar(30) | NO   |     | NULL    |                |
| room         | varchar(20) | YES  |     | NULL    |                |
| max_members  | tinyint(4)  | NO   |     | 20      |                |
| founded_date | date        | YES  |     | NULL    |                |
+--------------+-------------+------+-----+---------+----------------+
만들 테이블: LAB07_club_members (동아리 회원)
- id INT · PRIMARY KEY, AUTO_INCREMENT · 회원 번호
- club_id INT · NOT NULL, LAB07_clubs(id)를 참조하는 외래키 · 소속 동아리
- name VARCHAR(20) · NOT NULL · 회원 이름
- role ENUM('회장', '총무', '부원') · NOT NULL, 기본값 '부원' · 역할
- joined_date DATE · NOT NULL · 가입일
- 그 밖의 조건: 컬럼마다 COMMENT, 문자셋 utf8mb4 · 콜레이션 utf8mb4_bin
- 내가 이해한 문제: 회원이 어느 동아리 소속인지 club_id로 LAB07_clubs와 연결되는 LAB07_club_members 테이블을 만듦

## 질문
내 이해가 맞는지 봐 주고, 필요한 구문과 순서를 알려줘.

## 제약
- CREATE TABLE · 자료형 · 제약 조건(NOT NULL · DEFAULT · UNIQUE · PRIMARY KEY · AUTO_INCREMENT · FOREIGN KEY) · COMMENT · ALTER TABLE 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: 부모 테이블 `LAB07_clubs`를 만들지 않은 채 자식 테이블부터 만들어 외래키 에러가 남

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
동아리 회원 테이블 LAB07_club_members를 만들려고 해. club_id는 LAB07_clubs(id)를 참조하는 외래키야.
```sql
CREATE TABLE LAB07_club_members (
    id INT AUTO_INCREMENT COMMENT '회원 번호',
    club_id INT NOT NULL COMMENT '소속 동아리',
    name VARCHAR(20) NOT NULL COMMENT '회원 이름',
    role ENUM('회장', '총무', '부원') NOT NULL DEFAULT '부원' COMMENT '역할',
    joined_date DATE NOT NULL COMMENT '가입일',
    PRIMARY KEY (id),
    FOREIGN KEY (club_id) REFERENCES LAB07_clubs(id)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='동아리 회원';
```
- 기대한 결과: 테이블이 만들어지고 DESC에서 club_id 행이 (int(11), NO, MUL)
- 실제 결과: ERROR 1005 (HY000): Can't create table `myschool`.`lab07_club_members` (errno: 150 "Foreign key constraint is incorrectly formed")

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 4. 카페 메뉴 테이블 고치기

- Level 2 · 직접 만든 문제 · ALTER TABLE

### 정답 SQL

```sql
ALTER TABLE LAB07_menus ADD calorie SMALLINT DEFAULT 0 COMMENT '열량(kcal)';
ALTER TABLE LAB07_menus MODIFY name VARCHAR(50) NOT NULL COMMENT '메뉴 이름';
```

- 확인 결과: `DESC LAB07_menus;`

```text
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| name          | varchar(50) | NO   |     | NULL    |       |
| price         | int(11)     | NO   |     | NULL    |       |
| category      | varchar(20) | NO   |     | 커피    |       |
| is_hot        | tinyint(1)  | NO   |     | 1       |       |
| released_date | date        | YES  |     | NULL    |       |
| description   | text        | YES  |     | NULL    |       |
| calorie       | smallint(6) | YES  |     | 0       |       |
+---------------+-------------+------+-----+---------+-------+
```

- 풀이 핵심: 컬럼 추가는 `ADD`, 자료형 변경은 `MODIFY`. `MODIFY`는 컬럼 정의를 통째로 바꾸므로 유지할 `NOT NULL`도 다시 적어야 함. 추가한 컬럼은 맨 뒤에 붙음

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
고칠 LAB07_menus 테이블 구조:
+---------------+-------------+------+-----+---------+-------+
| Field         | Type        | Null | Key | Default | Extra |
+---------------+-------------+------+-----+---------+-------+
| name          | varchar(30) | NO   |     | NULL    |       |
| price         | int(11)     | NO   |     | NULL    |       |
| category      | varchar(20) | NO   |     | 커피    |       |
| is_hot        | tinyint(1)  | NO   |     | 1       |       |
| released_date | date        | YES  |     | NULL    |       |
| description   | text        | YES  |     | NULL    |       |
+---------------+-------------+------+-----+---------+-------+
- 바꿀 내용 1: calorie 컬럼 추가 · SMALLINT · 기본값 0 · 열량(kcal)
- 바꿀 내용 2: name 컬럼을 VARCHAR(50)으로 변경 · NOT NULL 유지
- 내가 이해한 문제: 테이블을 다시 만들지 않고 ALTER TABLE로 컬럼 하나를 추가하고, 다른 컬럼 하나의 자료형을 바꿈

## 질문
내 이해가 맞는지 봐 주고, 필요한 구문과 순서를 알려줘.

## 제약
- CREATE TABLE · 자료형 · 제약 조건(NOT NULL · DEFAULT · UNIQUE · PRIMARY KEY · AUTO_INCREMENT · FOREIGN KEY) · COMMENT · ALTER TABLE 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: `MODIFY`에서 `NOT NULL`을 다시 쓰지 않아 `name`이 NULL을 허용하게 됨

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
LAB07_menus 테이블에 calorie 컬럼(SMALLINT, 기본값 0)을 추가하고, name 컬럼을 NOT NULL을 유지한 채 VARCHAR(50)으로 바꾸려고 해.
고치기 전 name 행: (varchar(30), NO, Default NULL)
```sql
ALTER TABLE LAB07_menus ADD calorie SMALLINT DEFAULT 0 COMMENT '열량(kcal)';
ALTER TABLE LAB07_menus MODIFY name VARCHAR(50) COMMENT '메뉴 이름';
```
- 기대한 결과: DESC에서 name 행이 (varchar(50), Null NO)
- 실제 결과: DESC에서 name 행이 (varchar(50), Null YES)

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

## 문제 5. ERD를 보고 스터디룸 예약 테이블 만들기

- Level 2 · 직접 만든 문제 · ERD 기반 설계

### 정답 SQL

```sql
CREATE TABLE LAB07_members (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '회원 번호',
    name VARCHAR(20) NOT NULL COMMENT '회원 이름',
    phone VARCHAR(20) NOT NULL UNIQUE COMMENT '전화번호'
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='회원';

CREATE TABLE LAB07_rooms (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '스터디룸 번호',
    room_name VARCHAR(20) NOT NULL COMMENT '스터디룸 이름',
    capacity TINYINT NOT NULL DEFAULT 4 COMMENT '정원'
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='스터디룸';

CREATE TABLE LAB07_reservations (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '예약 번호',
    member_id INT NOT NULL COMMENT '예약한 회원',
    room_id INT NOT NULL COMMENT '예약한 스터디룸',
    reserved_date DATE NOT NULL COMMENT '이용 날짜',
    start_time TIME NOT NULL COMMENT '시작 시각',
    hours TINYINT NOT NULL DEFAULT 1 COMMENT '이용 시간',
    FOREIGN KEY (member_id) REFERENCES LAB07_members(id),
    FOREIGN KEY (room_id) REFERENCES LAB07_rooms(id)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='스터디룸 예약';
```

- 확인 결과: `DESC LAB07_members;` · `DESC LAB07_rooms;` · `DESC LAB07_reservations;`

```text
+-------+-------------+------+-----+---------+----------------+
| Field | Type        | Null | Key | Default | Extra          |
+-------+-------------+------+-----+---------+----------------+
| id    | int(11)     | NO   | PRI | NULL    | auto_increment |
| name  | varchar(20) | NO   |     | NULL    |                |
| phone | varchar(20) | NO   | UNI | NULL    |                |
+-------+-------------+------+-----+---------+----------------+
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| room_name | varchar(20) | NO   |     | NULL    |                |
| capacity  | tinyint(4)  | NO   |     | 4       |                |
+-----------+-------------+------+-----+---------+----------------+
+---------------+------------+------+-----+---------+----------------+
| Field         | Type       | Null | Key | Default | Extra          |
+---------------+------------+------+-----+---------+----------------+
| id            | int(11)    | NO   | PRI | NULL    | auto_increment |
| member_id     | int(11)    | NO   | MUL | NULL    |                |
| room_id       | int(11)    | NO   | MUL | NULL    |                |
| reserved_date | date       | NO   |     | NULL    |                |
| start_time    | time       | NO   |     | NULL    |                |
| hours         | tinyint(4) | NO   |     | 1       |                |
+---------------+------------+------+-----+---------+----------------+
```

- 풀이 핵심: 부모 테이블(회원 · 스터디룸)을 먼저, 자식 테이블(예약)을 마지막에 만듦. DBML의 `ref: >` 하나가 CREATE문의 `FOREIGN KEY ... REFERENCES ...` 한 줄이 됨

### 방향 묻기 프롬프트

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 직접 쓸게.

## 상황
만들 테이블의 ERD(DBML):
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
Table LAB07_reservations {
  id int [pk, increment, note: "예약 번호"]
  member_id int [not null, note: "예약한 회원", ref: > LAB07_members.id]
  room_id int [not null, note: "예약한 스터디룸", ref: > LAB07_rooms.id]
  reserved_date date [not null, note: "이용 날짜"]
  start_time time [not null, note: "시작 시각"]
  hours tinyint [not null, default: 1, note: "이용 시간"]
}
- 그 밖의 조건: note는 COMMENT로, 문자셋 utf8mb4 · 콜레이션 utf8mb4_bin
- 내가 이해한 문제: ERD의 테이블 3개를 CREATE TABLE로 만들고, 예약 테이블이 회원 · 스터디룸 테이블을 외래키로 참조하게 함

## 질문
내 이해가 맞는지 봐 주고, 테이블을 만들 순서와 필요한 구문을 알려줘.

## 제약
- CREATE TABLE · 자료형 · 제약 조건(NOT NULL · DEFAULT · UNIQUE · PRIMARY KEY · AUTO_INCREMENT · FOREIGN KEY) · COMMENT · ALTER TABLE 범위 안에서만

## 출력 형식
| 순서 | 구문 | 하는 일 | 표로
````

### 원인 묻기 프롬프트

- 가정한 실수: ERD의 `ref`를 옮기지 않아 외래키 없이 예약 테이블이 만들어짐(에러는 나지 않음)

````md
## 맥락
SQL 데이터베이스 구축 · 관리를 배우는 중이야. 쿼리는 내가 고칠게.

## 상황
ERD대로 LAB07_members · LAB07_rooms를 만든 뒤 예약 테이블 LAB07_reservations를 만들려고 해. ERD에서 member_id는 LAB07_members.id, room_id는 LAB07_rooms.id를 ref로 가리켜.
```sql
CREATE TABLE LAB07_reservations (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '예약 번호',
    member_id INT NOT NULL COMMENT '예약한 회원',
    room_id INT NOT NULL COMMENT '예약한 스터디룸',
    reserved_date DATE NOT NULL COMMENT '이용 날짜',
    start_time TIME NOT NULL COMMENT '시작 시각',
    hours TINYINT NOT NULL DEFAULT 1 COMMENT '이용 시간'
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='스터디룸 예약';
```
- 기대한 결과: DESC에서 member_id · room_id 행의 Key 칸이 MUL
- 실제 결과: 에러 없이 만들어졌지만 DESC에서 member_id · room_id 행의 Key 칸이 비어 있음

## 질문
기대와 다른 이유를 찾게 확인할 곳을 알려줘.

## 출력 형식
| 확인할 곳 | 이유 | 표로
````

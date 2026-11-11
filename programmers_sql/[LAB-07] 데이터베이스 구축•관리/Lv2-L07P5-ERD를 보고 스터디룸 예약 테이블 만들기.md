# [Lv.2] ERD를 보고 스터디룸 예약 테이블 만들기

- 문제 번호: 직접 만든 문제
- 분류: ERD 기반 설계
- 링크: 직접 만든 문제
- 실습 DB: `USE myschool;`
- 검증: myschool에서 직접 실행해 DESC 결과 확인함

## 테이블

스터디카페의 회원 · 스터디룸 · 예약을 DBML로 그린 ERD입니다. 예약 하나는 회원 한 명과 스터디룸 하나를 가리킵니다.

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
Table LAB07_reservations {
  id int [pk, increment, note: "예약 번호"]
  member_id int [not null, note: "예약한 회원", ref: > LAB07_members.id]
  room_id int [not null, note: "예약한 스터디룸", ref: > LAB07_rooms.id]
  reserved_date date [not null, note: "이용 날짜"]
  start_time time [not null, note: "시작 시각"]
  hours tinyint [not null, default: 1, note: "이용 시간"]
}
```

| 관계 | 자식 컬럼 | 부모 컬럼 |
| --- | --- | --- |
| 회원 1 : N 예약 | LAB07_reservations.member_id | LAB07_members.id |
| 스터디룸 1 : N 예약 | LAB07_reservations.room_id | LAB07_rooms.id |

## 문제

ERD대로 `LAB07_members`, `LAB07_rooms`, `LAB07_reservations` 세 테이블을 만드는 SQL문을 작성해주세요. ERD의 `ref`는 외래키로, `note`는 COMMENT로 옮기고, 문자셋은 utf8mb4, 콜레이션은 utf8mb4_bin으로 지정해주세요. 다른 테이블을 참조하는 테이블은 참조되는 테이블보다 나중에 만들어야 합니다.

## 예시

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

`DESC LAB07_reservations;`를 실행하면 다음과 같이 출력되어야 합니다.

| Field | Type | Null | Key | Default | Extra |
| --- | --- | --- | --- | --- | --- |
| id | int(11) | NO | PRI | NULL | auto_increment |
| member_id | int(11) | NO | MUL | NULL |  |
| room_id | int(11) | NO | MUL | NULL |  |
| reserved_date | date | NO |  | NULL |  |
| start_time | time | NO |  | NULL |  |
| hours | tinyint(4) | NO |  | 1 |  |

## 정답

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

## 해설

- 부모 테이블(회원 · 스터디룸)을 먼저 만들고 자식 테이블(예약)을 마지막에 만듦
- ERD의 `ref: >` 줄마다 CREATE문에 `FOREIGN KEY ... REFERENCES ...` 한 줄을 씀
- `unique`는 `UNIQUE`, `default: 4`는 `DEFAULT 4`로 옮김

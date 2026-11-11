"""programmers_sql/programmers.sql 에서 공용 테이블 36개 부분만 뽑아 표준 출력으로 내보낸다.

사용: python3 restore_common_tables.py programmers_sql/programmers.sql | mariadb -uroot -p1234 -P9901 -h127.0.0.1 --default-character-set=utf8mb4 myschool
- 파일의 `USE programmers;` 부터 첫 문제 전용 DB(`p273709`) 앞까지가 공용 테이블이다
- 각 테이블은 DROP TABLE IF EXISTS 뒤에 다시 만들므로 여러 번 실행해도 된다
- myschool 의 기존 테이블(departments · enrollments · professors · students · subjects)과는 이름이 겹치지 않는다
"""
import sys
s=open(sys.argv[1],encoding="utf-8").read()
a=s.index("USE `programmers`;")+len("USE `programmers`;")
b=s.index("CREATE DATABASE IF NOT EXISTS `p273709`")
sys.stdout.write("SET NAMES utf8mb4;\n"+s[a:b])

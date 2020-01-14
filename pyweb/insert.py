# Mysql 패키지 import
import mysql
import mysql.connector

# DB 접속 정보
dbconfig = {'host':'localhost', 'user':'root', 'password':'', 'database':'testdb'}

# DB 연결
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()
__SQL__ = """INSERT INTO testtable VALUES ('JJ', 'Seoul')"""

# SQL문 실행
cursor.execute(__SQL__)

# 실행한 SQL문 저장 (INSERT, UDATE, DELETE)
conn.commit()

# 커서 및 접속 종료
cursor.close()
conn.close()
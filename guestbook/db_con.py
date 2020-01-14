import mysql, mysql.connector
from mysql.connector import Error, errorcode

class Db:
    dbconfig = {'host':'localhost', 'user':'root', 'password':'', 'database':'gb_d'}
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()

    #글쓰기    
    def writeContent(self, id, name, title, content):
        try:
            newContentdData = (id, name, title, content)
            __SQL__ = """INSERT INTO gb_t (u_id, name, title, content) VALUES (%s, %s, %s, %s)"""

            self.cursor.execute(__SQL__, newContentdData)
            self.conn.commit()
            print("데이터 전송 성공")

        except mysql.connector.Error as error :
            print("데이터 전송 실패 rollback : {}".format(error))
            self.conn.rollback()

    #글읽기
    def readContent(self, no):
        try:
            noData = (no, )
            __SQL__ = """SELECT * FROM gb_t WHERE no=%s"""
            
            self.cursor.execute(__SQL__, noData)
            row = self.cursor.fetchone()
            return row

        except mysql.connector.Error as error :
            print("데이터 불러오기 실패 rollback : {}".format(error))
            self.conn.rollback()

    #조회수 컨트롤러    
    def viewControl(self, no):
        try:
            noData = (no, )
            __SQL__ = """UPDATE gb_t SET view=view+1 WHERE no=%s"""
            
            self.cursor.execute(__SQL__, noData)
            self.conn.commit()
            print(no + "번 글의 조회수가 1 올라갔습니다.")

        except mysql.connector.Error as error :
            print("데이터 불러오기 실패 rollback : {}".format(error))
            self.conn.rollback()

    #목록 읽기
    def listContent(self):
        try:
            __SQL__ = """SELECT * FROM gb_t"""
            
            self.cursor.execute(__SQL__)
            listData = self.cursor.fetchall()
            return listData

        except mysql.connector.Error as error :
            print("데이터 불러오기 실패 rollback : {}".format(error))
            self.conn.rollback()

    #글검색
    def searchContent(self, searchTarget, searchData):
        try:
            search = ("%"+searchData+"%", )
            __SQL__ = "SELECT * FROM gb_t WHERE " + searchTarget + " LIKE %s"

            self.cursor.execute(__SQL__, search)
            listData = self.cursor.fetchall()
            print(listData)
            return listData

        except mysql.connector.Error as error :
            print("데이터 불러오기 실패 rollback : {}".format(error))
            self.conn.rollback()
    
    #글수정
    def updateContent(self, name, title, content, no):
        try:
            newContentdData = (name, title, content, no)
            __SQL__ = """UPDATE gb_t SET name=%s, title=%s, content=%s WHERE no=%s"""

            self.cursor.execute(__SQL__, newContentdData)
            self.conn.commit()
            print(no + "번 글이 수정되었습니다.")

        except mysql.connector.Error as error :
            print("데이터 전송 실패 rollback : {}".format(error))
            self.conn.rollback()

    #글삭제
    def deleteContent(self, no):
        try:
            noData = (no, )
            __SQL__ = """DELETE FROM gb_t WHERE no=%s"""
            
            self.cursor.execute(__SQL__, noData)
            self.conn.commit()
            print(no + "번 글이 삭제되었습니다.")

        except mysql.connector.Error as error :
            print("데이터 불러오기 실패 rollback : {}".format(error))
            self.conn.rollback()

# 로그인 DB 컨트롤러    
    def loginCheck(self, id):
        try:
            __SQL__ = """SELECT u_pw FROM gb_t WHERE u_id=%s"""
            
            self.cursor.execute(__SQL__, (id, ))
            u_pw = self.cursor.fetchone()
            if u_pw is None :
                return False
            else :
                return u_pw[0]
            
        except mysql.connector.Error as error :
            print("데이터 불러오기 실패 rollback : {}".format(error))
            self.conn.rollback()
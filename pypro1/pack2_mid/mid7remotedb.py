# 사번 , 이름을 입력하여 로그인에 성공하면 해당 직원정보를 출력함.

import pickle
import MySQLdb

with open ('mydb.dat', mode='rb' ) as obj: # DB연결 정보를 별도의 파일로 만들어서 참조하도록 함. plckie를 사용하였다.
    config = pickle.load(obj)  # 파일 실행하기
    
def jikwonProcess():
    try:
        conn = MySQLdb.connect(**config) # dict type으로 값을 받는다.
        cursor = conn.cursor()
        jikwon_no = input("직원번호 입력: ")
        jikwon_name = input("직원이름 입력: ")
        sql="""
            select jikwon_no,jikwon_name, buser_name,buser_tel,jikwon_jik
            from jikwon inner join buser on jikwon.buser_num = buser.buser_no
            where jikwon_no = {} and jikwon_name='{}'
        """.format(jikwon_no, jikwon_name)
        # jikwon_name='{}' 의 이유는 입력값이 문자열이기 때문
        
        cursor.execute(sql) # sql문 수행
        datas = cursor.fetchall() # 모든 데이터를 읽는다.
        
        if len(datas) == 0:
            print('해당정보의 직원은 없습니다.')
            return
        
        for jikwon_no,jikwon_name, buser_name,buser_tel,jikwon_jik in datas: # 해당 직원정보 출력
            print(jikwon_no,jikwon_name, buser_name,buser_tel,jikwon_jik)
        
    except Exception as e:
        print('err' ,e)
        
    finally:
        cursor.close()
        conn.close()


if __name__ =='__main__': # 메인모듈이면 해당 함수를 실행시켜라
    jikwonProcess()
    
    
    
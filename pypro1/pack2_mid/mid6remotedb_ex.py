import MySQLdb
import pickle

with open ('mydb.dat', mode='rb' ) as obj: # DB연결 정보를 별도의 파일로 만들어서 참조하도록 함. plckie를 사용하였다.
    config = pickle.load(obj)  # 파일 실행하기 

try: 
    conn = MySQLdb.connect(**config) # dict type으로 값을 받는다.
    cursor = conn.cursor() # DB와 상호작용하기 위해서 cursor를 설정한다.
    bnum = input('부서번호 입력')
    
    if bnum in ['10','20','30','40']:
        sql = "SELECT jikwon_no, jikwon_name, buser_name, jikwon_jik FROM jikwon "
        # 긴 문자열을 나누는 방법입니다.  
        sql += "INNER JOIN buser ON buser_num = buser_no where buser_num ={0}".\
        format(bnum)
        
        cursor.execute(sql)
        print('사번 이름 부서명 직급' )
    
        for data in cursor.fetchall(): # 전부 읽는다. fetchone()은 한 줄 씩 출력하는 것이다.
            # print(data)
            print('%s %s %s %s'%data)

        count = cursor.execute(sql)
        print('인원수: ', count, '명')
    else:
        print('정확한 부서 번호를 입력하세요')
        
except Exception as e:
    print('err: '+e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()
import MySQLdb
# connect가 dict type을 받는다. 소스 안에 db연결정보가 들어있는 것은 좋지 않다.

config = { 
    
    'host':'127.0.0.1',
    'user':'root',
    'password':'time@less6805',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True

}


try: 
    conn = MySQLdb.connect(**config) # ** dict , * tuple
    cursor = conn.cursor()
    
    buser_num = input('부서번호를 입력하세요: ' )
    sql = "select jikwon_no, jikwon_name, buser_name, jikwon_jik from jikwon "
    sql += "inner join buser on buser_num = buser_no where buser_num=%s"
    cursor.execute(sql,(buser_num,)) # 입력 받은 변수를 넣어준다.
    print('사번 이름 부서명 직급')
    count= 0
    for data in cursor.fetchall():
        count +=1
        print('%s,%s, %s, %s'%data)
       
    print(count)
                
except Exception as e:
    print('err : ', e)
    conn.rollback()
    
finally:
    cursor.close()
    conn.close()

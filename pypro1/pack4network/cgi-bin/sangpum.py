# 상품자료 출력
import MySQLdb
import pickle

with open('cgi-bin/mydb.dat','rb') as obj:
    config = pickle.load(obj)
print("Content-Type:text/html;charset=utf-8\n")  

print("<html><body>") # 여기서의 print는 값을 서버로 전송하는 것이다.
print("<table border='1'>")
print("<tr><th>코드</th><th>품명</th><th>수량</th><th>단가</th></tr>")
try:
       conn = MySQLdb.connect(**config) # dict type으로 값을 받는다.
       cursor = conn.cursor()
       sql = "select * from sangdata"
       cursor.execute(sql) # sql문 실행함.
       datas = cursor.fetchall() # 전체 행을 읽는다.
       # fetchone() 한줄 한줄 읽는다.
       # fetchall() 전체 나열 함수
       # 레코드를 배열형식으로 저장해 주는 일을 합니다.
       for code,sang,su,dan in datas: # 해당 직원정보 출력
            print('''
             <tr>
                 <td>{0}</td>
                 <td>{1}</td>
                 <td>{2}</td>
                 <td>{3}</td>
             </tr>   
            '''.format(code,sang,su,dan))
    
except Exception as e:
    print('err :', e)
    
finally:
    cursor.close()
    conn.close()
    
print("</body></html>")
    
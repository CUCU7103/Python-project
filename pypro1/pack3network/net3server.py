# client / server 간 통신 연습
# try catch문을 사용한다.
import socket
import sys

# echo server : 클라이언트 요청에 반응하는 서버 - 서비스를 유지함.

HOST = '' # 본인의 아이피
PORT = 7878

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket(소캣의 종류, 소캣유형)
# serversock = socket(AF_INET, SOCK_STREAM)  from socket import * 이 아니기에 직접 위와 같이 지정해 주어야한다.
try:
    serversock.bind((HOST,PORT)) # 
    serversock.listen(5) # 동시 접속자수
    print('server service...')
    
    while True:
        conn, addr = serversock.accept() # 클라이언트의 접속 대기 
        print('client info ', addr[0],addr[1] ) # 클라이언트의 ip, port 출력한다.
        
        # 수신 (클라이언트의 메세지)
        print(conn.recv(1024).decode()) # 수신 데이터 암호화 된 자료 해제 후 출력
        
        # 송신
        conn.send(('from server :' + str(addr[1])+ '너도 잘지내라' ).encode('utf_8'))
        
except socket.error as err:
    print('socket err ', err )
    sys.exit()
    
except Exception as e:
    print('err: ', e)

finally:
    serversock.close()
    conn.close()
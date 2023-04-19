# client / server 간 통신 연습(1회용)
# 연습시 cmd 혹은 아나콘다 cmd 사용하기
# echo server : 클라이언트 요청에 반응하는 서버 
from socket import * 

# tcp 기반의 socket 객체 생성
serversock = socket(AF_INET, SOCK_STREAM) # socket(소캣의 종류, 소캣유형) 소캣 생성
serversock.bind(('127.0.0.1',8888)) # bind는 tuple type으로 값을 주어야 한다. 생성한 소캣에 ip address와 포트번호 부여
serversock.listen(1) # 1~5 까지 부여가 가능하며 동시 접속자 수를 의미한다. 
                     # Tcp Listener 지정함.
print('server start....')

conn,addr = serversock.accept() # 연결 대기 (클라이언트의 접속때까지 , 계속 기다린다.)
                                # 연결에 성공하면 클라이언트의 소캣과 클라이언트의 주소를 받는다

print('client addr : ' , addr)
print('from client message : ', conn.recv(1024).decode()) # 클라이언트 서버로 부터 받은 메세지를 출력함, 
                                                          # 기본적으로 바이트 type로 넘어오고 인코딩하여 오기에 디코딩으로 풀어줘야함.
conn.close() # 메세지 받은 다음에 연결을 종료한다.
serversock.close() # 연결끊기
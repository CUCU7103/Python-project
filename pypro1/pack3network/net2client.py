# client side : socket 객체를 생성한다.
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM) # 소캣 모듈에 들어있는 정보들.... 소캣 객체 생성
                                          # socket(소캣의 종류, 소캣유형)

clientsock.connect(('127.0.0.1',8888))  # 능동적으로 서버에 접속함.
clientsock.send('Hi server'.encode(encoding = 'UTF-8',errors='strict')) # 메시지 전달, errors='strict'은 생략이 가능하다.

# data는 'sequence binary data'로 전송이 된다. packet(Header+Body)단위
clientsock.close() # 연결 끊기



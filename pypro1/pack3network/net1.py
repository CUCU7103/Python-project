# 컴퓨터 간 통신 
# 소켓(Socket,tcp프로토콜을 지원한다.)이란 네트워크상에서 동작하는 프로그램 간 통신의 종착점(Endpoint)입니다. => 통신 채널이다.
# 즉, 프로그램이 네트워크에서 데이터를 통신할 수 있도록 연결해주는 연결부라고 할 수 있습니다.
# 채팅이나 게임 등 클라이언트와 서버 간 양방향 통신이 필요한 프로그램에 사용되고 있습니다

import socket

print(socket.getservbyname('http','tcp')) # 80 port 사용 / https = 443
print(socket.getservbyname('ftp', 'tcp')) # 21 port 사용 /
print(socket.getservbyname('telnet','tcp')) # 23 port 사용
print(socket.getservbyname('smtp','tcp')) # 25 / 
print(socket.getservbyname('pop3','tcp')) # 110

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
# [(<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.195.200', 80)), (<AddressFamily.AF_INET: 2>, 0, 6, '', ('223.130.200.107', 80))]
# http://223.130.195.200/index.html => URL




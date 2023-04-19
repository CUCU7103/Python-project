# Simple HTTPServer 구성하기
from http.server import SimpleHTTPRequestHandler, HTTPServer

# CGIHTTPRequestHandler :  이 클래스는 서버에서 CGI 스크립트로 실행해야 하는 파일의 요청을 처리합니다.

# HTTPServer :이 클래스는 들어오는 요청을 수신하고 적절한 핸들러로 요청을 전달하는 HTTP 서버를 만드는 데 사용
# 클래스는 서버의 주소 (호스트 이름 또는 IP 주소)와 포트 번호를 담은 
# 튜플과 요청 처리에 사용할 핸들러 클래스 두 가지 인수를 취합니다

port = 7777 # 포트 번호를 담음

handler = SimpleHTTPRequestHandler

serv = HTTPServer(('192.168.0.8',port),handler) 

print('웹 서비스 시작')
# 기본적으로 서버가 실행되어지면 index.html을 찾아간다. 이때 index.html은 논리적인 요청명이다.
serv.serve_forever() # 서버를 지속적으로 실행함. = 서버의 유지

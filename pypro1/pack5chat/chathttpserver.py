# 웹 서버 : CGI 
# Common Gateway Interface(CGI) 
# 서버와 애플리케이션 간에 데이터를 주고 받는 방식 또는 컨벤션을 CGI라고 한다
# 대화형 웹페이지를 만들수 있다.

from http.server import CGIHTTPRequestHandler, HTTPServer # 웹 서버를 생성하기 위함.

# CGIHTTPRequestHandler :  이 클래스는 서버에서 CGI 스크립트로 실행해야 하는 파일의 요청을 처리합니다.

# HTTPServer :이 클래스는 들어오는 요청을 수신하고 적절한 핸들러로 요청을 전달하는 HTTP 서버를 만드는 데 사용
# 클래스는 서버의 주소 (호스트 이름 또는 IP 주소)와 포트 번호를 담은 
# 튜플과 요청 처리에 사용할 핸들러 클래스 두 가지 인수를 취합니다

port = 7989 # 포트번호를 지정한다.

class Handler(CGIHTTPRequestHandler): # 서블릿과 유사하다.
    cgi_directiries=['/cgi-bin']    # 서버와 연결할 파일의 경로를 적어줘야한다
                                   
     
serv = HTTPServer(('192.168.0.8',port),Handler)
print('챗봇 웹 서비스 시작....')
serv.serve_forever()

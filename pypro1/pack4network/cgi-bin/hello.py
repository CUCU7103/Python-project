# 웹용 스크립트
str = "파이썬 작업도중 발생한 값"
print("Content-Type:text/html;charset=utf-8\n") # 마인 타입

print("<html><body>") # 여기서의 print는 값을 서버로 전송하는 것이다.

print("<b>와우 파이썬</b> 문서로 웹처리를 하다니")
print("<br>변수 값 : %s"%(str,))
print("</body></html>")
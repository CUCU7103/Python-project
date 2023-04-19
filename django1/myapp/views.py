from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def indexFunc(request):
    return HttpResponse("장고 만세")
# 서버실행시 에러면 setting 확인

def helloFunc(request): # 자바의 httprequest...
    msg = "파이썬 변수"
    ss = "<html><body>장고 프로젝트 %s</body></html>"%msg # html 적용하기
    return HttpResponse(ss)

def worldFunc(request): 
    msg = "홍길동" # 타임리프랑 유사하다.
    msg2 = "23"
    return render(request,"show.html",{'name':msg, 'age':msg2}) 
    # forwording 이 기본방식이다.
    # 클라이언트의 요청을 서버가 다른 서버로 직접 전달한다. 
    # 즉 url의 변경이 없다.
                                       # http://127.0.0.1/world.... 
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

def MainFunc(request): # 클라이언트의 정보를 request가 가지고 있다.
    return render(request,'index.html') # 렌더링한다는 것 : 서버로 html를 푸쉬한다.    
                                        # 즉 forward 방식이다.
                                        
class CallView(TemplateView): # Class-based views를 사용하기 위해서 TemplateView를 사용해야함.
    template_name = 'callget.html'
    
def insertFunc(request):
    if request.method == 'GET':
        print('GET 요청 처리')
        # print(request.GET.get('name')) # 태그의 name을 통해서 값을 받아온다. 아래와 기능은 동일하다.
        # print(request.GET['name']) 
        return render(request,'insert.html')
    
    
    elif request.method == 'POST':
        print('POST 요청 처리')  
        irum = request.POST.get('name')
        return render(request,"list.html",{"irum" : irum +"님"})
        
    else:
        print('요청오류')
        
def selectFunc(request):
    return render(request,'callget.html')
    
def upFunc(request):
    return render(request,'callget.html')
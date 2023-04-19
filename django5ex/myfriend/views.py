from django.shortcuts import render
from myfriend.models import Article

# Create your views here.
def showFunc(request): 
    return render(request,'main.html')

def showlist(request):
    datas = Article.objects.all() # ORM 사용
    return render(request,'list.html',{'articles': datas}) # key value 형식으로다가....
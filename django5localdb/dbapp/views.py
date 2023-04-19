from django.shortcuts import render
from dbapp.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def Datashow(request):
    datas = Article.objects.all() 
    # ORM(객체와 데이터베이스의 관계를 매핑해주는 도구)으로 select문이 수행된 것이다. 
    # sql문 대신에 객체를 사용하는 것.
    # all() : 테이블 자료를 모두 가져오기 위해서는 XXXXX.objects.all() 과 같이 all()을 사용한다.
    print(datas)
    # 담겨져 있는 테이블 정보확인함. 
    # <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>
    print(datas[0].name)
    return render(request,'list.html', {'articles': datas})
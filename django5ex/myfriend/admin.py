from django.contrib import admin
from myfriend.models import Article # import가 어플리케이션을 제대로 지정하였는지 확인할 필요가 있다.


# Register your models here.
class ArticleAdmin(admin.ModelAdmin): 
    # 관리자 페이지에서 테이블을 보기 위함.
    list_display = ('id','irum','juso','nai')
    
admin.site.register(Article, ArticleAdmin) 

from django.contrib import admin
from dbapp.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin): 
    # 관리자 페이지에서 테이블을 보기 위함.
    list_display = ('id','code','name','price','pub_date')
    
admin.site.register(Article, ArticleAdmin)

from django.db import models

# Create your models here.
class Article(models.Model):
    
    irum = models.CharField(max_length=20)
    juso = models.CharField(max_length=20)
    nai = models.IntegerField() 
    # 작업 후 migrate 및  make migration 실행하기
from django.db import models

# Create your models here.
class Article(models.Model):
    # modles.Model 이라는 클래스를 상속 받아서 사용할 것이다.
     title = models.CharField(max_length=100)   
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)  
     updated_at = models.DateTimeField(auto_now=True)   
    # comment_set =
    # django가 자동으로 위 코드를 추가해준다.


class Comment(models.Model):
     content = models.TextField()
     article = models.ForeignKey(Article, on_delete=models.CASCADE) # 부모가 지워졌을때, 자식이 같이 지워진다.
     # 1:N 관계에서 1은 Article, N은 Comment이다.
     
     # article_id =
     # django 가 자동으로 article_id 를 저장하고, 이 컬럼은 Article의 id를 참조한다.
     
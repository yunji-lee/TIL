from django.db import models
from django.conf import settings
# settings.AUTH_USER_MODEL

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 첫번째 인자는 클래스


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  #  괄호안의 Article은 위 class의 Article
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

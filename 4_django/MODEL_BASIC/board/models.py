from django.db import models
# 모델에는 클래스를 저장


class Article(models.Model):   # model 이라는 클래스에 Model 이라는 번역가를 같이 상속받은 클래스를 만들겠다.
    # id = Primary Key
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.title} - {self.content}'

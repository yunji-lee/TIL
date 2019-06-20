from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
from django.conf import settings


class HashTag(models.Model):
    content = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.content


class Post(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(blank=True)  # makemigrations 하면 사진없어서 2 번으로나오고 blank로 일단 설정
    image = ProcessedImageField(
        upload_to='posts/images',            # 올리는 위치 설정
        processors=[ResizeToFill(600, 600)],  #
        format='JPEG',                        #
        options={'quality': 90}               # 원본대비 품질 설정
    )
    hashtags = models.ManyToManyField(HashTag, blank=True)


class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #여기Post는 Post모델



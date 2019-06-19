from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class User(AbstractUser):
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="follower")  # settiong의 맨 아래에 선언한 user
    introduce = models.TextField(blank=True)
    image = ProcessedImageField(
        upload_to='accounts/images',  # 올리는 위치 설정
        processors=[ResizeToFill(150, 150)],  #
        format='JPEG',  #
        options={'quality': 90},  # 원본대비 품질 설정
        blank=True,
    )


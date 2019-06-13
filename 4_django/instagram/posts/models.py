from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models


class Post(models.Model):
    content = models.TextField()
    # image = models.ImageField(blank=True)  # makemigrations 하면 사진없어서 2 번으로나오고 blank로 일단 설정
    image = ProcessedImageField(
        upload_to='posts/images',            # 올리는 위치 설정
        processors=[ResizeToFill(600, 600)],  #
        format='JPEG',                        #
        options={'quality': 90}               # 원본대비 품질 설정
    )

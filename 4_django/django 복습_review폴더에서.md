# django 복습

## 1. 시작하기

```sh
# 폴더생성
student@M9029 MINGW64 ~/TIL/4_django (master)
$ django-admin startproject review

student@M9029 MINGW64 ~/TIL/4_django/review (master)
$ django-admin startapp articles
```

## 2. settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles' # 추가하기
]
```

## 3. models.py

```python
from django.db import models

# Create your models here.


class Article(models.Model): #models는 위에 import한 것, .Model은 정의된 Model을 사용하겠다는 말.
    title = models.CharField(max_length=100)
    content = models.TextField()
```

## 4. urls.py

## 5. templates 폴더 생성

## 		5-1. article폴더에 url에 따른 html생성

### 				1) base.html  생성

## 6. 실행코드

```sh
student@M9029 MINGW64 ~/TIL/4_django/review (master)
$ python manage.py runserver
```


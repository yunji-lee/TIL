# bootstrap

## 부트스트랩
<https://getbootstrap.com/docs/4.3/components/buttons/>





## REST
https://nesoy.github.io/articles/2017-02/REST

하나의 url로 두가지 동작을 하는 것을 RESTful하다고 말한다.

즉, 1) new+create 두가지로 나뉘어져있던 url을 하나의 url로 합치고 2)POST방식이냐 GET방식이냐에 따라 두가지 동작을 하게 하는 것을 말한다.

왜 하나로 합쳤는가? 

- 원자성을 가진다. 
- endpoint를 줄이고자
- 같은 url을 가지고 메소드만 다르게 해서 다른 action을 할 수 있도록 하는것(아래 사진 참조)
- ![img](https://gmlwjd9405.github.io/images/network/rest.png)
- ![img](https://gmlwjd9405.github.io/images/network/restapi-example.png)



## 관계설정

(게시물과 댓글 사이에 관계설정)

모델 2개 설정 FK(foreign key), CASCADE를 사용할 때 on_delete옵션은 써야함

```python
#  /TIL/4_django/board의 models.py에서 보면
## class Comment를 참고하자
article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

```sh
student@M9029 MINGW64 ~/TIL/4_django/board (master)
$ python manage.py makemigrations
$ python manage.py migrate

# migration작업이란 입력한 작업을 DB에 저장하기위해 변환해주는 작업 ? 맞나?
```

1(article) : N(comment)관계에서 접근하는 방식을 보면

1) 1 -> N 참조시 코드: N_set

2) N -> 1 참조시 코드: .1

---

댓글 삭제버튼 생성및 삭제하는 프로세스 만들기, 아래 코드는 detail.html에서 가져옴

```sh
<div class="alert alert-primary" role="alert">
  {{ comment.content }}
    <a class="btn btn-outline-danger" href="{% url 'articles:comment_delete' article.id comment.id %}">삭제</a> 
</div>
## 여기서 가져갈 내용
# 1. url에서 'articles:comment_delete'중 articles는 폴더이름 comment_delete는 정의한 함수 이름
# 2. article.id 와 comment.id 둘다 적어야 하는 것이 포인트
```


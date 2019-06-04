# Django.db / DB만들기

## 설치

``` sh
pip install django_extensions ipython ipython[notebook]
```

## SQLite 설치

1. C:\Program Files\DB Browser for SQLite 에서

2. DB Browser for SQLite.exe 실행

3. 데이터 베이스 실행 클릭
4. C:\Users\student\TIL\4_django\MODEL_BASIC 에서
5. db.sqlite3 클릭
6. board_article 우클릭 -> 데이터보기
7. 테이블 생성이 잘 된걸 확인하면 끝

## Python 과 SQL

python 세상에서 코드를 통해 SQL을 만나는것이지 직접만나지 않음.

``` sh
$ python manage.py shell # 파이썬 안의 장고세상으로 진입
```

``` python
In [1]: from board.models import Article

In [2]: article = Article()

In [3]: print(article.id)
None

In [5]: article.title
Out[5]: ''

In [6]: article.content
Out[6]: ''

In [7]: article.title = 'Hi!'

In [8]: article.title
Out[8]: 'Hi!'

In [9]: article.content = 'Hello World!'

In [11]: article.content
Out[11]: 'Hello World!'
    
In [12]: article.save()

In [13]: article
Out[13]: <Article: Article object (1)>

In [14]: article.title = 'Bye'

In [16]: article.content = 'Good Bye, World'

In [17]: article.save() # 사실 이전에 기록한거 위에 덮어씌우는 작업

In [18]: article
Out[18]: <Article: Article object (1)>

In [19]: article2 = Article() # 두번째 레코드 생성

In [21]: article2.title = 'Happy'

In [22]: article2.content = 'Hacking'

In [23]: article2.save() # 두번째 라인 저장, sqlite에서 새로고침하면 볼 수 있음

In [24]: article2
Out[24]: <Article: Article object (2)>

```

## 의문

1. 일일이 import 해야하는가?

   ``` python
   python manage.py shell_plus # 이 코드로 해결
   python manage.py shell_plus --notebook #
   ```

   

2. 데이터는 sql에 저장된다해도, 날아가는 코드들은 어떻게 하나

   ``` python
   Article.objects.all()
   Article.objects.get(id=1)
   # 근데 이걸로 해결하는건지는 모르겠음 ㅋㅋ
   ```

---

# CRUD Basic / DB 

## CRUD Operation
* Create => 데이터 생성
* Read (Retrieve) => 데이터 조회
* Update => 데이터 수정
* Delete => 데이터 삭제

## Articles Table - schema

=> 데이터의 스키마가 어떻게 되는가? 위의 테이블이라 설명할 수 있다.

| Field Name | Data Type                 |
| ---------- | ------------------------- |
| `id`       | Integer, PK               |
| `title`    | CharField(max_length=200) |
| `content`  | TextField()               |

---

## board_article_test_codes 실행

``` sh
student@M9029 MINGW64 ~/TIL/4_django/MODEL_BASIC (master) # 파일경로 지정 잘 확인하기
$ python manage.py shell_plus --notebook
```

Article이라는 것이 잘 설정되어있다면 어디서 실행하던지 돌아가는것이 핵심!

notebook환경에서 확인하는 이유는 바로 결과 값을 볼 수 있기 때문

파이참은 보통 코드를 작성하는 이유로 많이 사용. 

노트북은 결과값보기위해 사용한 것으로 이후에 사용할 일은 잘 없음

---


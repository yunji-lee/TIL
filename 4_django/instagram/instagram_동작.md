1. create.html

   1) form 태그안에 method="post"추가

   2)     {% csrf_token %} 추가

```html
{% extends 'posts/base.html' %}

{% block body %}
<h1>글 작성</h1>
<form action="" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
</form>
{% endblock %}
```



2. veiw.py

   1) def create 안의 if문 수정

   2) import에서 render뒤에 redirect추가

```python
from django.shortcuts import render, redirect
from .forms import PostForm


def index(request):
    return render(request, 'posts/index.html')


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.save()
        return redirect("posts:index")
    else:
        form = PostForm()
        context = {
            'form':form
        }
        return render(request, 'posts/create.html', context)
```



3. admin.py 수정

```python
from django.contrib import admin
from .models import Post


admin.site.register(Post)
```



4. user생성

```sh
student@M9029 MINGW64 ~/TIL/4_django/instagram (master)
$ python manage.py createsuperuser
```



5. veiw.py

   1) def create: 에서  if문 안에 if문 생성

   2) 실행 흐름(번호순) 잘 이해하기!

```python
from django.shortcuts import render, redirect
from .forms import PostForm


def index(request):
    return render(request, 'posts/index.html')


def create(request):
    # create 가 실행되는 조건
    #  1. get 방식으로 데이터를 입력할 수 있는 form 을 요청한다.
    #  4. 사용자가 데이터를 입력해서 post 요청을 보낸다.
    #  9. 사용자가 적절한 데이터를 입력해서 post 요청을 보낸다.
    if request.method == "POST":
        # 5. (post 방식으로 저장요청을 받고) 데이터를 받아서 PostForm 을 인스턴스화 한다.
        # 10. 데이터를 받아서 PostForm 을 인스턴스화 한다.
        form = PostForm(request.POST)
        # 6. 데이터 검증을 한다.
        # 11. 데이터 검증을 한다.
        if form. is_valid():   # vaild 하면 저장
            # 12. 적절한 데이터가 들어온다. 저장을 하고 인덱스로 보낸다.
            form.save()
            return redirect("posts:index")
        else:                  # vaild 안하면 반환
            # 7. is_vaild 가 False 인 경우, 즉 적절하지 않은 데이터가 들어옴.
            pass
    else:
        # 2. PostForm 을 인스턴스화 해서 form 변수에 저장
        form = PostForm()

    context = {
        'form':form  # 여기에 있는 form 이 무엇인지 잘 이해하기
    }
    # 3. 만들어진 form 을 create.html 에 담아서 전송
    # 8. 사용자가 정확하게 입력한 데이터를 유지한 상태의 form 을 전송
    return render(request, 'posts/create.html', context)

    #  form = PostForm()에서 
    # request가 있는 PostForm과 없는 PostForm의 차이는
    # request가 있는 PostForm은 기존에 사용자가 적었던 것이 form에 있다는 것
```

??? models.py가 있는데 forms.py를 만들어서 쓰는 이유는? 
		==>	정리의 문제

models: DB모델들을 관리, 데이터베이스에 어떻게 정의하겠다

forms: 폼들을 관리, 포스트가 바뀌면 알아서 폼도 바꿔준다 /  field=all



6. view.py

   1) def index 수정

   2) import 수정

   ```python
   from django.shortcuts import render, redirect
   from .forms import PostForm
   from .models import Post
   
   
   def index(request):
       posts = Post.objects.all()
       context = {
           'posts':posts
       }
       return render(request, 'posts/index.html', context)
   ```



7. index.html 수정

```sh
{% extends 'posts/base.html' %}

{% block body %}
<h1>인덱스 페이지</h1>
{% for post in posts %}
    {% include 'posts/_post.html' %}
{% endfor %}
{% endblock %}
```



8. _post.html 생성

   ​	1) 부트스트랩 Components에서 card

   ​	2) https://picsum.photos/여기서 img의 src='인자값' 가져오기

   ​	3) 부트스트랩 Layout에서 Grid

```html
<div class="card">
  <img src="https://picsum.photos/id/{{post.id}}/300/300" class="card-img-top" alt="...">
  <div class="card-body">
<!--    <h5 class="card-title">Card title</h5>-->
    <p class="card-text">{{post.content}}</p>
<!--    <a href="#" class="btn btn-primary">Go somewhere</a>-->
  </div>
</div>
```



9. index 수정

```html
{% extends 'posts/base.html' %}

{% block body %}
{% for post in posts %}
    <div class="row">
    {% include 'posts/_post.html' %}
    </div>
{% endfor %}
{% endblock %}
```



10. _post.html 수정

    1) div class 값 수정

```html
<div class="card col-md-6 my-3">
  <img src="https://picsum.photos/id/{{post.id}}/300/300" class="card-img-top" alt="...">
  <div class="card-body">
<!--    <h5 class="card-title">Card title</h5>-->
    <p class="card-text">{{post.content}}</p>
<!--    <a href="#" class="btn btn-primary">Go somewhere</a>-->
  </div>
</div>
```



11. base.html수정

    1) navbar에서 url설정

    ```html
     <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <a class="navbar-brand" href="{% url 'posts:index %}">
              <i class="fab fa-instagram"></i> | Instagram
          </a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
              <a class="nav-item nav-link active" href="{% url 'posts:create' %}"> NEW <span class="sr-only">(current)</span></a>
              <a class="nav-item nav-link" href="#">My page</a>
            </div>
          </div>
        </nav>
    ```

    

12. django bootstrap 4 설치

    1) pip install django-bootstrap4

    2) setting.py에  'bootstrap4' 추가

    ==> 13번에서 bootstrap_form을 사용하기 위해서(bootstrap홈페이지의 gird form)

13. create.html

    ```html
    {% extends 'posts/base.html' %}
    {% load bootstrap4 %}
    {% block body %}
    <h1>글 작성</h1>
    <!--form과 input태그 항상 해야하는 작업.-->
    <form action="" method="post">
        {% csrf_token %}
        {% bootstrap_form form %}
        <input type="submit">
    </form>
    {% endblock %}
    ```

    

14. urls.py, update부분 수정

    ```python
        # Update - 포스트 수정하기
        path('<int:post_id>/update/', views.update, name="update"),
    ```



15. view.py 

    1) update부분 수정

    2)def create부분 하단 수정

    ```python
    def update(request, post_id):
        #포스트 방식으로 들어올 떄 : 사용자가 입력한 데이터 가져와서 기존 데이터 수정하기
        #겟방식으로 들어올 때 : 기존의 정보 담아서 수정페이지 보여주기
        if request.method == 'POST':
            pass
        else:
            post = Post.objects.get(id=post_id)
            form = PostForm(instance=post)
        return render(request, 'posts/form.html', {'form':form}) # create의 context부분과 동일한 점을 인지하자
    ```

    ```python
        return render(request, 'posts/form.html', context)
    	# 후에 create.html을 form.html로 수정
    ```

    3) update부분 마저 수정하기

    ```python
    def update(request, post_id):
        #포스트 방식으로 들어올 떄 : 사용자가 입력한 데이터 가져와서 기존 데이터 수정하기
        #겟방식으로 들어올 때 : 기존의 정보 담아서 수정페이지 보여주기
        post = Post.objects.get(id=post_id)
        if request.method == 'POST':
            # form = PostForm(request.POST) # 새로만드는것
            form = PostForm(request.POST, instance=post)  # 기존의 instance(사용자)는 post야
            #PostForm(data=request.POST, instance=post)에서 data=은 생략됨
            if form.is_valid():
                form.save()
                return redirect("posts:index")
            else:
                pass
        else:
            form = PostForm(instance=post)
        return render(request, 'posts/form.html', {'form':form}) # create의 context부분과 동일한 점을 인지하자
    ```

    ?? is_valid 폼에 맞는 값을 넣었는지, false라면 save안되게 설정하는 것

15. _post.html

    1) 버튼달기

    ```html
    <div class="card col-md-6 my-3">
      <img src="https://picsum.photos/id/{{post.id}}/300/300" class="card-img-top" alt="...">
      <div class="card-body">
    <!--    <h5 class="card-title">Card title</h5>-->
        <p class="card-text">{{post.content}}</p>
    <!--    <a href="#" class="btn btn-primary">Go somewhere</a>-->
          <a class="btn btn-warning" href="{% url 'posts:update' post.id %}">수정</a>
      </div>
    </div>
    ```

----

(6/13)

17. models.py

1) post class수정

```python
class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(blank=True)  # makemigrations 하면 사진없어서 2 번으로나오고 blank로 일단 설정
```



18. forms.html

1) form태그안에 enctype 추가

```html
{% extends 'posts/base.html' %}
{% load bootstrap4 %}
{% block body %}
<!--form과 input태그 항상 해야하는 작업.-->
<form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {% bootstrap_form form %}
    <input type="submit">
</form>
{% endblock %}
```



19. views.py

1) def create 수정, 10. 번아래 request.FILES 추가

```python
def create(request):
    # create 가 실행되는 조건
    #  1. get 방식으로 데이터를 입력할 수 있는 form 을 요청한다.
    #  4. 사용자가 데이터를 입력해서 post 요청을 보낸다.
    #  9. 사용자가 적절한 데이터를 입력해서 post 요청을 보낸다.
    if request.method == "POST":
        # 5. (post 방식으로 저장요청을 받고) 데이터를 받아서 PostForm 을 인스턴스화 한다.
        # 10. 데이터를 받아서 PostForm 을 인스턴스화 한다.
        form = PostForm(request.POST, request.FILES)
        # 6. 데이터 검증을 한다.
        # 11. 데이터 검증을 한다.
        if form. is_valid():   # vaild 하면 저장
            # 12. 적절한 데이터가 들어온다. 저장을 하고 인덱스로 보낸다.
            form.save()
            return redirect("posts:index")
        else:                  # vaild 안하면 반환
            # 7. is_vaild 가 False 인 경우, 즉 적절하지 않은 데이터가 들어옴.
            pass
    else:
        # 2. PostForm 을 인스턴스화 해서 form 변수에 저장
        form = PostForm()

    context = {
        'form':form  # 여기에 있는 form 이 무엇인지 잘 이해하기
    }
    # 3. 만들어진 form 을 create.html 에 담아서 전송
    # 8. 사용자가 정확하게 입력한 데이터를 유지한 상태의 form 을 전송
    return render(request, 'posts/form.html', context)
```

 ==> 이상태로 새로 게시물 작성하면 사진은 Instagram 프로젝트파일(루트파일)에 저장됨. 이는 효과적이지 않음.



20. settings.py

    1) 파일 맨 아래에 추가

    ```python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    # 동일 파일 내 있는 BASE_DIR을 참조한다는 것,  주소설정을 한다는 것
    ```

    2) 이후에 서버에서 게시물 하나 더 생성하면, media라는 폴더가 생기고 그 안에 사진이 저장됨

    

21. instagram 폴더안(최상단)의 urls.py

    1)  기존 코드 아래에 추가

    ```python
    from django.conf.urls.static import static
    from django.conf import settings # settings.AUTH_USER_MODEL 쓸 때 불러왔던 것
    
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #urlpatterns += static('/media/')로 사용해도 되지만 변수화하여 사용하는게 좋으므로 위의 코드를 사용
    ```

    

22. views.py

    1) 최신순으로 바꾸기, def index를 수정 

    ​		: posts = 의 맨뒷부분

    ```python
    def index(request):
        posts = Post.objects.all().order_by('-id')
        context = {
            'posts':posts
        }
        return render(request, 'posts/index.html', context)
    ```



23. 이미지 수정에는 두개의 라이브러리가 추가적으로 필요 (image resizing)

    <https://github.com/matthewwithanm/django-imagekit>  #imagekit관련 공식문서

    1) pip install pilkit

    ​    pip install django-imagekit

    2) 이후에 setting.py의 INSTALL_APPS에 'imagekit'추가

    ​    => 최종사용이 imagekit이고 이 imagekit이 pikit에 붙어있어서? imagekit만 추가하면됨

    3) models.py

    ```python
    from imagekit.models import ProcessedImageField #추가
    from imagekit.processors import ResizeToFill 	#추가
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
    ```

    ​	4) 이후 python manage.py makemigrations와 python manage.py migrate 실행

    ​	==> 새 게시물을 작성하여 사진의 resizeing을 확인해보기

    

    24. 새로운 앱 추가

        1) 터미널에 django-admin startapp accounts

        2) setting.py INSTALLED_APP에 'accounts' 추가

        3) 루트 urls.py에 path('accounts/', include('accounts.urls')) 추가

        4) account폴더 안에 urls.py 생성 및 내용 추가

        ```python
        from django.urls import path
        from . import views
        
        app_name = 'accounts'
        
        urlpatterns = [
            path('signup/', views.signup, name='signup'),  # 회원가입
            path('login/', views.login, name='login'),
            path('logout/', views.logout, name='logout')
        ]
        ```

        4) view.py

        ```python
        from django.shortcuts import render, redirect
        from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
        from django.contrib.auth import login as auth_login
        from django.contrib.auth import logout as auth_logout
        
        
        
        def signup(request):
            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('posts:index')
            else:
                form = UserCreationForm()
                # 인스턴스화 시킨다는 것은?  UserCreationForm자체는 이름을 정의, ()를 붙여 모델의 정의하여 인스턴스화 한것(=생성을 한 것이라고 말해도 되나?)을 form이라는 이름으로 저장?
            return render(request, 'accounts/signup.html', {'form':form}) # 왜 signup으로? usercreationform은 유저생성만을 위한 폼이니까. form으로 한 것은 postform에서는 create와 update 두가지 기능이 있었으니까!
        
        
        def login(request):
            if request.method == "POST":
                form = AuthenticationForm(request, request.POST)  #AuthenticationForm은 인자로 request를 추가로 넣어준다.
                if form.is_valid():
                    auth_login(request, form.get_user())
                    return redirect('posts:index')
            else:
                form = AuthenticationForm()  # 인증
            return render(request, 'accounts/login.html', {'form':form})
        
        
        def logout(request):
            auth_logout(request)
            return redirect('posts:index')
        ```

        5) instagram>accounts>templates(폴더생성)>accounts(폴더생성)>signup.html(생성) 후 작성

        ```html
        {% extends 'posts/base.html' %}
        {%load bootstrap4%}
        
        {% block body %}
            <form action="" method="post">
                <!-- csrf_token은 post메소드를 사용하기 위함        -->
                {% csrf_token %}
                {% bootstrap_form form %}
                <input class="btn btn-primary" type="submit" value="회원가입">
            </form>
        {% endblock %}
        ```

        6) instagram>accounts>templates>accounts>signup.html(생성) 후 작성

        ```html
        {% extends 'posts/base.html' %}
        {%load bootstrap4%}
        
        {% block body %}
            <form action="" method="post">
                <!-- csrf_token은 post메소드를 사용하기 위함        -->
                {% csrf_token %}
                {% bootstrap_form form %}
                <input class="btn btn-primary" type="submit" value="로그인">
            </form>
        {% endblock %}
        ```



25. base.html 수정

    instagram>posts>templates>posts>base.html 에서 navbar 수정

    ```html
      <div class="navbar-nav">
                <a class="nav-item nav-link active" href="{% url 'posts:create' %}">
                    NEW<span class="sr-only">(current)</span>
          		</a>
                {% if user.is_authenticated %}
                    <a class="nav-item nav-link" href="{% url 'accounts:logout' %}">LogOut</a>
                {% else %}
                    <a class="nav-item nav-link" href="{% url 'accounts:signup' %}">SignUp</a>
                    <a class="nav-item nav-link" href="{% url 'accounts:login' %}">LogIn</a>
                {% endif %}
            </div>
    ```

    
    
    
    
    ----
    
    6/17
    
    
    
    * posts앱의 models.py 수정
    
      1) class Post안에 user생성 및 연결
    
      ```python
      from django.conf import settings
      
      class Post()
      	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        # user = models.ForeignKey(어떤 모델과 연결할지, 어떻게 처리할지)
      ```
    
      2) python manage.py makemigrations -> 1(Enter) -> 1(Enter)
    
      ​    python manage.py migrate
    
    ​      => 여기서 서버를 실행해보면 user를 선택할 수 있게되어있는데, user를 선택할 수 있게하면 안되고 자동으로 로그인된 user로 되게끔 해야함. 이게이어서 수정할 내용임



- posts앱의 form.py 수정

  1) field 수정

  ```python
  class PostForm(forms.ModelForm):
      class Meta:
          model = Post
          # fields = '__all__'
          fields = ['content', 'image' ] # 어떤내용 보여줄지 설정하는 것
  ```

  

- view.py

  1) def create 수정

  ```python
          if form. is_valid():   # vaild 하면 저장
              # 12. 적절한 데이터가 들어온다. 저장을 하고 인덱스로 보낸다.
              ### 아래의 3줄이 수정한 부분
             post = form.save(commit=False)  
             # DB에 반영되기전 압축하는 것. 'commit=False' = DB에 넣지는 마
             # 왜냐하면 유저정보 안넣었으니까, 아래 라인이 유저정보 넣는거야!
             post.user = request.user        
             post.save()                     # 이제 컬럼 다 채웠으니까 저장해!!
              return redirect("posts:index")
          else:                  # vaild 안하면 반환
              # 7. is_vaild 가 False 인 경우, 즉 적절하지 않은 데이터가 들어옴.
              pass
  ```

  => 이상태로 실행하면 로그아웃하고 게시물작성 하면 오류가 뜸. 이걸 또 수정하겠죠?

  

  2) import 하나 하고 def create() 윗 줄에 한 줄 삽입

  ```python
  from django.contrib.auth.decorators import login_required
  
  @login_required
  def create(request):
      
      
  # update()와 delete에도 윗줄에 써주기
  ```

  => 로그인 안하면 못쓰게 설정.  logout하고 new하면 뜨는 url

  => logout하고 new하면 뜨는 url : <http://127.0.0.1:8000/accounts/login/?next=/posts/create/>

  ​    : 로그인하면  next이후의 url로 옮겨다 줄게 라는 말이지만

  ​    : 막상 수정하고 실행하면 게시물작성페이지가 아니라 index페이지로 이동함 ㅋㅋ

  



- _posts

- 1) 게시물에 username나오게 하기

  ```html
  <p class="card-text"><strong>{{post.user.username}}</strong>{{post.content}}</p>
  ```



- base.html

  ```html
  <a href="">{{user}}님 반갑습니다.</a> 
  # 
  ```

  

- 내가 작성하지 않은 것 수정, 삭제 못하게

  1) views.py 

  : def update() 수정

  ```python
  def update(request, post_id):
      post = Post.objects.get(id=post_id) 
      # Post의 user(글을 보는 사람)와 request의 유저(=작성하는 사람)의 차이
      if request.user == post.user:
          # 내가 작성한 글일 떄
          if request.method == 'POST':
              # form = PostForm(request.POST) # 새로만드는것
              form = PostForm(request.POST, instance=post)  # 기존의 instance(사용자)는 post야
              #PostForm(data=request.POST, instance=post)에서 data=은 생략됨
              if form.is_valid():
                  form.save()
                  return redirect("posts:index")
              else:
                  pass
          else:
              form = PostForm(instance=post)
          return render(request, 'posts/form.html', {'form':form}) # create의 context부분과 동일한 점을 인지하자
      else:
          # 내가 작성하지 않은 글일 때
          return redirect("posts:index")
  ```

  2) _posts.html 수정

  : 수정, 삭제 버튼있는 a 태그를 if 문으로 감싸기

  ```python
  {% if post.user == user %}
  <a class="btn btn-warning" href="{% url 'posts:update' post.id %}">수정</a>
  <a class="btn btn-warning" href="{% url 'posts:delete' post.id %}">삭제</a>
  {% endif %}
  ```



- 댓글기능 추가하기

  1) posts 앱에서 models.py

  ```python
  class Comment(models.Model):
      content = models.TextField()
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      post = models.ForeignKey(Post, on_delete=models.CASCADE) #여기Post는 Post모델
  ```

  => python manage.py makemigrations 

  ​    python manage.py migrate

  2) admin.py

  ```python
  from django.contrib import admin
  from .models import Post, Comment
  
  
  admin.site.register(Post)
  admin.site.register(Comment)
  ```

  3)urls.py에 추가

  ```python
   # Comment_create
      path('<int:post_id>/comments/create', views.comment_create, name="comment_create"),
  ```

  4) views.py

  ```python
  from .forms import PostForm, CommentForm
  from .models import Post, Comment
  
  def index(request):
      posts = Post.objects.all().order_by('-id')
      comment_form = CommentForm()
      context = {
          'posts':posts
          'comment_form':comment_form
      }
      return render(request, 'posts/index.html', context)
  
  
  
  @login_required
  def comment_create(request, post_id):
      post = Post.objects.get(id=post_id)
      if request.method == "POST":  
  # 원래는 url을 하나만 쓰려고 if문으로 처리, 여기서는 get방식 안쓸거라 else문 필요없다.
          comment_form = CommentForm(request.POST)
          if comment_form.is_valid():
              comment = comment_form.save(commit=False)
              comment.user = request.user  # 지금 로그인한 사람
              comment.post = post  # 바로 위에서 정의한 post
            # comment.post_id = post_id  
      # 윗줄 대신 이것도 가능, 둘의 차이점은 post 객체 자체를 가져오느냐 post의 숫자(id)를 가져오느냐
              comment.save()
              return redirect("posts:index")
  ```

  5) forms.py

  ```python
  from .models import Comment
  
  class CommentForm(forms.ModelForm):
      class Meta:
          model = Comment
          fields = ['content']
  ```

  6) _posts.html

  : 맨 상단에 {% load bootstrap4 %}추가

  : 댓글 출력, 댓글 폼 추가

  ```html
      {% if post.image %}
        <img src="{{ post.image.url }}" class="card-img-top" alt="...">
      {% else %}
        <img src="https://picsum.photos/id/{{post.id}}/300/300" class="card-img-top" alt="...">
      {% endif %}
      <div class="card-body">
    <!--    <h5 class="card-title">Card title</h5>-->
        <p class="card-text"><strong>{{post.user.username}}</strong>{{post.content}}</p>
          <!--    <a href="#" class="btn btn-primary">Go somewhere</a>-->
          {% if post.user == user %}
          <a class="btn btn-warning" href="{% url 'posts:update' post.id %}">수정</a>
          <a class="btn btn-warning" href="{% url 'posts:delete' post.id %}">삭제</a>
          {% endif %}
      </div>
      <!--  댓글 출력 시작   -->
      <div class="card-body">
          {% for comment in post.comment_set.all%}
              <p><strong>{{ comment.user.username }}</strong>{{ comment.content }}</p>
          {% empty %}
              <p>댓글이 없습니다.</p>
          {% endfor %}
      </div>
      <!--  댓글 출력 끝  -->
      <!--  댓글 폼 시작  -->
      <div class="card-body">
          <form action="{% url 'posts:comment_create' post.id %}" method="post">
              {% csrf_token %}
              {% bootstrap_form comment_form %}
              <input type="submit">
          </form>
      </div>
      <!--  댓글 폼 끝  -->
  </div>
  ```

  

- content 칸 줄이기

  1) models.py

  : class Comment(): 에서 content의 TextField를 CharField로

  ```python
  class Comment(models.Model):
      content = models.CharField(max_length=100)
      user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      post = models.ForeignKey(Post, on_delete=models.CASCADE) #여기Post는 Post모델
  ```

   : python manage.py makemigrations 

   : python manage.py migrate

  2) _posts.html

  : 댓글 폼 변경

  ```html
              {% csrf_token %}
              {# bootstrap_form comment_form #}
              {% bootstrap_field comment_form.content show_label=False %}
  ```

  

- 회원가입 변경(회원가입 후 로그인실행)

  1) accounts의 views.py

  : def signup() 부분

  :is_valid()부분 수정

  ```python
  		 if form.is_valid():
              user = form.save()
              auth_login(request, user)
              return redirect('posts:index')
  ```

  

- 좋아요기능, N:N설정

  ![N대N_관계](C:\Users\student\Desktop\N대N_관계.jpg)

  1) models.py

  : class Post()에 like_users 추가

  ```python
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
  ```

   : python manage.py makemigrations 

   : python manage.py migrate

  2) urls.py

  :path 추가

  ```python
  # Like
      path('<int:posts_id>/likes', views.likes, name="likes"),
  ```

  3) posts\view.py

  : def likes 추가

  ```python
  def likes(request, post_id):
      user = request.user
      post = Post.objects.get(id=post_id)
  
      # 이미 좋아요가 눌러졌으면
      if user in post.like_users.all(): #지금 로그인한 사람이 post.like_users에 속해있나? 즉 좋아요 눌렀는가에 대한 것
          # 좋아요 취소
          post.like_users.remove(user)
      # 좋아요 안했으면
      else:
          # 좋아요 추가
          post.like_users.add(user)
      return redirect("posts:index")
  ```

  4) _posts.html

  ```html
      <div class="card-body">
    <!--    <h5 class="card-title">Card title</h5>-->
          <p>{{ post.like_users.count }}명이 좋아합니다.</p>
          <p class="card-text"><strong>{{post.user.username}}</strong>{{post.content}}</p>
          <!--    <a href="#" class="btn btn-primary">Go somewhere</a>-->
          {% if user in post.like_users.all %}
          <a href="{% url 'posts:likes' post.id %}"><i class="fas fa-heart"></i></a>
          {% else %}
          <a href="{% url 'posts:likes' post.id %}"><i class="far fa-heart"></i></a>
          {% endif %}
          {% if post.user == user %}
          <a class="btn btn-warning" href="{% url 'posts:update' post.id %}">수정</a>
          <a class="btn btn-warning" href="{% url 'posts:delete' post.id %}">삭제</a>
          {% endif %}
      </div>
  ```



- 추가 작업, 로그인이랑 회원가입

  1) accounts\views.py

  ```python
  def signup(request):
      if request.user.is_authenticated:
          return redirect("posts:index")
  
  def login(request):
      if request.user.is_authenticated:
          return redirect("posts:index")
  ```

  
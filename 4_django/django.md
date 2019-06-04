1. 장고설치
```sh
student@M9029 MINGW64 ~/TIL (master)
$ pip install django==2.1.8
```
2. 장고 디렉토리 생성
(TIL에 4_django 디렉토리 생성 후 4_django안에서 아래 코드 실행)
```sh
student@M9029 MINGW64 ~/TIL/4_django (master)
$ django-admin startproject first_django
```
장고는 앱들이 모여있는 프로젝트다.
위의 코드를 입력했을 때 생기는 가장 상위의 디렉토리를 project라고 부른다

그 하위 디렉토리들은 앱이라고 부르고, 자동생성된 동일이름의 앱(first_django)을 master app이라고 부른다.

---

# Django

## what

: 프레임워크 사용은 카페 창업시 프렌차이즈를 사용하는 것과 유사

: 즉, 기본적인 구조나 필요한 코드를 제공

## why

: hotframeworks.com (web framework)

* full-stack frame work

## How

: 요청과 응답

: static은 요청시 있으면 주고 없으면 말고

: Django의 경우 'M'(model데이터관리) 'T'(template사용자가 보는 화면) 'V'(view중간(혹은 총괄)관리<u>자</u>, 매니저)

: Django도 M V C 모델 뷰 컨트롤러로 패턴으로 되어 있지만, 유니크한 M V T 로 표현하고자 함

---

함수 정의 시 첫번째 인자로 무조건 request, 시작과 끝 무조건 request

views.py에서 보면 아래와 같다.
request란 요청에대한 모든것이 담겨있다

```python
from django.shortcuts import HttpResponse

def index(request):
    #print(request)
    #print(request.META)
    
    return render(request, 'index.html')

```
위의 코드를 실행해서 보면 request에 대한 정보를 볼 수 있다.
print 구문은 확인 후 지워도 됨.

---

```html
                   ,--,        ,---,        .--. ,--.'|    
                   ,'_ /|    ,-+-. /  |     .--,`| |  |,     
      .--,    .--. |  | :   ,--.'|'   |     |  |.  `--'_     
    /_ ./|  ,'_ /| :  . |  |   |  ,"' |     '--`_  ,' ,'|    
 , ' , ' :  |  ' | |  . .  |   | /  | |     ,--,'| '  | |    
/___/ \: |  |  | ' |  | |  |   | |  | |     |  | ' |  | :    
 .  \  ' |  :  | : ;  ; |  |   | |  |/      :  | | '  : |__  
  \  ;   :  '  :  `--'   \ |   | |--'     __|  : ' |  | '.'| 
   \  \  ;  :  ,      .-./ |   |/       .'__/\_: | ;  :    ; 
    :  \  \  `--`----'     '---'        |   :    : |  ,   /  
     \  ' ;                              \   \  /   ---`-'   
      `--`                                `--`-'             
```

---


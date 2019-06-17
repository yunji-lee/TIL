from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def signup(request):
    if request.user.is_authenticated:
        return redirect("posts:index")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = UserCreationForm()
        # 인스턴스화 시킨다는 것은?  UserCreationForm자체는 이름을 정의, ()를 붙여 모델의 정의하여 인스턴스화 한것(=생성을 한 것이라고 말해도 되나?)을 form이라는 이름으로 저장?
    return render(request, 'accounts/signup.html', {'form':form}) # 왜 signup으로? usercreationform은 유저생성만을 위한 폼이니까. form으로 한 것은 postform에서는 create와 update 두가지 기능이 있었으니까!


def login(request):
    if request.user.is_authenticated:
        return redirect("posts:index")
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
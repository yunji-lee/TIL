from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .models import User


def signup(request):
    if request.user.is_authenticated:
        return redirect("posts:index")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
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


def user_page(request, user_id):
    user_info = User.objects.get(id=user_id)
    context = {
        'user_info': user_info
    }
    return render(request, 'accounts/user_page.html', context)


def follow(request, user_id):
    me = request.user
    you = User.objects.get(id=user_id)
    # 자기 자신을 팔로우 할 수 없도록
    if me != you:
        # 나 중심
        # if you in me.follow.all() : # 팔로우 했으면
        #     me.follow.remove(you) # 팔로우 취소
        # else : # 팔로우 안했으면
        #     me.follow.add(you) # 팔로우 추가

        # 너 중심
        if me in you.follower.all():
            you.follower.remove(me)
        else:
            you.follower.add(me)
    else :
        pass
    return redirect('accounts:user_page', you.id)
    #   return redirect(f"/posts/#post_{post.id}")
    # return redirect('accounts:user_page', user_id)

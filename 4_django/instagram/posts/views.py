from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment, HashTag
from django.contrib.auth.decorators import login_required
from itertools import chain
from django.http import JsonResponse


@login_required
def index(request):
    user_follow = request.user.follow.all()  # user in user.follow.all() 와 같은 말
    follow_list = chain(user_follow, [request.user])
    posts = Post.objects.order_by('-id').filter(user__in=follow_list)
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'posts/index.html', context)


def all(request):
    posts = Post.objects.all().order_by('-id')
    comment_form = CommentForm()
    context = {
        'posts':posts,
        'comment_form':comment_form,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    # create 가 실행되는 조건
    #  1. get 방식으로 데이터를 입력할 수 있는 form 을 요청한다.
    #  4. 사용자가 데이터를 입력해서 post 요청을 보낸다.
    #  9. 사용자가 적절한 데이터를 입력해서 post 요청을 보낸다.
    if request.method == "POST":
        # 5. (post 방식으로 저장요청을 받고) 데이터를 받아서 PostForm 을 인스턴스화 한다.
        # 10. 데이터를 받아서 PostForm 을 인스턴스화 한다.
        form = PostForm(request.POST, request.FILES)  # content, image, 여기에는 user에 대한 정보가 빠져있음
        # 6. 데이터 검증을 한다.
        # 11. 데이터 검증을 한다.
        if form. is_valid():   # vaild 하면 저장
            # 12. 적절한 데이터가 들어온다. 저장을 하고 인덱스로 보낸다.
            post = form.save(commit=False)  # DB에 반영되기전 압축하는 것. 'commit=False' = DB에 넣지는 마
            post.user = request.user        # 왜냐하면 유저정보 안넣었으니까, 이 라인이 유저정보 넣는거야!
            post.save()                     # 이제 컬럼 다 채웠으니까 저장해!!

            # 해시태그 추가
            # post.content = request.POST.get('content')  # 방법 1
            content = form.cleaned_data.get('content')            # 방법 2 : 깨끗하게 처리 된 데이터.
            words = content.split()
            for word in words:
                if word[0] == "#":
                    # 해시태그 생성
                    hashtag = HashTag.objects.get_or_create(content=word)  # 두가지 일 한번에 처리?
                    # 해시태그와 post 모델을 연결
                    post.hashtags.add(hashtag[0])  # 리턴값이 튜플이라서
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

    #  form = PostForm()에서
    # request가 있는 PostForm과 없는 PostForm의 차이는
    # request가 있는 PostForm은 기존에 사용자가 적었던 것이 form에 있다는 것


@login_required
def update(request, post_id):
    post = Post.objects.get(id=post_id) # Post의 user(글을 보는 사람)와 request의 user(=작성하는 사람)의 차이
    if request.user == post.user:
        # 내가 작성한 글일 떄
        if request.method == 'POST':
            # form = PostForm(request.POST) # 새로만드는것
            form = PostForm(request.POST, instance=post)  # 기존의 instance(사용자)는 post야
            # PostForm(data=request.POST, instance=post)에서 data=은 생략됨
            if form.is_valid():
                form.save()

                # 기존의 M:N관계를 삭제
                post.hashtags.clear()
                # 해시태그 추가
                # post.content = request.POST.get('content')  # 방법 1
                content = form.cleaned_data.get('content')  # 방법 2 : 깨끗하게 처리 된 데이터.
                words = content.split()
                for word in words:
                    if word[0] == "#":
                        # 해시태그 생성
                        hashtag = HashTag.objects.get_or_create(content=word)  # 두가지 일 한번에 처리?
                        # 해시태그와 post 모델을 연결
                        post.hashtags.add(hashtag[0])

                return redirect("posts:index")
            else:
                pass
        else:
            form = PostForm(instance=post)
        return render(request, 'posts/form.html', {'form':form}) # create의 context부분과 동일한 점을 인지하자
    else:
        # 내가 작성하지 않은 글일 때
        return redirect("posts:index")
    # 포스트 방식으로 들어올 떄 : 사용자가 입력한 데이터 가져와서 기존 데이터 수정하기
    # 겟방식으로 들어올 때 : 기존의 정보 담아서 수정페이지 보여주기


@login_required
def comment_create(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":  # 원래는 url을 하나만 쓰려고 if문으로 처리, 여기서는 index,,? 어쩌고 여기서는 get방식 안쓸거라 else문 필요없당
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user  # 지금 로그인한 사람
            comment.post = post  # 바로 위에서 정의한 post
            # comment.post_id = post_id  # 윗줄 대신 이것도 가능, 둘의 차이점은 post 객체 자체를 가져오느냐 post의 숫자(id)를 가져오느냐
            comment.save()
            return redirect("posts:index")


@login_required
def likes(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    # 이미 좋아요가 눌러졌으면
    if user in post.like_users.all():  # 지금 로그인한 사람이 post.like_users에 속해있나? 즉 좋아요 눌렀는가에 대한 것
        # 좋아요 취소
        post.like_users.remove(user)
        is_like = False
    # 좋아요 안했으면
    else:
        # 좋아요 추가
        post.like_users.add(user)
        is_like = True
    # return redirect(f"/posts/#post_{post.id}")
    like_count = post.like_users.count()
    context = {
        'is_like': is_like,
        'like_count': like_count
    }
    return JsonResponse(context)


def hashtags(request, hashtag_id):
    hashtag = HashTag.objects.get(id=hashtag_id)
    posts = hashtag.post_set.all()  # 여기에 추가된 것외에는 all함수와 동일함

    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
        'hashtag': hashtag,
    }
    return render(request, 'posts/index.html', context)


def javascript(request):
    return render(request, 'posts/js.html')


@login_required
def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("posts:index")
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts':posts
    }
    return render(request, 'posts/index.html', context)


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

    #  form = PostForm()에서
    # request가 있는 PostForm과 없는 PostForm의 차이는
    # request가 있는 PostForm은 기존에 사용자가 적었던 것이 form에 있다는 것


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


def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect("posts:index")

from django.shortcuts import render,redirect
from .models import Article, Comment
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)


def create(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.user = request.user
        article.save()
        return redirect('articles:detail', article.id)
    else:
        return render(request, 'articles/form.html')


def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('articles:index')


def update(request, article_id):
    if request.method == "POST":
        article = Article.objects.get(id=article_id)
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.id)
    else:
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'articles/form.html', context)


def comment_create(request, article_id):
    comment = Comment()  # 비어있는 인스턴스, 즉 비어있는 객체 생성
    article = Article.objects.get(id=article_id)
    comment.content = request.POST.get('content')  # get()의 인자는 detail.py의 name 과 일치시킨다
    comment.article = article
    comment.user = request.user
    comment.save()
    return redirect("articles:detail", article_id)

def comment_delete(request, article_id, comment_id):
    # 각페이지에 있는 article에 달린 댓글 중 하나를 가져온다
    comment = Comment.objects.get(id=comment_id)  # article_set에서 하나만 가져오기
    comment.delete()
    return redirect('articles:detail', article_id)


def comment_all(request):
    return render(request, 'articles/comment_all.html')
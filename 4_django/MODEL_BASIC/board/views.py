from django.shortcuts import render, redirect
from .models import Article

# Create your views here.


def index(request):
    return render(request, 'board/index.html', {})


# Form HTML
def new_article(request):
    return render(request, 'board/new_article.html')


# Save new Article
def create_article(request):
    article = Article()

    article.title = request.POST.get('title')   # 메서드 GET 요청에서 'title'을 get하겠다.
    article.content = request.POST.get('content')

    article.save()
    return redirect(f'/board/{article.id}/')

#  Read all
def article_list(request):  # 전체 article 조회하기
    articles = Article.objects.all()   # []
    return render(request, 'board/article_list.html', {
        'articles': articles,
    })
# (Article.objects)매니저님 모두 가져와서 articles라 저장하고
# article_list.html을 렌더해서 articles를 실어보낼게요


#  Read one
def article_detail(request, article_id):  # 특정 article 조회하기
    article = Article.objects.get(id=article_id)
    return  render(request, 'board/article_detail.html', {
        'article': article,
    })

#  Update
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'board/edit_article.html', {
        'article': article
    })


def update_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')

    article.save()
    return redirect(f'/board/{article.id}/')



#  Delete
def delete_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('/board/')

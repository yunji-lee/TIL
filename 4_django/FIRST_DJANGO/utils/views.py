from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'utils/index.html')


def artii(request, keyword):
    import art
    result = art.text2art(keyword, 'random')
    # 1번 유형
    # return render(request, 'utils/HTML.html', {'result': result})
    # 2번 유형
    context = {
        'result': result,
        'keyword': keyword,
    }
    return render(request, 'utils/artii.html', context)

def stock(request):
    pass  # TODO : 완성하기


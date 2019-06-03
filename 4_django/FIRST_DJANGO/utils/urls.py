from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # utils/
    path('art/<str:keyword>/', views.artii), # utils/art.<KEYWORD> / 패턴상으로 좋음?
    path('stock/', views.stock), # utils/stock/
]

from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # Main page
    path('', views.index, name='index'),
    # Restaurant page
    path('restaurant/', views.detail, name='detail'),

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)  # ''이말은 url/board/ 가 default 라는 말
]

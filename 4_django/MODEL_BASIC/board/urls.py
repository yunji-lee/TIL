from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),  # ''이말은 url/board/ 가 default 라는 말
    # Create
    path('new/', views.new_article),
    path('create/', views.create_article),# board/create/

    # Read
    path('', views.article_list),  # /board/
    path('<int:article_id>/', views.article_detail),  # /board/<int:article_id>/

    # Update
    path('<int:article_id>/edit/', views.edit_article),  # /board/<int:article_id>/edit
    path('<int:article_id>/update/', views.update_article),  # /board/<int:article_id>/update

    # Delete
    path('<int:article_id>/delete/', views.delete_article), # /board/delete
]

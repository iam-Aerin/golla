from django.urls import path
from . import views

app_name = 'golla_app'

urlpatterns = [
    path('', views.index, name='index'),                        # /questions/
    path('create/', views.create, name='create'),               # /questions/create/
    path('<int:id>/', views.detail, name='detail'),             # /questions/1/
    path('random/', views.random_article, name='random'),       # /questions/random/
    path('comments/<int:answer_id>/edit/', views.edit_answer, name='edit_answer'),  # 댓글 수정
]

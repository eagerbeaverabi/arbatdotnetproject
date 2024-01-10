from django.urls import path
from . import views

app_name = 'blogger'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('<str:username>/home/', views.home, name='home'),
    path('<str:username>/profile/', views.profile, name='profile'),
    path('<str:username>/articles/', views.articles, name='articles'),
    path('<str:username>/bloggers/', views.bloggers, name='bloggers'),
    path('<str:username>/bloggers/<int:author>/', views.bloggers, name='bloggers'),
    path('<str:username>/workspace/', views.workspace, name='workspace'),
    path('<str:username>/<int:article_id>/workspace/', views.workspace, name='workspace'),
    path('<str:username>/<int:article_id>/<int:delete>/workspace/', views.workspace, name='workspace'),
]
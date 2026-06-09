# pages/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),       
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/create/', views.todo_create, name='todo_create'),
    path('todos/edit/<int:todo_id>/', views.todo_edit, name='todo_edit'),
    path('todos/complete/<int:todo_id>/', views.todo_complete, name='todo_complete'),



]
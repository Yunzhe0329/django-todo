from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('toggle/<int:todo_id>/', views.toggle_complete, name='toggle_complete'),

    # 登入系統
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
     path('accounts/login/', auth_views.LoginView.as_view(template_name='todo/login.html')),
]



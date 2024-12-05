from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user/', views.user_page, name='user_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('adicionar_treino/', views.adicionar_treino, name='adicionar_treino'),
]

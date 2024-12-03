from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('user/', views.user_page, name='user_page'),
    # ... other URL patterns ...
]

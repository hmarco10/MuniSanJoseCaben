from django.urls import path
from user import views


app_name = 'user'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
]
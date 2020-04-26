from django.urls import path
from apps.users.views import UserRegister, UserDetailUpdate

app_name = 'users'
urlpatterns = [
    path('', UserRegister.as_view()),
    path('update/<int:pk>/', UserDetailUpdate.as_view()),
]

from django.urls import path
from accounts.views import RegisterApi,LoginApi,LogoutApi,HomeApi

urlpatterns = [
    path('register/',RegisterApi.as_view()),
    path('login/',LoginApi.as_view()),
    path('logout/',LogoutApi.as_view()),
    path('home/',HomeApi.as_view())
]

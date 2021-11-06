from django.urls import path
from .views import RegisterAPI, LoginAPI
from knox.views import LogoutView

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='register'),
]
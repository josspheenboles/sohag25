from django.urls import path
from .views import Regview
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('Login/',LoginView.as_view(
        template_name='myuser/login.html'
    ),name='Login'),
    path('Logout/',LogoutView.as_view(),name='Logout'),
    path('Reg/',Regview,name='Reg'),
]
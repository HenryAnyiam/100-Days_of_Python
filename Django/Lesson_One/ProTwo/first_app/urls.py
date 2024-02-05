from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('users', views.users, name='users')
]
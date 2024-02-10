from django.urls import path
from . import views

app_name = 'base_app'

urlpatterns = [
    path('', views.index, name='home'),
    path('signup', views.sign_up, name='sign_up')
]
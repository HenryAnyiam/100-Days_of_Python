from . import views
from django.urls import path

urlpatterns = [
    path("display", views.display, name="display"),
    path("<str:name>", views.index, name="index")  
]

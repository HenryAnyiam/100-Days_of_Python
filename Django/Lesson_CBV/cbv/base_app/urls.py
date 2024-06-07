from django.urls import path
from base_app import views

app_name ='base_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('new', views.IndexTemplateView.as_view(), name='new_home'),
    path('school', views.SchoolListView.as_view(), name="schools"),
    path('school/<int:pk>', views.SchoolDetailsView.as_view(), name="school"),
    path('json_school', views.school, name="json_school"),
    path('create', views.SchoolCreateView.as_view(), name='create'),
]
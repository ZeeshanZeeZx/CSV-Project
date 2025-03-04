from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_csv, name='upload_csv'),
    path('csv_list/', views.csv_list, name='csv_list'),
]
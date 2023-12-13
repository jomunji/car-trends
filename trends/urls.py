from django.urls import path
from trends import views

urlpatterns = [
    path("trends/", views.trends, name='trends')
]
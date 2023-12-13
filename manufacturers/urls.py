from django.urls import path
from manufacturers import views

urlpatterns = [
    path("manufacturers/", views.manufacturers, name='manufacturers')
]
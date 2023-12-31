from django.urls import path
from trends import views

urlpatterns = [
    path("trends/", views.trends, name='trends'),
    path("trends_plots/<str:col_input>/", views.trends_plots, name="trends_plots"),
]
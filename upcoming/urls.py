from django.urls import path
from . import views

urlpatterns = [
    path('', views.upcoming, name='upcoming'),
    path('addpost/', views.add_post, name="add_post"),
]

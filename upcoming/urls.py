from django.urls import path
from . import views

urlpatterns = [
    path("", views.upcoming, name="upcoming"),
    path("addpost/", views.add_post, name="add_post"),
    path("deletepost/<int:post_id>/", views.delete_post, name="delete_post"),
    path("editpost/<int:post_id>/", views.edit_post, name="edit_post"),
]

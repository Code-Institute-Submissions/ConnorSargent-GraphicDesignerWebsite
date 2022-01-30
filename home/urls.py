from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("addreview/", views.add_review, name="add_review"),
    path(
        "deletereview/<int:review_id>/",
        views.delete_review,
        name="delete_review",
    ),
    path("editreview/<int:review_id>/", views.edit_review, name="edit_review"),
]

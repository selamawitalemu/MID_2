from django.urls import path
from . import views

urlpatterns = [
    path("list-create", views.ListCreateAPI.as_view()),
    path("list-delete/<int:pk>",views.Dl.as_view()),
]
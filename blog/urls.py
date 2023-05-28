from .import views
from django.urls import path

urlpatterns = [
    path("blog",views.blog1, name='blog'),
]
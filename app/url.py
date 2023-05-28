from .import views
from django.urls import path



urlpatterns = [
    path("homeapp/",views.homeapp, name='homeapp'),
]
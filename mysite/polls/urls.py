from django.urls import path
from . import views


# Home page
urlpatterns = [
    path('', views.index, name='index'),
]


from django.urls import path
from . import views  # Import views from the core app

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
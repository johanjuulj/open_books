from django.urls import path
from . import views  # Import views from the core app

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("about/", views.AboutView.as_view(), name="about"),
    path("roadmap/", views.RoadMapView.as_view(), name="roadmap"),
    path("vision/", views.VisionView.as_view(), name="vision"),
]



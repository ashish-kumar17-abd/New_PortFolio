from django.urls import path
from .views import home, about, projects, project_detail, contact_view

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('projects/', projects, name="projects"),
    path('projects/<int:pk>/', project_detail, name='project_detail'),
    path('contact/', contact_view, name="contact"),
]

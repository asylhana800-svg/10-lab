from django.contrib import admin
from django.urls import path
from main import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),                        
    path('about/', views.about),                 
    path('projects/<int:project_id>/', views.project_detail), 
    path('info/', views.info),                   
]
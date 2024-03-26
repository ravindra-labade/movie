from django.urls import path
from .views import add_movie, show_movie, update_movie, delete_movie

urlpatterns = [
    path('add/', add_movie, name='add_url'),
    path('show/', show_movie, name='show_url'),
    path('update/<int:pk>/', update_movie, name='update_url'),
    path('delete/<int:pk>/', delete_movie, name='delete_url'),
]
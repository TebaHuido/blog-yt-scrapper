from django.urls import path
from  . import views
urlpatterns = [
path('', views.posts),
path('videos/', views.videos),
]

from django.shortcuts import render

# Create your views here.
from .models import Post, Videos
def posts(request):
    posts=Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})
def videos(request):
    videos=Videos.objects.all()
    return render(request, 'muestraVideos.html', {'videos':videos})

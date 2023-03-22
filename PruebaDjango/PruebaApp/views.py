from scrapChannelYT import scrapChannel
from django.shortcuts import render
from .models import Videos as v
# Create your views here.
from .models import Post, Videos
def posts(request):
    posts=Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})
def videos(request):
    videos=Videos.objects.all()
    return render(request, 'muestraVideos.html', {'videos':videos})
def vidsync(request):
    for video in scrapChannel("ibai_",27):
        x = v(titulo=video.title, idvideo=video.id)
        x.save()
    videos=Videos.objects.all()
    return render(request, 'muestraVideos.html', {'videos':videos})
import django
import os
import scrapChannelYT
from scrapChannelYT import scrapChannel
from models import Videos as v
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PruebaDjango.settings')


for video in scrapChannel("ibai_",27):
    x = v(titulo=video.title, idvideo=video.id)
    x.save()



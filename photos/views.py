from django.shortcuts import render_to_response
from .models import Photo
# Create your views here.
def showphotos(request):
    photos = Photo.objects.all()
    return render_to_response('photo.html',locals())
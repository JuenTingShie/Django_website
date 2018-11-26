from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

from gallery.models import Gallery
from Django_website.forms import GalleryForm

def ShowGallery(request):
    images = Gallery.objects.all().order_by('-upload_time')
    return render(request,'Gallery.html',locals())
    

@login_required
def GalleryView(request):
    if request.method == 'POST':
        uploader = Gallery(uploader = request.user )
        form = GalleryForm(request.POST ,request.FILES ,instance = uploader)
        if form.is_valid():
            form.save()
        return redirect('/gallery')
    else:
        form = GalleryForm()
    return render(request,'gallery/upload.html',locals())


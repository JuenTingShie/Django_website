from django.urls import path

from gallery.views import ShowGallery,GalleryView

urlpatterns = [
    path('gallery/', ShowGallery),
    path('dashboard/edit_gallery/',GalleryView)
]
from django.urls import path

from blog.views import ShowIndex,ShowPost,EditPost

urlpatterns = [
    path('', ShowIndex),
    path('post/<slug:slug>',ShowPost),
    path('dashboard/edit/',EditPost),
]

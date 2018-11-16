from django.urls import path

from blog.views import ShowIndex,ShowPost

urlpatterns = [
    path('', ShowIndex),
    path('post/<slug:slug>',ShowPost),
]

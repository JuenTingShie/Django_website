from django.urls import path

from blog.views import ShowIndex,ShowPost,EditPost,NewPost

urlpatterns = [
    path('', ShowIndex),
    path('post/<slug:slug>',ShowPost),
    path('post/edit_/<int:id>/',EditPost),
    path('dashboard/new_post/',NewPost),
]

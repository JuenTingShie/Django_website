from django.contrib import admin
from .models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','publish_time')
admin.site.register(Post,PostAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','poster','post_time')
    ordering = ('-post_time',)
admin.site.register(Comment,CommentAdmin)
from django.contrib import admin
from django.db.models.functions import Length

from blog.models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','publish_time','edited_time','author')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','poster','post_time')
    list_filter = ('post',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
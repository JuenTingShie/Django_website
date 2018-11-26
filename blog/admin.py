from django.contrib import admin

from blog.models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','publish_time','edited_time','author',)
    fields = ('title','image','context')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','poster','post_time')
    list_filter = ('post',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
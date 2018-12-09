from django.contrib import admin

from simple_history.admin import SimpleHistoryAdmin

from blog.models import Post,Comment

class PostHistoryAdmin(SimpleHistoryAdmin):
    list_display = ['title','publish_time','edited_time','author',]
    fields = ['title','image','context']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','poster','post_time')
    list_filter = ('post',)



admin.site.register(Post,PostHistoryAdmin)
admin.site.register(Comment,SimpleHistoryAdmin)

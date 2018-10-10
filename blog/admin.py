from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','publish_time')
admin.site.register(Post,PostAdmin)
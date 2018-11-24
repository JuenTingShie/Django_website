from django.db import models
from django.db.models.signals import pre_save

from uuslug import slugify
### Post block ###
class Post(models.Model):
    author = models.CharField('作者',max_length = 200 ,editable = False )
    title = models.CharField('標題' ,max_length = 200 )
    slug = models.SlugField('網址' ,unique = True ,editable = False )
    context = models.TextField('文章內容' )
    publish_time = models.DateTimeField('發布時間' ,auto_now_add = True )
    edited_time = models.DateTimeField('修改時間' ,auto_now = True )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def rename(instance,filename):
        ext = filename.split('.')[-1]
        return '{0}/{1}.{2}'.format('post/side',instance.slug,ext)

    image = models.ImageField('側邊圖片',upload_to=rename,blank=True )

def create_slug(instance):
    slug = slugify(instance.title)
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug='{0}{1}'.format(slug,qs.first().id)
        return new_slug
    return slug
  
def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
### Comment block ###
class Comment(models.Model):
    post = models.ForeignKey('Post' ,related_name='comments' ,on_delete=models.CASCADE )
    poster = models.CharField('留言的人' ,max_length = 30 ,default = '陌生人' )
    context = models.TextField('留言內容' ,max_length = 140 ,blank = False)
    post_time = models.DateTimeField('留言時間' ,auto_now_add=True )

    def __str__(self):
        return self.post
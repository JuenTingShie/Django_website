from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from uuslug import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField('標題',max_length=200)
    slug = models.SlugField('網址',unique=True,editable=False)
    image = models.URLField('首頁圖片',max_length=200,blank=True)
    context = models.TextField('文章內容')
    publish_time = models.DateTimeField('發布時間',default=timezone.now)

    class Meta:
        ordering = ('-publish_time',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

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
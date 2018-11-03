from django.db import models
from stdimage.models import StdImageField

# Create your models here.
class Photo(models.Model):
    photo = StdImageField(upload_to='pho/%Y/%m/%d/',null=True,
                        variations={'thumbnail': {'width': 512 , 'height': 512}})
    uploaded_at = models.DateTimeField('上傳時間',auto_now_add=True)
    
    class Meta:
        ordering = ('-uploaded_at',)
    def __str__(self):
        return str(self.uploaded_at)
    def save(self, *args, **kwargs):
        super(Photo, self).save(*args, **kwargs)
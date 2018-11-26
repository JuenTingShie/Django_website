from django.db import models
from stdimage.models import StdImageField

class Gallery(models.Model):
    image = StdImageField(upload_to='pho/%Y/%m/%d/',null=True,
                        variations={'thumbnail': {'width': 512 , 'height': 512}})
    upload_time = models.DateTimeField('上傳時間',auto_now_add=True)
    uploader = models.CharField('上傳者',max_length = 200 ,editable = False )
    
    def __str__(self):
        return str(self.upload_time)
    def save(self, *args, **kwargs):
        super(Gallery, self).save(*args, **kwargs)
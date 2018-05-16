from django.db import models
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Typeinfo(models.Model):
    # 商品分类
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    book = models.Manager()
    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    # 具体的商品
    gtitle = models.CharField(max_length=20)
    # gpic = models.ImageField(upload_to='static/media')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    g_type = models.ForeignKey(Typeinfo)
    gclick = models.IntegerField(default=0)
    gunit = models.CharField(max_length=20,default='550g')
    gjianjie = models.TextField()
    gpub_date = models.DateTimeField(default=datetime.datetime.now())
    gpubj_date = models.DateTimeField()
    book1 = models.Manager()
    gpic = RichTextUploadingField()

    def __str__(self):
        return  self.gtitle
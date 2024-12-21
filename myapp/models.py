from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

# 站点数据总浏览量、总数据量、总使用量、创建时间
class Site_Data(models.Model):
    total_views = models.BigIntegerField(verbose_name="总浏览量",default=0)
    total_datas = models.IntegerField(verbose_name="总数据量")
    total_used = models.IntegerField(verbose_name="总使用量")
    create_time = models.DateField(verbose_name="创建时间", auto_now=True)

# 上传的原始图像
class Remote_Sensing_Image(models.Model):
    img_name = models.CharField(verbose_name="图像名称", max_length=64)
    img_path = models.ImageField(verbose_name="原始图像路径", max_length=128, upload_to='remote_sensing_images/')
    create_time = models.DateField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.img_name

# 增强后的图像结果
class Augment_Image(models.Model):
    img_path = models.CharField(verbose_name="增强结果路径", max_length=128, blank = True, null = True)
    create_time = models.DateField(verbose_name="创建时间", auto_now_add=True)

# 分割后的图像结果
class Segmentation_Image(models.Model):
    img_path = models.CharField(verbose_name="分割结果路径", max_length=128, blank = True, null = True)
    create_time = models.DateField(verbose_name="创建时间", auto_now_add=True)   
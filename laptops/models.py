from django.db import models

# Create your models here.
class Laptop(models.Model):
	name = models.CharField(max_length=100, verbose_name="نام محصول")
	photo = models.ImageField(upload_to='images', verbose_name="تصویر")
	price = models.IntegerField(verbose_name="قیمت")
	hard = models.CharField(max_length=100, verbose_name="طرقیت حافظه داخلی")
	cpu = models.CharField(max_length=100, verbose_name="پردازنده")
	ram = models.IntegerField(verbose_name="ظرفیت حافطه RAM")
	display = models.IntegerField(verbose_name="اندازه صفحه نمایش")
	ram_type = models.CharField(max_length=100, verbose_name="نوع حافظه RAM")
	display_type = models.CharField(max_length=100, verbose_name="دقت صفحه نمایش")
	hard_type = models.CharField(max_length=200, verbose_name="نوع حافظه داخلی")

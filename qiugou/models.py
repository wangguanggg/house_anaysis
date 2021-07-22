from django.db import models

# Create your models here.
class Qiugou(models.Model):
    name = models.CharField("购房人姓名", max_length=20)
    card = models.CharField("身份证", max_length=20)
    phone = models.CharField("手机号", max_length=30)
    num = models.IntegerField("购房数")
    money = models.FloatField("购房金额", max_length=30)

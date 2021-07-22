from django.db import models

# Create your models here.
class Qiuzu(models.Model):
    name = models.CharField("租房人姓名", max_length=20)
    card = models.CharField("身份证", max_length=20)
    phone = models.CharField("手机号", max_length=30)
    num = models.IntegerField("所租房")
    time = models.CharField("租凭期", max_length=20)
    money = models.FloatField("租房金额", max_length=30)

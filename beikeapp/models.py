from django.db import models

# Create your models here.
class sellhouse(models.Model):
    title = models.CharField("标题", max_length=200)
    address = models.CharField("地址", max_length=20)
    unit_type = models.CharField("户型", max_length=30)
    created_time = models.CharField("建立时间", max_length=30)
    room_type = models.CharField("房间类型", max_length=30)
    area = models.FloatField("面积", max_length=10)
    toward = models.CharField("朝向", max_length=15)
    total_price = models.FloatField("总价", max_length=10)
    unit_price = models.FloatField("单价", max_length=20)
    follows = models.IntegerField("关注人数")

class resthouse(models.Model):
    title = models.CharField("标题", max_length=200)
    room_type = models.CharField("房间类型", max_length=30)
    toward = models.CharField("朝向", max_length=15)
    area = models.FloatField("面积", max_length=10)
    month_price = models.FloatField("月租", max_length=20)
    pass

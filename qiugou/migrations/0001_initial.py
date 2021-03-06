# Generated by Django 2.2 on 2021-07-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Qiugou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='购房人姓名')),
                ('card', models.CharField(max_length=20, verbose_name='身份证')),
                ('phone', models.CharField(max_length=30, verbose_name='手机号')),
                ('num', models.IntegerField(verbose_name='购房数')),
                ('money', models.FloatField(max_length=30, verbose_name='购房金额')),
            ],
        ),
    ]

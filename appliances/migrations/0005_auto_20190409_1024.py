# Generated by Django 2.1.7 on 2019-04-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0004_auto_20190409_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridgemodel',
            name='image',
            field=models.ImageField(upload_to='photo_fridge'),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='image',
            field=models.ImageField(upload_to='photo_tv'),
        ),
    ]

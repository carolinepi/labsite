# Generated by Django 2.1.7 on 2019-04-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appliances', '0002_fridgemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fridgemodel',
            name='clicks',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='tvmodel',
            name='clicks',
            field=models.PositiveIntegerField(),
        ),
    ]

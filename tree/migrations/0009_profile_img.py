# Generated by Django 2.1.2 on 2018-11-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0008_auto_20181109_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]
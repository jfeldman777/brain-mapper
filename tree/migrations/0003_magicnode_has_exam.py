# Generated by Django 2.1.2 on 2018-11-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_magicnode'),
    ]

    operations = [
        migrations.AddField(
            model_name='magicnode',
            name='has_exam',
            field=models.BooleanField(default=False),
        ),
    ]

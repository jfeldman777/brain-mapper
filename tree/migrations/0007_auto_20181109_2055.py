# Generated by Django 2.1.2 on 2018-11-09 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0006_auto_20181105_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('D', 'директор'), ('W', 'автор учебника'), ('Н', 'учитель'), ('S', 'ученик'), ('P', 'родитель'), ('T', 'тьютор'), ('U', 'неизвестно')], default='U', max_length=1),
        ),
    ]
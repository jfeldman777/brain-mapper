# Generated by Django 2.1.2 on 2018-11-03 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_magicnode_has_exam'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('desc', models.CharField(max_length=255)),
                ('figure', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('text', models.TextField(blank=True)),
                ('is_open', models.BooleanField(default=False)),
                ('answer', models.IntegerField()),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tree.MagicNode')),
            ],
        ),
    ]
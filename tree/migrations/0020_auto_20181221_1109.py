# Generated by Django 2.1.2 on 2018-12-21 08:09

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0019_auto_20181213_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='magicnode',
            name='video2',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='magicnode',
            name='video3',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from treebeard.al_tree import AL_Node
from embed_video.fields import EmbedVideoField
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = (
        ('D','директор'),
        ('С','спец по содержанию'),
        ('Н','учитель'),
        ('S','ученик'),
        ('P','родитель'),
        ('T','тьютор'),
        ('U','неизвестно'),
    )

    role = models.CharField(
        max_length=1,
        choices=ROLES,
        default='U',
    )
#############################################################
class MagicNode(AL_Node):
    owner = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default = 1)
    is_ready = models.BooleanField(default = False)
    updated_at = models.DateTimeField(auto_now = True)
    parent = models.ForeignKey('self',
                               related_name='children_set',
                               null=True,
                               db_index=True,on_delete=models.CASCADE)
    sib_order = models.PositiveIntegerField()
    desc = models.CharField(max_length=255)
    figure = models.ImageField(upload_to='uploads/%Y/%m/%d',
                               blank=True,
                               null=True,)
    text = models.TextField(
            blank=True)

    video = EmbedVideoField(null=True,blank=True)  # same like models.URLField(

    sites = ArrayField(
            models.TextField(blank=True),
            blank = True,
            null=True,
            size=5,

        )

    has_exam = models.BooleanField(default = False)

    def __str__(self):
        return self.desc

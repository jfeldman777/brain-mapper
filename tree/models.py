from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from treebeard.al_tree import AL_Node
from embed_video.fields import EmbedVideoField
from django.contrib.postgres.fields import ArrayField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    master = models.ForeignKey(User, related_name='master',
                    on_delete=models.SET_DEFAULT, default = 1)
    parent = models.ForeignKey(User, related_name='parent',
                    on_delete=models.SET_DEFAULT, default = 1)

    ROLES = (
        ('D','директор'),
        ('W','Автор учебника'),
        ('Z','Учитель'),
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

    img = models.ImageField(upload_to='uploads/%Y/%m/%d',
                               blank=True,
                               null=True,)

    birth_date = models.DateField(null=True, blank=True)
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
############################################################
class Quiz(models.Model):
    node = models.ForeignKey(MagicNode, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    desc = models.CharField(max_length=255)
    figure = models.ImageField(upload_to='uploads/%Y/%m/%d',
                               blank=True,
                               null=True,)
    text = models.TextField(blank=True)
    is_open = models.BooleanField(default = False)
    answer = models.IntegerField(blank=True)
    is_ready = models.BooleanField(default = False)

    def __str__(self):
        return self.desc + ' ( ' + str(self.node)+ ' # '+ str(self.number) + ' )'

class Exam(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    answer = models.IntegerField(blank=True, default=0)
    text = models.TextField(blank=True)
    need_help = models.BooleanField(default = False)

class Ticket(models.Model):
    student = models.ForeignKey(User, on_delete=models.PROTECT, related_name='student')
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, related_name='teacher')
    book = models.ForeignKey(MagicNode, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-updated_at','-created_at',]
    def __str__(self):
        return str(self.student) + ' ( ' + str(self.book) + ' @ '+ str(self.teacher) + ' )'

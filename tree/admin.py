from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from .models import Quiz
from .models import Exam, Ticket

class TicketAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ticket, TicketAdmin)

class ExamAdmin(admin.ModelAdmin):
    pass
admin.site.register(Exam, ExamAdmin)

class QuizAdmin(admin.ModelAdmin):
    pass
admin.site.register(Quiz, QuizAdmin)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import MagicNode

class MagicAdmin(TreeAdmin):
    form = movenodeform_factory(MagicNode)

admin.site.register(MagicNode, MagicAdmin)

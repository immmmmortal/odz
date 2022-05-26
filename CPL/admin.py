from django.contrib import admin

# Register your models here.
from CPL.models import *


@admin.register(CyclingEvent, User)
class CyclingEventAdmin(admin.ModelAdmin):
    pass


class EventParticipatingGroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'get_group_members')


admin.site.register(EventParticipatingGroup, EventParticipatingGroupAdmin)

from django.contrib import admin

from schedules.models import Schedule


@admin.register(Schedule)
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('day', 'time', 'mentoring', 'student')


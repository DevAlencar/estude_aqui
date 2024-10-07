from django.contrib import admin

from users.models import Mentor, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course_student')


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('user', 'course_mentor', 'cpf_mentor')


from django.contrib import admin

from classes.models import Category, Mentoring, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category',)


@admin.register(Mentoring)
class MentoringAdmin(admin.ModelAdmin):
    list_display = ('name_mentoring', 'value_mentoring', 'description_mentoring', 'category', 'mentor')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('body_review', 'mentor', 'student')

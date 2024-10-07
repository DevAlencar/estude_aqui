from django.db import models

from users.models import Mentor, Student


class Category(models.Model):
    name_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name_category


class Mentoring(models.Model):
    name_mentoring = models.CharField(max_length=100)
    value_mentoring = models.CharField(max_length=100)
    description_mentoring = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_mentoring

class Review(models.Model):
    body_review = models.CharField(max_length=100)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.body_review



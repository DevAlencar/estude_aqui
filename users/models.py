from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_student = models.CharField(max_length=100)



class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course_mentor = models.CharField(max_length=100)
    cpf_mentor = models.CharField(max_length=15)


from django.db import models

from classes.models import Mentoring
from users.models import Student


class Schedule(models.Model):
    day = models.DateField()
    time = models.TimeField()
    mentoring = models.ForeignKey(Mentoring, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.day} às {self.time}"


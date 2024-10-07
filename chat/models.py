from django.db import models

from users.models import Mentor, Student


class Message(models.Model):
    body_message = models.CharField(max_length=100)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.body_message



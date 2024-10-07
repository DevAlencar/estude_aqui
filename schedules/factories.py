import factory
from factory import Faker, SubFactory
from .models import Schedule
from users.factories import StudentFactory
from classes.factories import MentoringFactory


class ScheduleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Schedule

    day = Faker('date_this_year')
    time = Faker('time')
    mentoring = SubFactory(MentoringFactory)
    student = SubFactory(StudentFactory)


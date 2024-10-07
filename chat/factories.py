import factory
from factory import Faker, SubFactory

from users.factories import MentorFactory, StudentFactory
from .models import Message

class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Message

    body_message = Faker('text', max_nb_chars=100)
    mentor = SubFactory(MentorFactory)
    student = SubFactory(StudentFactory)

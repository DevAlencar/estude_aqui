import factory
from factory import Faker
from django.contrib.auth.models import User
from .models import Student, Mentor

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = Faker('user_name')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    email = Faker('email')

class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    user = factory.SubFactory(UserFactory)
    course_student = factory.Faker('word')

class MentorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mentor

    user = factory.SubFactory(UserFactory)
    course_mentor = factory.Faker('word')
    cpf_mentor = Faker('cpf', locale='pt_BR')

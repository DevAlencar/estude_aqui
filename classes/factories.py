import factory
from factory import Faker, SubFactory

from users.factories import MentorFactory, StudentFactory
from .models import Category, Mentoring, Review


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name_category = Faker('word')

class MentoringFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Mentoring

    name_mentoring = Faker('sentence', nb_words=3)
    value_mentoring = Faker('random_number', digits=2)
    description_mentoring = Faker('text', max_nb_chars=100)
    category = SubFactory(CategoryFactory)
    mentor = SubFactory(MentorFactory)

class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    body_review = Faker('text', max_nb_chars=100)
    mentor = SubFactory(MentorFactory)
    student = SubFactory(StudentFactory)


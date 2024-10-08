from django.shortcuts import render
from rest_framework import viewsets

from classes.models import Category, Mentoring, Review
from classes.serializers import CategorySerializer, MentoringSerializer, ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MentoringViewSet(viewsets.ModelViewSet):
    queryset = Mentoring.objects.all()
    serializer_class = MentoringSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
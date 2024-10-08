from rest_framework import serializers
from classes.models import Category, Mentoring, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MentoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentoring
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

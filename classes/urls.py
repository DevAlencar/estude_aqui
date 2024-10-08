from django.urls import path

from classes import views

urlpatterns = [
    path("classes/category/", views.CategoryViewSet.as_view(), name="category_model_view"),
    path("classes/mentoring/", views.MentoringViewSet.as_view(), name="mentoring_model_view"),
    path("classes/review/", views.ReviewViewSet.as_view(), name="review_model_view"),
]
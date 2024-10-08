from django.urls import path

from schedules import views

urlpatterns = [
    path("schedules/", views.ScheduleListCreateView.as_view(), name="schedules_create_list"),
    path("schedules/<int:pk>", views.ScheduleDetailView.as_view(), name="schedules_detail"),
]
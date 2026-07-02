from django.urls import path
from .views import JobCreateAPI, UserTestAPI, JobListAPI

urlpatterns = [
    path('user/', UserTestAPI.as_view()),
    path('jobs/', JobListAPI.as_view()),
    path('jobs/create/', JobCreateAPI.as_view()),
]


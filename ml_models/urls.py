from django.urls import path
from . import views


urlpatterns = [
    path("hello/", views.say_hello),
    path("iris/", views.classification_function),
    path("score/", views.regression_function),
]

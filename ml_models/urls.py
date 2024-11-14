from django.urls import path
from . import views


urlpatterns = [
    path("iris/", views.classification_function),
    path("score/", views.regression_function),
]

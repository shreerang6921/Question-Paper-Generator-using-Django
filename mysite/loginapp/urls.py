from django.urls import path
from loginapp import views

urlpatterns = [
    path("question",views.index, name="question")
]
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
import random


def index(request):
    questions = Question.objects.all()
    params = {'questions':questions}
    print(questions[1].ques)
    return render(request, 'question.html', params)
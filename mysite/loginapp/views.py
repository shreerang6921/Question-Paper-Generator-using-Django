from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
import random


def index(request):
    ques = Question.objects.all()
    params = {'ques':ques}
    print(ques)
    return render(request, 'questions.html', params)
from django.http import HttpResponse
from django.shortcuts import render
import random


def index(request):
    return render(request, 'index.html')

def generatePaper(request):
    print('GenertePaperRequest')
    return render(request, 'generatePaper.html')

def about(request):
    mytext = request.POST.get('ques1', 'default')    #get the text from text box
    noOfQues = request.POST.get('noOfQues', 'NULL')
    print("mytext: "+mytext)
    print("noOFQes: "+noOfQues)

    k=''
    l=[]
    for i in mytext:
        k=k+i
        if i=='\n':
            k = k.strip()
            l.append(k)
            k=''

    finalListOfQues = []
    
    print(l)
    i = 0
    while i < int(noOfQues):
        rand = random.choice(l)
        if rand not in finalListOfQues:
            finalListOfQues.append(rand)
            i=i+1

    print(finalListOfQues)

    lastString = ''
    z = 1
    for i in finalListOfQues:
        i = "Q" + str(z) + ". " + i
        lastString = lastString + i + "\n"
        z = z+1

    params = {"q1" : lastString}
    return render(request, 'questions.html', params)

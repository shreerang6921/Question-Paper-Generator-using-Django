from django.db import models

# Create your models here.
# class Question(models.Model):
#     qid = models.AutoField
#     ques = models.CharField(max_length=150)
#     sub = models.CharField(max_length=30)
#     class Diff(models.IntegerChoices):
#         simple=1
#         hard=2
    
#     def __str__(self):
#         return self.sub

#     diff = models.IntegerField(choices=Diff.choices)
#     class Meta:
#         db_table = "question"

class questionBank(models.Model):
    question = models.CharField(max_length=300)
    chapter = models.IntegerField()
    difficulty = models.IntegerField()
    marks = models.IntegerField()
    unit = models.IntegerField()
    sem = models.IntegerField()
    year = models.IntegerField()
    subname = models.CharField(max_length=100)

    def __str__(self):
        return self.question

    class Meta:
        db_table = "questionBank"

    
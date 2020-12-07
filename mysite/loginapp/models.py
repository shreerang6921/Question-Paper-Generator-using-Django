from django.db import models

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
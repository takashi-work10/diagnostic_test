# diagnosis/models.py
from django.db import models

class DiagnosisResult(models.Model):
    """
    20個の回答を保存する例。
    質問が少ないなら数を減らしてもOK。
    """
    question1 = models.IntegerField()
    question2 = models.IntegerField()
    question3 = models.IntegerField()
    question4 = models.IntegerField()
    question5 = models.IntegerField()
    question6 = models.IntegerField()
    question7 = models.IntegerField()
    question8 = models.IntegerField()
    question9 = models.IntegerField()
    question10 = models.IntegerField()
    question11 = models.IntegerField()
    question12 = models.IntegerField()
    question13 = models.IntegerField()
    question14 = models.IntegerField()
    question15 = models.IntegerField()
    question16 = models.IntegerField()
    question17 = models.IntegerField()
    question18 = models.IntegerField()
    question19 = models.IntegerField()
    question20 = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DiagnosisResult #{self.id}"

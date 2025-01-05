# diagnosis/models.py
from django.db import models

class DiagnosisResult(models.Model):
    """
    20問の回答をDBに保存するモデル。
    q1～q20 それぞれ -3~+3 の整数を想定
    また、最終判定された不安タイプ(result_type)も保存
    """
    # 20個の回答
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()
    q13 = models.IntegerField()
    q14 = models.IntegerField()
    q15 = models.IntegerField()
    q16 = models.IntegerField()
    q17 = models.IntegerField()
    q18 = models.IntegerField()
    q19 = models.IntegerField()
    q20 = models.IntegerField()

    # 8つのタイプのどれかを保存
    result_type = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DiagnosisResult #{self.id} ({self.result_type})"

# diagnosis/admin.py
from django.contrib import admin
from .models import DiagnosisResult

@admin.register(DiagnosisResult)
class DiagnosisResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')  # 管理画面の一覧表示に出したいフィールド

# mysite/urls.py (例)
from django.contrib import admin
from django.urls import path
from diagnosis.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
]

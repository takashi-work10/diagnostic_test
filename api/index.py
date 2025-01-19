# api/index.py
import os
import sys
from django.core.wsgi import get_wsgi_application

#
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Djangoプロジェクトパスを追加する（configディレクトリ等を認識させるため）
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

app = get_wsgi_application()

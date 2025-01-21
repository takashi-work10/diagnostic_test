# index.py
import os
from django.core.wsgi import get_wsgi_application

# Django の settings.py を指定
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# WSGI アプリケーションを作成
application = get_wsgi_application()

# Vercel は Lambda 互換のハンドラを想定しているので、
# Python Runtime (Beta) 用に以下のように定義してみる
def handler(event, context):
    # event/context を Django WSGI にどう渡すかは実装次第
    # 実験的な例: "Mangum" や "apig-wsgi" を使うケースもあり
    return application(event, context)

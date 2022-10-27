from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Key
from .views import get_random_code

def key_update():
    Key.objects.create(key=get_random_code(100))
    print("key is updated!")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(key_update, 'cron', hour=0, minute=0)# 毎日0時0分に実行
    #scheduler.add_job(key_update, 'interval', minutes=1)
    scheduler.start()
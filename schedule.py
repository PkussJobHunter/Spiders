import sched
import time

#执行定时任务
# coding = utf-8
from apscheduler.schedulers.twisted  import TwistedScheduler
import time
import os
import sys
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(p)
from twisted.internet import reactor

def job():
    pass

sched = TwistedScheduler()
sched.add_job(job, 'cron', hour='*/2', id='push_ip')
sched.start()
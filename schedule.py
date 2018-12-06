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

sched = TwistedScheduler()
logger = Log().getLogger('development')
crawler.start(sched)
sched.add_job(push_ip, 'cron', hour='*/2', id='push_ip')
sched.start()
logger.info('sched start')
reactor.run()
logger.info('sched end')
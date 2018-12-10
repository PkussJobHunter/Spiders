#执行定时任务
# coding = utf-8
from apscheduler.schedulers.twisted  import TwistedScheduler
import time
import os
import sys
import requests
p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(p)
from twisted.internet import reactor
import json

path = os.path.abspath(os.path.dirname(__file__))
ip_source = path + '/Spiders/ip_source.json'
with open(ip_source, 'r') as f:
    data = json.load(f)
    print(data)
    f.close()

# 列出所有项目
# curl http://localhost:6800/listprojects.json
# return status， projects
# {"status": "ok", "projects": ["myproject", "otherproject"]}

# 运行spider
# curl http://localhost:6800/schedule.json -d project=myproject -d spider=somespider
# return status,jobid
# {"status": "ok", "jobid": "6487ec79947edab326d6db28a2d86511e8247444"}

# 列出所有spiders
# curl http://localhost:6800/listspiders.json?project=myproject
# return status, spiders
# {"status": "ok", "spiders": ["spider1", "spider2", "spider3"]}

# 列出所有任务
# curl http://localhost:6800/listjobs.json?project=myproject | python -m json.tool
# return json
# {
#     "status": "ok",
#     "pending": [
#         {
#             "project": "myproject", "spider": "spider1",
#             "id": "78391cc0fcaf11e1b0090800272a6d06"
#         }
#     ],
#     "running": [
#         {
#             "id": "422e608f9f28cef127b3d5ef93fe9399",
#             "project": "myproject", "spider": "spider2",
#             "start_time": "2012-09-12 10:14:03.594664"
#         }
#     ],
#     "finished": [
#         {
#             "id": "2f16646cfcaf11e1b0090800272a6d06",
#             "project": "myproject", "spider": "spider3",
#             "start_time": "2012-09-12 10:14:03.594664",
#             "end_time": "2012-09-12 10:24:03.594664"
#         }
#     ]
# }

#

# sched = TwistedScheduler()
# sched.add_job(job, 'cron', hour='*/2', id='push_ip')
# sched.start()
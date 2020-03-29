import os
from script import main
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.blocking import BlockingScheduler

cron_schedule = os.environ["CRON_SCHEDULE"]

scheduler = BlockingScheduler()
scheduler.add_job(main, CronTrigger.from_crontab(cron_schedule))

scheduler.start()

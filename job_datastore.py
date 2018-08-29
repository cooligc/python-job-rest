from apscheduler.scheduler import Scheduler
from data_store import engine

from apscheduler.schedulers.background import  BackgroundScheduler


# # Start the scheduler
# sched = Scheduler()

def job_function():
    print "Hello World"

def start_job():
    jobstores = {
        'mongo': MongoDBJobStore(),
        'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    }
    executors = {
        'default': ThreadPoolExecutor(20),
        'processpool': ProcessPoolExecutor(5)
    }
    job_defaults = {
        'coalesce': False,
        'max_instances': 3
    }
    scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

    # Schedules job_function to be run on the third Friday
    # of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
    sched.add_cron_job(job_function, second=10)
    sched.start()
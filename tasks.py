from celery import Celery 

# the first you need is a celery instance. We call this Celery application or just
# app for short. AS this instance is used as the entry-point for everything
# you want to do in Celery, like creating tasks and managing workers, it must be
# possible for other modules to import it.

app = Celery('tasks', backend='db+mysql://rashid:password@localhost:3306/airflowdb', broker='amqp://user:password@127.0.0.1:5672//')

@app.task
def add(x, y):
   return x + y


from .celery import app
import time 


@app.task
def add(x, y):
    time.sleep(10)
    print("Done sleeping. Executing the add command")
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

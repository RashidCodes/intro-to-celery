from proj.tasks import add
import time

# A task can only be in a single state, but it can progress through
# several states. The stages of a typical task can be:
# PENDING -> STARTED -> SUCCESS

def print_hello():
    print("hello from celery")



if __name__ == '__main__':
    # some asynchronous task
    result = add.delay(2,2)

    while result.state != 'SUCCESS':
        time.sleep(1.5)
        print_hello()


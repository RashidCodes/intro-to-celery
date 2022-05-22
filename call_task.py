from tasks import add 

# to call a task, you can use the delay() method
async_result = add.delay(4,4)

# Calling a task returns an AsyncResult instance. It can be used to check the state of the task,
# wait for the task to finish, or get its return value (or if the task failed, to get the exception 
# and traceback)


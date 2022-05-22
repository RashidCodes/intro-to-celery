from celery import Celery


app = Celery('proj', backend='db+mysql://rashid:password@localhost:3306/airflowdb', broker='amqp://user:password@127.0.0.1:5672//', include=['proj.tasks'])


app.conf.update(
        result_expires=3600,
        task_routes = {
            'proj.tasks.add': {'queue': 'hipri'},
        },
)


if __name__ == '__main__':
    app.start()

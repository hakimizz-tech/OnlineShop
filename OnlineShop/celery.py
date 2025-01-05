import os
from celery import Celery

# set the default django setting module for the celery command line program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineShop.settings')

app = Celery('OnlineShop')
app.config_from_object('django.conf:settings', namespace='CELERY') 
#tells Celery to read its configuration from Django's settings file.

app.autodiscover_tasks()
#find tasks defined in any installed Django app listed in the INSTALLED_APPS setting.
# It looks for a tasks.py file in each app directory, like this:


"""
    CELERY_BROKER_URL: Specifies the message broker. In this example, it's RabbitMQ, which uses the amqp:// protocol.
    CELERY_RESULT_BACKEND: Determines where task results are stored (e.g., RabbitMQ, Redis, or a database).
    CELERY_ACCEPT_CONTENT and CELERY_TASK_SERIALIZER: Define the formats Celery can process (e.g., JSON).
    CELERY_ALWAYS_EAGER: setting allows you to execute tasks locally in a synchronous manner instead of sending them to the queue.

    CELERY_BROKER_URL = 'amqp://localhost'
    CELERY_RESULT_BACKEND = 'rpc://'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'

"""
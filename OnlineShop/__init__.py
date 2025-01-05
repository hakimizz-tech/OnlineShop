from celery import  app as celery_app

# To ensure celery is loaded when django starts
__all__ = ['celery_app']
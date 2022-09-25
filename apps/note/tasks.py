# from __future__ import absolute_import, unicode_literals
from celery import shared_task
import celery
# app = Celery('myproject'）

class BaseTask(celery.Task):
    max_retries = 3
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(f"Celery task [{task_id}] failed: [{einfo}], args: [{args}]")

    def on_success(self, retval, task_id, args, kwargs):
        print(f"Celery task [{task_id}] success: {retval}")

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        print(f"Celery task [{task_id}] retry: {einfo}")


@shared_task(base=BaseTask)
def add(x, y):
    return x + y

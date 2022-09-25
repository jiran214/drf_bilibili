from django.core.mail import send_mail
# from __future__ import absolute_import, unicode_literals
from celery import shared_task, Task

from bilibili import settings


class BaseTask(Task):
    max_retries = 3

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print(f"Celery task [{task_id}] failed: [{einfo}], args: [{args}]")

    def on_success(self, retval, task_id, args, kwargs):
        print(f"Celery task [{task_id}] success: {retval}")

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        print(f"Celery task [{task_id}] retry: {einfo}")


@shared_task(base=BaseTask)
def send_mail_task(email, username,code):
    """
    使用django内置函数发送邮件
    """
    subject = "mzh"
    message = ""
    sender = settings.EMAIL_FROM  # 发
    recipient = [email]  # 收
    html_message = f"<h1>{username} 验证码为{code}</h1>"
    send_mail(subject, message, sender, recipient, html_message=html_message)

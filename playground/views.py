from django.core.mail import BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers


def say_hello(request):
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context={'name': 'Nipun'}
    #     )
    #     message.send(['john@admin.com'])
    # except BadHeaderError:
    #     pass

    notify_customers.delay('Hello')
    return render(request, 'hello.html', {'name': 'Nipun'})

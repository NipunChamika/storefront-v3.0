from django.core.mail import BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Nipun'}
        )
        message.send(['john@admin.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Nipun'})

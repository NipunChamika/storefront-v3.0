from django.core.cache import cache
from django.core.mail import BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests


def say_hello(request):
    # try:
    #     message = BaseEmailMessage(
    #         template_name='emails/hello.html',
    #         context={'name': 'Nipun'}
    #     )
    #     message.send(['john@admin.com'])
    # except BadHeaderError:
    #     pass

    # notify_customers.delay('Hello')

    key = 'httpbin_result'
    if cache.get(key) is None:
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        cache.set(key, data)
    return render(request, 'hello.html', {'name': cache.get(key)})

from django.core.cache import cache
from django.core.mail import BadHeaderError
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests


class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': data})


# @cache_page(5 * 60)
# def say_hello(request):
#     # try:
#     #     message = BaseEmailMessage(
#     #         template_name='emails/hello.html',
#     #         context={'name': 'Nipun'}
#     #     )
#     #     message.send(['john@admin.com'])
#     # except BadHeaderError:
#     #     pass

#     # notify_customers.delay('Hello')

#     response = requests.get('https://httpbin.org/delay/2')
#     data = response.json()
#     return render(request, 'hello.html', {'name': data})

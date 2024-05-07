from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        message = EmailMessage('subject', 'message',
                               'nipun@admin.com', ['john@admin.com'])
        message.attach_file('playground/static/images/clock.png')
        message.send()
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Nipun'})

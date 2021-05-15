from django.http import HttpResponse
#utilidades como la hora
from datetime import datetime

def hello(request):
    now = str(datetime.now().strftime('%b %dth,%Y - %H:%M hrs '))
    return HttpResponse(f'La hora exacta es: {now}')

def hi(request):

    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))

def mayores(request,name,age):
    if age < 12:
        message = (f'Usted {name} es menor de edad y no puede pasar')
    else:
        message= (F'Bienvenido {name}')

    return HttpResponse(message)
from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'interfeys.html')

def pay(request):
    date_time = datetime.now()
    formatted_time = date_time.strftime('%H:%M/%d.%m.%Y')
    ctx = {'date_time': formatted_time}
    return render(request, 'pay.html', ctx)

def qr(request):
    return render(request, 'qr.html')
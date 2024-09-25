from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    date = datetime.datetime.now().year
    return render(request, 'index.html', {'date': date})
    

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    return render(request, 'contact.html')




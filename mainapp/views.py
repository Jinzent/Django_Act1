from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def hours(request):
    return render(request, 'hours.html')

def contact(request):
    return render(request, 'contact.html')

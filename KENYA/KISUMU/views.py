from django.shortcuts import render
def home(request):
    return render(request,'home.html',  {'bike': 'home'})

def about(request):
    return render(request, 'about.html',  {'bike': 'about'})

def contact(request):
    return render(request, 'contact.html', {'bike': 'contact'})



# Create your views here.

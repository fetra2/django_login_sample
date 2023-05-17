from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import ContactForm, infoClientForm

def index(request):
    return render(request, 'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')


def contact(request):
    if request.method == 'POST':
        formContact = ContactForm(request.POST)
        if formContact.is_valid():
            return render(request, 'login.html')
    else:
        formContact = ContactForm()
        return render(request, 'contact.html', {'form_contact': formContact})

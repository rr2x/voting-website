from django.shortcuts import render, redirect
from django.urls import reverse


def welcometoauth(request):
    return render(request, 'authentication/index.html')


def login(request):
    if request.method == 'POST':
        return redirect(reverse('frontpage'))

    return render(request, 'authentication/login.html')


def signup(request):
    if request.method == 'POST':
        return redirect(reverse('frontpage'))

    return render(request, 'authentication/signup.html')


def resetpassword(request):
    if request.method == 'POST':
        return redirect(reverse('frontpage'))

    return render(request, 'authentication/resetpassword.html')

from django.shortcuts import render
from django.http import HttpResponse


def welcometoauth(request):
    return render(request, 'authentication/index.html')

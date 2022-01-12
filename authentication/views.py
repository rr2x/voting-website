from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from validate_email import validate_email
from .models import User


def login(request):
    if request.method == 'POST':
        return redirect(reverse('frontpage'))

    return render(request, 'authentication/login.html')


def signup(request):
    if request.method == 'POST':
        context = {'has_error_password': False,
                   'has_error_email': False,
                   'account_created': False,
                   'data': request.POST}

        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Password should be 6 characters or more', extra_tags="password_error")
            context['has_error_password'] = True

        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'Password mismatch', extra_tags="password_error")
            context['has_error_password'] = True

        if not validate_email(email):
            messages.add_message(request, messages.ERROR,
                                 'Invalid Email Address', extra_tags="email_error")
            context['has_error_email'] = True

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Email already used', extra_tags="email_error")
            context['has_error_email'] = True

        if context['has_error_password'] or context['has_error_email']:
            return render(request, 'authentication/signup.html', context)

        user = User.objects.create_user(email=email, password=password)
        user.save()

        messages.add_message(request, messages.SUCCESS,
                             'Account created, please confirm via email', extra_tags="account_created")
        context['account_created'] = True

    return render(request, 'authentication/signup.html')


def resetpassword(request):
    if request.method == 'POST':
        return redirect(reverse('frontpage'))

    return render(request, 'authentication/resetpassword.html')

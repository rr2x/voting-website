from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from validate_email import validate_email
from .models import User

from utilities.decorators import auth_user_should_not_access


def auth(request):
    return redirect(reverse('main-frontpage-url'))


@auth_user_should_not_access
def login(request):
    if request.method == 'POST':

        context = {'has_error': False,
                   'data': request.POST}

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if not user or user.is_superuser or not user.is_active:
            messages.add_message(request, messages.ERROR,
                                 'Account not found or invalid credentials')
            context['has_error'] = True
            return render(request, 'authentication/login.html', context)

        if not user.is_verified:
            messages.add_message(request, messages.ERROR,
                                 'Check your email to verify account')
            context['has_error'] = True
            return render(request, 'authentication/login.html', context)

        auth_login(request, user)

        return redirect(reverse('main-dashboard-url'))

    return render(request, 'authentication/login.html')


@auth_user_should_not_access
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

        # TODO: verification email, use mailtrap, then if not development use actual email sending

        return render(request, 'authentication/signup.html', context)

    return render(request, 'authentication/signup.html')


# TODO: reset pass
def resetpassword(request):
    if request.method == 'POST':
        return redirect(reverse('main-frontpage-url'))

    return render(request, 'authentication/resetpassword.html')


def logout(request):
    auth_logout(request)
    return render(request, 'authentication/logout.html')

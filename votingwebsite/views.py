from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def FrontPage(request):
    return render(request, 'index.html')


def SubmitContact(request):
    # after allowing submission via hCaptcha, tell user their inquiry has been submitted
    return render(request, 'index.html')


@login_required
def Dashboard(request):
    return render(request, 'dashboard.html')

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    message = None
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is None:
            try:
                user = User.objects.get(email=username)
                user = authenticate(username=user.username, password=password)
            except:
                user = None
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                message = 'Your account has disabled.'
        else:
            message = 'The username or password were incorrect.'

    return render(
        request,
        'login.html',
        {
            'message': message
        }
    )

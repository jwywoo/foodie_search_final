from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from .forms import SignupForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'food/main.html')
        else:
            return render(request, 'user/login.html', {'message': 'Wrong password/username'})
    else:
        return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return render(request, 'food/main.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.signup()
            login(request, user)
            return render(request, 'food/main.html')
    else:
        form = SignupForm()

    context = {
        'form': form,
    }
    return render(request, 'user/user_create.html', context)

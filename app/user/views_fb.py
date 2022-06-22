from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from .forms import SignupForm
import pyrebase

config = {
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


# def signIn(request):
#     return render(request, "user/login.html")


def postsign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pasw = request.POST.get('pass')
        try:
            # if there is no error then signin the user with given email and password
            user = authe.sign_in_with_email_and_password(email, pasw)
        except:
            message = "Invalid Credentials!!Please ChecK your Data"
            return render(request, "user/login.html", {"message": message})
        session_id = user['idToken']
        request.session['uid'] = str(session_id)
        return render(request, "food/main.html", {"email": email})
    else:
        return render(request, "user/login.html")


def user_logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "food/main.html")


def user_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passs = request.POST.get('pass')
        name = request.POST.get('name')
        try:
            # creating a user with the given email and password
            user = authe.create_user_with_email_and_password(email, passs)
            uid = user['localId']
            idtoken = request.session['uid']
        except:
            return render(request, "food/main.html")
        return render(request, "user/login.html")
    else:
        return render(request, 'user/user_create.html')

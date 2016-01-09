from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from datetime import datetime


# Create your views here.
def password_reset(request):
    if request.user.is_active:
        return redirect('/reset/change_password/')
    else:
        page_title = 'Password Reset'
        if request.method == 'GET':
            return render(request, 'password_reset/login_reset.html' )

        elif request.method == 'POST':
            email = request.POST.get('email')
            try:
                user = User.objects.get(email=email)
            except:
                return redirect('/')
                # return HttpResponse('User not found.')
            password = User.objects.make_random_password(length=16)
            user.set_password(password)
            # user.save()
            sendResetEmail(email, password)
            return render(request, 'password_reset/reset_success.html')


@login_required
def change_password(request):
    if request.method == 'GET':
        return render(request, 'password_reset/change_password.html')
    elif request.method == 'POST':
        new_pass = request.POST.get('new_password')
        user = User.objects.get(id=request.user.id)
        user.set_password(new_pass)
        user.save()
        username = user.username
        userAuth = authenticate(username=username, password=new_pass)
        if userAuth is not None:
            login(request, userAuth)
        return redirect('/reset/change_password/')


def sendResetEmail(userEmail, new_pass):
    '''Sends the user their reset passwords.
    : param username: username
    : param userEmail: user email
    : param new_pass: user password from user.set_password()
    '''
    email = "philshoreteam@gmail.com"
    dateReset = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    resetTimeMessage = "Your password has been reset on " + str(dateReset)
    noticeMessage = "\nPlease change your password as soon as possible."
    signature = "\n\nPhilSHORE Team\nThis email is system-generated."
    doNotReply = " Please do not reply."
    main_message = resetTimeMessage + noticeMessage + signature + doNotReply
    send_mail('PhilSHORE Password Reset', "\nPassword: " + str(new_pass) + "\n" + main_message,
              email, [str(userEmail)])

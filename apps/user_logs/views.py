from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.user_logs.models import TimeIn, TimeOut
from time import strftime

# Create your views here.


@login_required
def user_logs(request):
    """
    Render update profile page. Fields were already filled up
    by default values from the database. Some values like username,
    first name, last name and organization cannot be edited.
    """
    page_title = "Daily Time Record"
    user = request.user
    timeInlist = TimeIn.objects.filter(userId=request.user.id)
    timeOutlist = TimeOut.objects.filter(userId=request.user.id)
    return render(request, 'profile/logs.html',
                  {'page_title': page_title,
                   'user': user,
                   'timeInList': timeInlist,
                   'timeOutList': timeOutlist,
                   })


def record_timein(request):
    timein = TimeIn()
    timein.userId = request.user.id
    timein.dateIn = strftime("%Y-%m-%d")
    timein.timeIn = strftime("%H:%M:%S")
    timein.save()
    return redirect("/profile/")


def record_timeout(request):
    timeout = TimeOut()
    timeout.userId = request.user.id
    timeout.dateOut = strftime("%Y-%m-%d")
    timeout.timeOut = strftime("%H:%M:%S")
    timeout.save()
    return redirect("/profile/")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from apps.register.models import UserComponent
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


@user_passes_test(lambda u: u.is_staff, login_url='/profile/')
def admin_dashboard(request):
    page_title = "Admin Dashboard"
    users = User.objects.all().exclude(id=request.user.id).values(
            'id', 'first_name')
    component = UserComponent.objects.all().exclude(user_id=request.user.id).values(
            'user_id', 'component')
    data_dict = ValuesQuerySetToDict(users, component)
    print(data_dict)
    dateToday = strftime("%Y-%m-%d")
    timeInListToday = TimeIn.objects.filter(dateIn=dateToday)
    admin = User.objects.get(id=request.user.id)
    return render(request, 'profile/dashboard.html',
                  {'page_title': page_title,
                   'users': users,
                   'admin':admin,
                   'timeInList': timeInListToday,
                   'data_dict': data_dict,
                   })


@user_passes_test(lambda u: u.is_staff, login_url='/profile/')
def admin_logs(request, user_id):
    page_title = "Admin Logs"
    user = request.user
    client = User.objects.get(id=user_id)
    timeInlist = TimeIn.objects.filter(userId=user_id)
    timeOutlist = TimeOut.objects.filter(userId=user_id)
    return render(request, 'profile/logs.html',
                  {'page_title': page_title,
                   'user': user,
                   'timeInList': timeInlist,
                   'timeOutList': timeOutlist,
                   'client': client,
                   })


def ValuesQuerySetToDict(vqs, vqs2):
    """
    Converts a query set to a valid json response.
    Joins two data models [User, UserProfile]
    """
    userdata = {"user": []}
    for item, item2 in zip(vqs, vqs2):
        temp = {}
        temp['id'] = item['id']
        temp['first_name'] = item['first_name']
        temp['component'] = item2['component']
        userdata['user'].append(temp)
    return [userdata]
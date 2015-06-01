from django.shortcuts import render, redirect
from apps.register.forms import RegistrationUserForm
from apps.register.forms import RegistrationUserComponentForm


def register(request):
    """
    Creates a user registration form.
    Sets values for User model with fields 'is_superuser',
    'is_active' and 'is_staff' to False.
    """
    page_title = "Registration"
    registered = False
    if request.method == 'POST':
        print("hello world")
        # User and Profile data are pulled from the rendered forms.
        user_form = RegistrationUserForm(data=request.POST)
        component_form = RegistrationUserComponentForm(data=request.POST)
        # Checks the forms' validity.
        if user_form.is_valid() and component_form.is_valid():
            user = user_form.save()
            # Default value of user roles
            user.is_superuser = False
            user.is_active = True
            user.is_staff = False
            # user.set_password(form.password) encrypts user password
            user.set_password(user.password)
            user.save()
            # Before writing to the database store initial info in memory.
            component = component_form.save(commit=False)
            # Binds the user profile with a specific user.
            component.user = user
            # Writes profile info to profile table.
            component.save()
            # Sets register into true.
            registered = True
            # Send a registration success email.
            return redirect('/register/success/')
    else:
        # Render initial registration page
        user_form = RegistrationUserForm()
        component_form = RegistrationUserComponentForm()
    return render(request, 'registration/register.html',
                  {'user_form': user_form,
                   'component_form': component_form,
                   'page_title': page_title,
                   'registered': registered})


def success_register(request):
    """
    Renders a registration success page.
    """
    page_title = "Success"
    return render(request, 'registration/register_success.html', {
        "page_title": page_title
    })

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Login Module
# Accessible even if user is not logged in


def user_login(request):
    """
    Renders a user login page.
    If user is already logged in, render the user's profile.
    """
    page_title = "Login"
    # Check if user is logged in
    if request.user.is_staff:
        return redirect('/dashboard/')
    else:
        if request.user.is_active:
            # Redirect to user profile page
            return redirect('/profile/')
        # If user is not logged in !
        else:
            # Login Button is clicked
            if request.method == 'POST':
                # Get user name and password from login form
                username = request.POST.get('username')
                password = request.POST.get('password')
                # Check if user is valid
                try:
                    user = authenticate(username=username, password=password)
                    # If user is activated
                    if user.is_active:
                        # Login the user
                        login(request, user)
                        if user.is_staff:
                            return redirect('profile/dashboard/')
                        # Render the user profile page
                        else:
                            return redirect('/profile/')
                    # If user is not activated
                    elif user.is_active is False:
                        # Display account deactivated as flash message
                        message = "Account Deactivated"
                        return render(request, 'login/login.html', {
                            'page_title': page_title,
                            'message': message, 'invalid': True})
                # if user is not valid
                except:
                    # Display invalid credentials as flash message
                    loginMessage = 'Invalid Username or Password'
                    return render(request, 'login/login.html', {
                        'page_title': page_title,
                        'message': loginMessage, 'invalid': True})
            else:
                # Render login.html for initial request of the page
                return render(request, 'login/login.html', {
                    'page_title': page_title,
                })


# Logout Module
# Only accessible if user is logged in
@login_required
def user_logout(request):
    """
    A logged in user will be logged out of their session.
    """
    # Logout the session of the user
    logout(request)
    page_title = "Login"
    # Redirect to the login.html after logout
    logoutMessage = "You have been logged out."
    return render(request, 'login/login.html', {
        'page_title': page_title,
        'outMessage': logoutMessage, 'invalid': True})

from django.shortcuts import render, get_object_or_404, redirect
from django.utils.http import is_safe_url, urlsafe_base64_encode
from django.conf import settings as conf_settings
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse

""" IF USER IS LOGIN IT WILL DIRECTLY REDIRECT TO USER DDASHBOARD ELSE TO LOGIN PAGE"""
def dashBoardView(request):
    nextUrl = request.GET.get('next', )
    if request.user.is_authenticated and not request.user.is_staff:
        print('request.user.role',  request.user.role.role, str(request.user.role) == 'vendor')
        if request.user.role.role == 'vendor':
            return render(request, 'vendor_dashboard.html')
        elif request.user.role.role == 'user':
            return render(request, 'customer_dashboard.html')
        else:
            return HttpResponse('<h4 class="text-center">Please register as user or vendor</h4>')
    else:
        return render(request, 'login.html', {'nextUrl': nextUrl})


def register(request):
    return render(request, 'register.html')


def cart(request):
    return render(request, 'cart.html')



# LOGIN SUBMIT
def loginSubmit(request):
    if request.method == "POST":
        email = request.POST.get('email', )
        password = request.POST.get('password', )

        # next url for user to redirect directly after login
        nextUrl = request.POST.get('nextUrl', )

        url_is_safe = is_safe_url(
            url=nextUrl,
            allowed_hosts=conf_settings.ALLOWED_HOSTS,
            require_https=request.is_secure(),
        )

        if email and password:
            user = authenticate(username=email, password=password)
            if user is not None:
                if not user.is_staff:
                    login(request, user)
                    if nextUrl != 'None' and url_is_safe:
                        return redirect(nextUrl)
                    else:
                        return redirect('login')
                else:
                    return render(request, 'login.html', {'error': "Invalid Login Username or Password"})
            else:
                return render(request, 'login.html', {'error': "Invalid Login Username or Password"})
    else:
        return redirect('login')


# END LOGIN SUBMIT


# LOGOUT
def LogoutView(request):
    logout(request)
    return redirect('login')
# END LOGOUT
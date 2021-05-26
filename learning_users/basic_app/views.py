from django.shortcuts import redirect, render
from basic_app.forms  import UserForm,UserProfileForm

from django.contrib.auth import login, logout,authenticate
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required 

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')



# def login_form(request):
#     return render(request,'basic_app/login.html')





def registration(request):
    registered  = False
    if request.method =='POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'basic_app/registration.html',
    {
        "user_form" : user_form,
        "profile_form":profile_form,
        "registered":registered,

    })
# return render(request,'basic_app/registration.html')



def user_login(request):
    hello = True
    logged = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password=password)
        if user:
            if user.is_active :
                login(request,user)
                logged = True
                return HttpResponseRedirect(reverse('index'),{"logged":logged})
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            hello = False
            return HttpResponse("Wrong Credentials")
    else:
         return render(request,'basic_app/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
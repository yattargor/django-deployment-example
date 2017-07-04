from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

#out login_required decorator to assume that users that made request to logout is already logging ing
@login_required
def user_logout(request):
    logout(request)   #pass logut request
    return HttpResponseRedirect(reverse('index')) #after return to index page

def register(request):
    #set registered to False so after made this following at the end save
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        #check if form insertion is valid or not
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()             #grab userform and save in db
            user.set_password(user.password)    #hash della pw
            user.save() #save pw in db

            #Method for upload various files not only this type based on key for example in this case 'profile_pic' define in model
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES :
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html',
                            {'user_form':user_form,
                             'profile_form':profile_form,
                             'registered': registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username') #use 'get' because in <input> text in login.html is POST request so i can 'get' username
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) #this line authenticate automatically user for you

        if user:                        #check if there is a user
            if user.is_active:          #check if account is active
                login(request, user)    #log user in
                return HttpResponseRedirect(reverse('index')) #after succesfully login redirect to homepage

            else:
                return HttpResponse("ACCOUNT NO ACTIVE")
        else: #if user not present print on console credentials of user that try to made login
            print("Someone tried to login and failed!")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request,'basic_app/login.html',{})

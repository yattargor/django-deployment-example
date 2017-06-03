from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from . import forms
# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    users_dict = { 'users': user_list } #reference from particular html page with this django tag es. 'users' in this case
    return render(request, 'AppTwo/users.html', context = users_dict)

def userform(request):
    form = forms.MyUserForm()

    if request.method == 'POST':
        form = forms.MyUserForm(request.POST)
        if form.is_valid():
            myuserform = form.save(commit=True)
            return index(request)
        else:
            print('Error Form Invalid')

    return render(request, 'AppTwo/userform.html',{'form': form})

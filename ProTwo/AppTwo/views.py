from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    users_dict = { 'users': user_list } #reference from particular html page with this django tag es. 'users' in this case
    return render(request, 'AppTwo/users.html', context = users_dict)

from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName() #instance della FormName class here

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid(): #validation routines for all fields
            #DO SOMETHING CODE
            print("VALIDATION SUCCESS")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("COMMENT: " + form.cleaned_data['text'])

    return render(request, 'basicapp/form_page.html', {'form': form})

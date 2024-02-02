from django.shortcuts import render, redirect
from . import forms
from datetime import datetime

# Create your views here.
def home(request):
    form = forms.UserData();
    time = datetime.now()
    if request.method == "POST":
        form = forms.UserData(request.POST)
        if form.is_valid():
            request.session['first_name'] = form.cleaned_data['First_Name']
            request.session['last_name'] = form.cleaned_data['Last_Name']
            request.session['email'] = form.cleaned_data['Email']
            return redirect(info)
    return render(request, 'myapp/index.html', {'form':form, 'time':time})

def info(request):
    fname = request.session.get('first_name')
    lname = request.session.get('last_name')
    email = request.session.get('email')
    context = {'fname':fname, 'lname':lname, 'email':email}
    return render(request, 'myapp/info.html', context=context)
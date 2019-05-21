from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['Password1']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/signup/')
        else:
            return render(request, 'login.html',{'error' : 'username or password is incorrect'})
    else:
        return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['Password2'] == request.POST['Password1']:
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['Password1'])
            auth.login(request,user)
            return redirect('/home/')
    return render(request,'signup.html')
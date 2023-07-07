from django.shortcuts import render, redirect
from django.http import HttpResponse
# importing a django inbuilt library to post user details into the database
from django.contrib.auth.models import User
# to show/output a message that the user has successfully registered or all such messages, we can import an inbuilt library
from django.contrib import messages

# Create your views here.
def home(request):
     return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save() 
        messages.success(request, "registered successfully")

        # after creating and storing the user in the database, we need to redirect to the login page
        return redirect('signin')
    return render(request, "authentication/signup.html")

def signin(request):
    return render(request, "authentication/signin.html")

def signout(request):
    pass
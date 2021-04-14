from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

#APIs
def home(request):
    
    return render(request, 'home/home.html')
    # return HttpResponse('This is home')

def aboutme(request):
    return render(request, 'home/About.html')
    #return HttpResponse('This is Aboutme')
    
#def projects(request):
    #return render(request, 'home/Project.html')
    #return HttpResponse('This are my projects')
    
def portfolio(request):
    return render(request, 'home/Portfolio.html')
    #return HttpResponse('This is my portfolio')
    
def contactme(request):
 
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        more = request.POST['more']
        print(name, email, phone, age, more)


        if len(name)<2 or len(email)<3 or len(phone)<10 or len(more)<4:
            messages.error(request, "Please fill your form correctly.")
        else:
            contact = Contact(name=name, email=email, phone=phone, age=age, more=more)
            contact.save()
            messages.success(request, "Your form is successfully submitted.")
    return render(request, 'home/contact.html')
    #return HttpResponse('This is my contact page')



#APIs
def signup(request):
    if request.method=='POST':
        #Get the post
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        confpassword=request.POST['confpassword']

        # Check for errorneous inputs
        
        #Username should be of 10 characters
        if len(username) > 10:
            messages.error(request, 'Username must not be under 10 characters')
            return redirect('home')

        #username should be alphanumeric
        if not username.isalnum():
            messages.error(request, 'Username must not contain any special character')
            return redirect('home')

        # Password should be same
        if password!=confpassword:
            messages.add_message(request, messages.ERROR, 'Passwords do not match')
            return redirect('home')
        
        #Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Your Inomotive account has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')

def Login(request):
    
    if request.method == 'POST':
        #Get the post
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        
        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please try again")
            return redirect('home')

    return HttpResponse('404 Not Found')

def Logout(request):
    logout(request)
    messages.success(request, "Succesfully logged Out")
    return redirect('home')



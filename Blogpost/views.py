from django.shortcuts import render , HttpResponseRedirect ,HttpResponse
# from dajngo.http import 

from .models import post  
from .forms import Signup ,SigninUser
from django.contrib import messages
from django.contrib.auth import authenticate , login  
from django.contrib.auth.models import Group
from django.contrib.auth import logout as Blog_out
from .forms import create_post 
from django.core.cache import cache 
# Create your views here.




def home(request):
    b = post.objects.all().order_by("-id")
    return render( request ,'Blogpost/home.html' , {'b' : b })


def about(request):
    return render(request , 'Blogpost/about.html')

def contact(request):
    return render(request , 'Blogpost/contact.html')

def dashboard(request):
    if request.user.is_authenticated:
        b = post.objects.all().order_by("-id")
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all() # getting model of group which user have 
        # cache for login count 
        ct = cache.get('count' , version=user.pk)

        return render(request , 'Blogpost/dashboard.html' ,{'datas' : b , 'user' : user , 'fname' : full_name , 'groups' : gps , 'ct':ct})
    else:
        return HttpResponseRedirect("/singin/")




# detail view post 


def detail_blog(request , id):
    print(request.user)
    data = post.objects.get(id=id)
    return render(request , 'Blogpost/visitblog.html' , {'datas' : data})





# create - post 

def createPost(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form=create_post(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request , "Post Added SuccessFully !! ")
                return  HttpResponseRedirect("/dashboard/")
        else:
            form = create_post()
        return render(request , 'Blogpost/crud_post/create_post.html' , {'form' : form})
    else:
        return HttpResponseRedirect("/")
#--------------------------------------------------update-----------------



def update_post(request , id):
    if request.user.is_authenticated:
        instance = post.objects.get(id=id)
        if request.method == "POST":
            form = create_post(request.POST , instance=instance)
            if form.is_valid():
                form.save()
                messages.success(request , f"you { instance.title} Post  is Updated SuccessFully  !! ")
                return HttpResponseRedirect("/dashboard/")
        else:
            form = create_post(initial={'title' : instance.title , 
            'desc' : instance.desc })
        return render(request , 'Blogpost/crud_post/update_post.html' , {'form' : form } )
    else:
        return HttpReponseRedirect("/")


# delete post 


def delete_post(request , id):
    if request.user.is_authenticated:

        if request.method=="POST":
            i = post.objects.get(id=id)
            i.delete()
           
            messages.success(request , f" You are Post is  SuccessFully !! {request.user.username}")
            return HttpResponseRedirect("/dashboard/")
        else:
            return HttpResponseRedirect("/")

    else:
        return HttpResponseRedirect("singin/")
    # login ------------------------------------------------------------------------

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SigninUser(request=request , data=request.POST)
            if form.is_valid():
                uname = request.POST.get('username')
                upass = request.POST.get('password')
                print(uname , upass)
                user = authenticate(username=uname , password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request , "Logged in Successfully !!")
                    return HttpResponseRedirect('/dashboard/')
            
        else:
            form = SigninUser()

        return render(request , 'Blogpost/login.html' , {'form' : form})

    else:
        return HttpResponseRedirect("/dashboard/")
#------------------------------------------------------------------------------------

def logout(request):
    if request.user.is_authenticated:
        Blog_out(request)
        messages.success(request , 'Logout successfully')
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/singin/")

def register(request):
    if request.method == 'POST':
        form = Signup(request.POST)
        if form.is_valid():
            messages.success(request , 'congrulation  !!  you are becoming authore.')
            user = form.save()
            # givving permission 
            group = Group.objects.get(name="Authore")
            user.groups.add(group)
            # u = request.POST.get('username')
            # pw = request.POST.get('password')
            # em = request.POST.get('email')
            # fn = request.POST.get('first_name')
            # ln = request.POST.get('lastname')
            # print(u , pw , em,fn , ln)
            return  HttpResponseRedirect('/signup/')
            # user = form.cleaned_data.get['username']
            # password = form.cleaned_data.get['password']
            # print(user , password )
    else:
        form = Signup()

    return render(request , 'Blogpost/signup.html' , {'form' : form})


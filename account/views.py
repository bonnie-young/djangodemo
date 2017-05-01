# Create your views here.
from .models import User, UserForm
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone


def index(request):
    template = "account/index.html"
    login = User()
    context = {'login': login}
    return render(request, template, context)


def login(request):
    form_name = request.POST.get("name")
    form_password = request.POST.get("password")
    try:
        user_obj = User.objects.get(name=form_name)
        request.session['user_id'] = user_obj.id
    except:
        context = {"error_message": "User does not exist!"}
        return render(request, "account/index.html", context)
    if form_name == "" or form_password == "":
        context = {"error_message": "Please enter your name and password!"}
        return render(request, "account/index.html", context)
    if form_password == user_obj.password and user_obj.role == 1:
        return HttpResponseRedirect('/account/userlist')
    elif form_password == user_obj.password and user_obj.role == 2:
        return HttpResponseRedirect(reverse('account:userprofile', args=(user_obj.id,)))
    else:
        context = {"error_message": "Password is wrong, please try again.", "name" : user_obj.name}
        return render(request, "account/index.html", context)

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    context = {"error_message" : "You are logged out"}
    return render(request, 'account/index.html', context)

def register(request):
    return render(request, 'account/register.html', {})

def userlist(request):
    userlist = User.objects.all().order_by("-id")
    return render(request, "account/userlist.html", {'userlist': userlist})

def adduser(request):
    print(timezone.now())
    return render(request, "account/adduser.html", {"createtime": timezone.now(), "updatetime":timezone.now()})

def userdetail(request, user_id):
    user_obj = User.objects.get(pk=user_id)
    return render(request, "account/userdetail.html", {"user_obj": user_obj})

def saveuser(request):
    #XXX
    f = UserForm(request.POST)
    f.save()
    userlist = User.objects.all().order_by("-id")
    return render(request, "account/userlist.html", {"userlist": userlist})

def updateuser(request, user_id):
    user_obj = User.objects.get(pk=user_id)
    return render(request, "account/updateuser.html", {"user_obj": user_obj, "updatetime": timezone.now()})

def saveupdateuser(request, user_id):
    a = User.objects.get(pk=user_id)
    f = UserForm(request.POST, instance=a)
    f.save()
    userlist = User.objects.all().order_by("-id")
#    return HttpResponseRedirect(reverse('account:userlist', args=(userlist,)))
    return render(request, "account/userlist.html", {"userlist": userlist})

def userprofile(request, user_id):
    user_obj = User.objects.get(pk=user_id)
    return render(request, "account/userprofile.html", {"user_obj": user_obj})

def deluser(request, user_id):
    User.objects.get(pk=user_id).delete()
    userlist = User.objects.all().order_by("-id")
    return render(request, "account/userlist.html", {"userlist": userlist})


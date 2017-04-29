# Create your views here.
from .models import User
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect


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
        context = {"error_message": "User does not exist, Please register your account first."}
        return render(request, "account/register.html", context)
    if form_password == user_obj.password and user_obj.role == 1:
        return HttpResponseRedirect('/account/userlist')
    elif form_password == user_obj.password and user_obj.role == 2:
        return HttpResponseRedirect(reverse('account:userpofile', args=(user_obj.id)))
    else:
        context = {"error_message": "Password is wrong, please try again.", "name" : user_obj.name}
        return render(request, "account/index.html", context)

def register(request):
    pass

def userlist(request):
    userlist = User.objects.all()
    return render(request, "account/userlist.html", {'userlist': userlist})
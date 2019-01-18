from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_protect
def register(request):
 if request.method == 'POST':
  form = RegistrationForm(request.POST)
  if form.is_valid():
   user = User.objects.create_user(
   username=form.cleaned_data['username'],
   password=form.cleaned_data['password1'],
   email=form.cleaned_data['email']
   )
   return HttpResponseRedirect('/register/success/')
 else:
  form = RegistrationForm()
 variables = {
 'form': form
 }

 return render(request, 'registration/register.html',
 variables
 )

@csrf_exempt
def onlineUsers(request):
 userOnline = []
 for user in request.online_now:
    userOnline.append(user)
    userOnline.append('<br>')
 return HttpResponse(userOnline)
    

def register_success(request):
 return render_to_response(
 'registration/success.html',
 )

def logout_page(request):
 logout(request)
 return HttpResponseRedirect('/')

@login_required
def home(request):
 return render_to_response(
 'home.html',
 { 'user': request.user , 'onlineusers':request}
 )
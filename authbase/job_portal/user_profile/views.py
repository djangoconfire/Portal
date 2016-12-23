
from django.shortcuts import render,render_to_response,redirect,get_object_or_404
from django.template import RequestContext
from job.models import *
from company.models import *
from user_profile.models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse , HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from user_profile.models import UserProfile
from user_profile.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings





def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'account/signup.html', {'form': form})

        else: 
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            djangouser = User(username=username)
            djangouser.set_password(password)
            djangouser.email = email 
            try:
                djangouser.save()
            except Exception as e:
                form = SignUpForm()
                return render(request,'account/signup.html',{'form':form})

            new_user=UserProfile()
            user = authenticate(username=username, password=password)
            ## user has been added to the current session
            new_user.user = djangouser
            new_user.save()
                    
            login(request, user)

            return redirect('/accounts/login/')
    else:
        return render(request, 'account/signup.html', {'form': SignUpForm()})


@login_required
def user_profile(request,username):
    if request.user.is_authenticated():
        try:
            user=UserProfile.objects.get(user=request.user) 
            print user
            print '############' 
            job_applications=JobApplications.objects.filter(jobseeker=user)
            print job_applications

            return render(request,'user_profile/dashboard.html',{'job_applications':job_applications}) 
 
        except UserProfile.DoesNotExist:
            message="UserProfile does not exist"
            return render_to_response('500.html',{'error':message},context_instance = RequestContext(request))  
    else:
    	return HttpResponse('User is not authenticated')    




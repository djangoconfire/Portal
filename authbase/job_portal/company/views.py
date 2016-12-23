from django.shortcuts import render,render_to_response,get_object_or_404
from models import Company
from django.template import RequestContext

# Create your views here.


def CompanyProfile(request,company_slug):
  company=get_object_or_404(Company,slug=company_slug)
  return render_to_response('company/profile.html',{'instance':company},context_instance=RequestContext(request))
    



from django.conf.urls import url,include
from views import *
urlpatterns=[
	
	   
	   url(r'^(?P<company_slug>[-\w]+)/$',CompanyProfile,name="company_profile"),


    ]

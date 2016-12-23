from django.conf.urls import url,include

from views import *

urlpatterns=[
			
	    url(r'^sign_up/$',signup,name="signup"),      
        url(r'^(?P<username>.*)$',user_profile,name="logged_in_user"),
        
        

    ]


from django.conf.urls import url,include
from views import *
urlpatterns=[
	
	   url(r'^$',Home, name='home'),
	   url(r'^search/$',search, name='search'),
	   url(r'^apply_for_job/$',Apply_for_job, name='apply_for_job'),
	   url(r'^(?P<company_slug>[-\w]+)/(?P<job_slug>[-\w]+)/job_detail/$',JobDetail,name="job_detail"),
	   url(r'^posting_new_job/$',PostingNewJob,name="posting_new_job"),

	
    ]

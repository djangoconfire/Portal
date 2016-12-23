"""job_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from .  import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^job/',include('job.urls',namespace="job")),
    url(r'^user/',include('user_profile.urls',namespace="user_profile")),
    url(r'^company/',include('company.urls',namespace="company")),

    # login and logout views here
    url(r'^accounts/login/', views.user_login, name='login'),
    url(r'^accounts/logout/', views.user_logout, name='logout'),

    url(r'^taggit_suggest/', include('taggit_autosuggest.urls')),

    url(r'^ajax/add_designation/$','designation.views.AddingNewDesignation',name="new_designation"),
    url(r'^ajax/add_city/$','location.views.AddingNewCity',name="new_city"),


    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

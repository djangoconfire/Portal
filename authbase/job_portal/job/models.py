from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.core.exceptions import ValidationError
from user_profile.models import UserProfile 
from company.models import Company
from django.utils.translation import ugettext_lazy as _
from taggit_autosuggest.managers import TaggableManager
from autoslug import AutoSlugField
from django.utils import timezone
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import markdown
from taggit.models import Tag

class JobListing(models.Model) : 
    
    JOB_TYPE_CHOICES = (
            ('fulltime','Full Time'),
            ('contract','Contract'),
            ('intern','Intern'),
            ('freelance','Freelance'),
            ('parttime','Part Time')
    )
    
    EXP_CHOICES=[(int(item),int(item)) for item in range(1,20)]

    JOB_CTC_CHOICE=[(item,item) for item in range(1,20)]




    company                      = models.ForeignKey(Company,null=True,help_text="<strong>Select Company from dropdown")
    job_title                    = models.CharField(max_length=100,null=True,blank=True)
    slug                         = AutoSlugField( populate_from="job_title",unique=True)
    
     
    
    job_type                     = models.CharField(max_length = 10, blank  = True, null = True, 
                                   choices = JOB_TYPE_CHOICES, help_text = '<strong>Select Type of job </strong>')
    job_desc                     = models.TextField()
    job_min_ctc                  = models.IntegerField(choices=JOB_CTC_CHOICE,null = True)
    job_max_ctc                  = models.IntegerField(choices=JOB_CTC_CHOICE,null = True)
    job_min_exp                  = models.IntegerField(choices=EXP_CHOICES)
    job_max_exp                  = models.IntegerField(choices=EXP_CHOICES)
    job_location                 = models.CharField(max_length=100,blank=True,null=True)
    job_skills                   = models.CharField(max_length=200,null=True,blank=True)
    pub_date                     = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    last_updated_date            = models.DateTimeField(auto_now=True,blank=True,null=True)
    job_no_of_applications       = models.IntegerField(default=0,blank=True)

       

    def __str__(self):
        return "%s " %(self.job_title)

        
    class Meta : 
        ordering = ['-job_min_ctc']


    def get_absolute_url(self):
        return reverse('job:job_detail',kwargs={ "company_slug": self.company.slug, "job_slug": self.slug})


class JobApplications(models.Model) :
    

    COMPANY_ACTION = (
            ('rejected','Rejected'),
            ('shortlisted','Shortlisted'),
            ('waiting','Put on Hold'),
            )


    jobseeker               = models.ForeignKey(UserProfile,null=True, blank=True)
    job                     = models.ForeignKey(JobListing,null=True, blank=True)
    action_by_company	    = models.CharField(max_length = 20, blank = True, null = True, choices = COMPANY_ACTION)
    is_shortlisted          = models.NullBooleanField(blank=True,null=True)
    is_rejected             = models.NullBooleanField(blank=True,null=True)


    def get_company_action(self) : 
        if not self.action_by_company : 
            return None 
        action_short_name = ['rejected','shortlisted','waiting']
        action_large_name = ['Rejected','Shortlisted','Put on Hold']
        return action_large_name[action_short_name.index(self.action_by_company)]

 





        









        



  




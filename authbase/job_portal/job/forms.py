from django import forms
from models import JobListing

class JobListingForm(forms.ModelForm):
   class Meta:
      model=JobListing
      fields=['job_skills','job_location','job_min_exp','job_max_exp','job_min_ctc','job_max_ctc']

      labels={
         'job_skills':'Skill',
         'job_location':'Location',
         'job_min_exp':'Min Exp.',
         'job_max_exp':'Max Exp.',
         'job_min_ctc':'Min CTC',
         'job_max_ctc':'Max CTC',
      }


   # def __init__(self, *args, **kwargs):
   #    super(JobListingForm,self).__init__(*args,**kwargs)
   #    for fieldname in ['job_skills']:
   #          self.fields[fieldname].help_text = 'Enter your Skills'
      
class JobCreatingForm(forms.ModelForm):
   class Meta:
      model=JobListing
      exclude=['job_no_of_applications']

      # labels={
      #    'job_skills':'Skill',
      #    'job_location':'Location',
      #    'job_min_exp':'Min Exp.',
      #    'job_max_exp':'Max Exp.',
      #    'job_min_ctc':'Min CTC',
      #    'job_max_ctc':'Max CTC',
      # }
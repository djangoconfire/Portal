from django.shortcuts import render,render_to_response,get_object_or_404
from django.template import RequestContext
from forms import JobListingForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponseRedirect
import json
import traceback
from models import JobListing,JobApplications
from forms import JobListingForm,JobCreatingForm
from django.contrib.auth.decorators import login_required

# Create your views here.

## utility functions...
def intersect_list(a,b):
    return list(set(a) & set(b))

def union_list(a,b):
    return list(set(a) | set(b))



def Home(request):
    print 'inside function'
    form=JobListingForm()
    return render_to_response('job/home.html',{'form':form},context_instance=RequestContext(request))



@csrf_exempt
def search(request):
    print 'inside search'
    form_data=request.POST.get('form_data','')
    form_data=json.loads(form_data)

    job_list =JobListing.objects.all()
    query_list=[job for job in job_list]

    for i in range(len(form_data)):
        current_dict = form_data[i]
        print current_dict


        if current_dict['name'] == 'job_min_exp':
            list_of_min_exp=current_dict['value'].split(',')
            for k in range(len(list_of_min_exp)):
                exp_id=list_of_min_exp[k]
                if exp_id != '' and exp_id != None:
                    try:
                        JobListings = JobListing.objects.filter(job_min_exp__gte=int(exp_id))
                        query_list=intersect_list(query_list,list(JobListings))
                        print query_list
                    except Exception as e:
                        print e
                        traceback.print_exc()
                    

        

        if current_dict['name'] == 'job_max_exp':
            list_of_max_exp=current_dict['value'].split(',')
            for k in range(len(list_of_max_exp)):
                exp_id=list_of_max_exp[k]
                if exp_id != '' and exp_id != None:
                    try:
                        JobListings = JobListing.objects.filter(job_max_exp__lte=int(exp_id))
                        query_list=intersect_list(query_list,list(JobListings)) 
                    except Exception as e:
                        print e
                        traceback.print_exc()
                   


        if current_dict['name'] == 'job_min_ctc':
            list_of_min_ctc=current_dict['value'].split(',')
            for k in range(len(list_of_min_ctc)):
                ctc_id=list_of_min_ctc[k]
                if ctc_id != '' and ctc_id != None:
                    try:
                        JobListings = JobListing.objects.filter(job_min_ctc__gte=int(ctc_id))
                        query_list=intersect_list(query_list,list(JobListings)) 
                    except Exception as e:
                        print e
                        traceback.print_exc()
                    # query_list=intersect_list(query_list,list(JobListings)) 

        if current_dict['name'] == 'job_max_ctc':
            list_of_max_ctc=current_dict['value'].split(',')
            for k in range(len(list_of_max_ctc)):
                ctc_id=list_of_max_ctc[k]
                if ctc_id != '' and ctc_id != None:
                    try:
                        JobListings = JobListing.objects.filter(job_max_ctc__lte=int(ctc_id))
                        query_list=intersect_list(query_list,list(JobListings)) 
                    except Exception as e:
                        print e
                        traceback.print_exc()
                    # query_list=intersect_list(query_list,list(JobListings))
            

        if current_dict['name'] == 'job_location':
            list_of_location=current_dict['value'].split(',')
            for k in range(len(list_of_location)):
                location_id=list_of_location[k]
                if location_id != '' and location_id != None:
                    try:
                        JobListings = JobListing.objects.filter(job_location=str(location_id).lower())
                        query_list=intersect_list(query_list,list(JobListings))     
                        print query_list

                    except Exception as e:
                        print e
                        traceback.print_exc()
                   
                    # query_list=intersect_list(query_list,list(JobListings))
                     
             
        
        if current_dict['name'] == 'job_skills':
            list_of_skill=current_dict['value'].split(',')
            for k in range(len(list_of_skill)):
                skill_id=list_of_skill[k]
                print skill_id
                if skill_id != '' and skill_id != None:
                    try:
                        JobListings = JobListing.objects.filter(job_skills=str(skill_id).lower())  
                        query_list=intersect_list(query_list,list(JobListings)) 
                        print query_list

                    except Exception as e:
                        print e
                        traceback.print_exc()
                    # query_list=intersect_list(query_list,list(JobListings)) 
          

                        
 
    list_of_matching_profiles = []
    print query_list
    for job_item in query_list:
        if job_item.job_location != None:
            location_name=job_item.job_location
        else:
            location_name = 'Not Specified'   

        if job_item.company != None:
            company_name=job_item.company.company_name
            print company_name
        else:
            company_name = 'Not Specified'     


        list_of_matching_profiles.append([job_item.job_title,job_item.job_type,\
                                            company_name,job_item.job_min_exp,\
                                            job_item.job_max_exp,location_name,\
                                            job_item.job_skills,\
                                            job_item.job_desc,job_item.company.company_logo.url,\
                                            job_item.slug,job_item.company.slug,\
                                            job_item.get_absolute_url()
                                            ])
    print list_of_matching_profiles   
    return JsonResponse(list_of_matching_profiles,safe=False)





def JobDetail(request,company_slug,job_slug):
    job=get_object_or_404(JobListing,slug=job_slug)
    form=JobListingForm(instance=job)
    application=get_object_or_404(JobApplications,job=job)
    application_id=application.id
    return render(request,'job/job_detail.html',{'application_id':application_id,'application':application,'form':form})    


@csrf_exempt
@login_required
def Apply_for_job(request):
    print 'inside apply_for_job'
    if request.method=='POST':
        id = request.POST.get('id',0)
        print '\n\n\n'
        print id
        print '\n\n\n'
    try:
        application=JobApplications.objects.get(id=id)
        print '\n\n\n'
        print application.jobseeker.user.username
        print '\n\n\n'
    except Exception as e:
        ##message="Job Application does not exit"
        return JsonResponse({'success':'False','exception': e})
       
    application.jobseeker.is_applied=True
    application.jobseeker.user=request.user
    
    try:
        application.jobseeker.save()
        return JsonResponse({'success':'True'})
    except Exception as e:
        return JsonResponse({'success':'False','exception':e})
    return JsonResponse({'success':'False'})



@login_required
def PostingNewJob(request):
    if request.method=="POST":
        form=JobCreatingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/' + request.user.username)
    else:
        form=JobCreatingForm()
    return render_to_response('job/posting_job.html',{'form':form},context_instance=RequestContext(request))
 


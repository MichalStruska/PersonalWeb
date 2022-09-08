from .models import ProfileSingle

def basic_info_process(request):
    user_info = ProfileSingle.objects.get(user_name="Michal Struska")
    
    context={
        'facebook_link':user_info.facebook_link,
        'twitter_link':user_info.twitter_link,
        'github_link':user_info.github_link,
        'instagram_link':user_info.instagram_link,
        'researchgate_link':user_info.researchgate_link,
        'orcid_link':user_info.orcid_link,
        'linkedin_link':user_info.linkedin_link,
        'email':user_info.email,
        'department_link':user_info.department_link,
        'laboratory_link':user_info.laboratory_link,
    }
    return context


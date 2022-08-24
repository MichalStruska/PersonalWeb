from .models import ProfileSingle

def basic_info_process(request):
    user_info = ProfileSingle.objects.get(user_name="Michal Struska")
    
    context={
        'facebook_link':user_info.facebook_link,
        'twitter_link':user_info.twitter_link,
        'github_link':user_info.github_link,
        'instagram_link':user_info.instagram_link,
        'department_link':user_info.department_link,
        'laboratory_link':user_info.laboratory_link,  
    }
    return context


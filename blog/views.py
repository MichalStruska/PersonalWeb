from cProfile import Profile
from django.shortcuts import render
from django.views import generic
from .models import Category, ProfileSingle, Publication


class SingleProfileView(generic.DetailView):
    model = ProfileSingle
 
def about(request):

    # my_data = ProfileSingle.objects.get(pk=1).bio #for all the records 
    user_object = ProfileSingle.objects.get(user_name="Michal Struska")
    bio = user_object.bio
    profile_image = user_object.profile_image

    context={
       
      'bio':bio,
      'profile_image':profile_image,
    
    } 

    return render(request, 'blog/about.html', context)

class PublicationList(generic.ListView):
    model = Publication
    
    template_name = 'blog/publications_list.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        publication_list = Publication.objects.all()
        context = super(PublicationList, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context["publication_list"] = publication_list
        return context

class PublicationDetail(generic.DetailView):
    model = Publication
    template_name = 'blog/publication_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        
        pub = Publication.objects.get(id=self.kwargs['pk'])
        context = super(PublicationDetail, self).get_context_data(*args, **kwargs)
        context["title"] = pub.title
        context["author"] = pub.author
        context["description"] = pub.description
        return context

def splash(request):
    return render(request, 'blog/splash.html')

def base(request):
    user_object = ProfileSingle.objects.get(user_name="Michal Struska")
    
    context={
       
        'facebook_link':user_object.facebook_link,
        'twitter_link':user_object.twitter_link,
        'github_link':user_object.github_link,
        'instagram_link':user_object.instagram_link,
        'department_link':user_object.department_link,
        'laboratory_link':user_object.laboratory_link,
    } 

    return render(request, 'blog/base.html', context)



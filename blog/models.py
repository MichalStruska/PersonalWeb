from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True, blank=True)
    #slug = models.SlugField(max_length=200, unique=True)
    #title_tag = models.CharField(max_length=255, default="Dept")
    #slug = AutoSlugField(populate_from=['title'])
    author = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now= True, null=True, blank=True)
    #content = models.TextField()
    content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=1, null=True, blank=True)
    article_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    thumbnail_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    category = models.CharField(max_length=255, default="News", null=True, blank=True)
    snippet = models.CharField(max_length=255, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-home')
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(null = True, blank = True, upload_to = "images/profile/")
    bio = models.TextField(max_length=500, null=True, blank=True)
    facebook_link = models.CharField(max_length=255, null=True, blank=True)
    twitter_link = models.CharField(max_length=255, null=True, blank=True)
    instagram_link = models.CharField(max_length=255, null=True, blank=True)
    website_link = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=30,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog-home')

    def __str__(self):
        return self.user.username



class ProfileSingle(models.Model):
    user_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(null = True, blank = True, upload_to = "images/profile/")
    bio = models.TextField(max_length=500, null=True, blank=True)
    facebook_link = models.CharField(max_length=255, null=True, blank=True)
    twitter_link = models.CharField(max_length=255, null=True, blank=True)
    instagram_link = models.CharField(max_length=255, null=True, blank=True)
    website_link = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=30,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog-home')

class Publication(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    snippet = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(null = True, blank = True, upload_to = "images/publication/")
    link = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('blog-home')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, null=True, blank=True)
    #slug = AutoSlugField(populate_from=['name'])

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog-home')

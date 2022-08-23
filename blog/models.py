from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from tinymce.models import HTMLField
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

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

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('blog-home')

class Publication(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    snippet = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(null = True, blank = True, upload_to = "images/publication/")
    link = models.CharField(max_length=255, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    pages = models.CharField(max_length=255, null=True, blank=True)
    journal = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['-publication_date']
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

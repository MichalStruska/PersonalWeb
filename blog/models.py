from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse

AUTHOR_RANK = (
    (0,"First author"),
    (1,"Coauthor")
)

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

PROJECT_CATEGORY = (
    (0,"Profesional project"),
    (1,"Personal project")
)

PROJECT_PROGRESS = (
        ("In progress", "In progress"),
        ("Finished", "Finished")
    )

PUBLICATION_PROGRESS = (
    ("In review", "In review"),
    ("In press","In press"),
    ("Published","Published")
    )


class ProfileSingle(models.Model):
    user_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(null = True, blank = True, upload_to = "images/profile/")
    bio = models.TextField(null=True, blank=True)
    facebook_link = models.CharField(max_length=255, null=True, blank=True)
    twitter_link = models.CharField(max_length=255, null=True, blank=True)
    instagram_link = models.CharField(max_length=255, null=True, blank=True)
    github_link = models.CharField(max_length=255, null=True, blank=True)
    researchgate_link = models.CharField(max_length=255, null=True, blank=True)
    linkedin_link = models.CharField(max_length=255, null=True, blank=True)
    orcid_link = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    department_link = models.CharField(max_length=255, null=True, blank=True)
    laboratory_link = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=30,null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse('blog-home')

class Publication(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    author_rank = models.IntegerField(choices=AUTHOR_RANK, default=0)
    description = models.TextField(null=True, blank=True)
    snippet = models.TextField(null=True, blank=True)
    image = models.ImageField(null = True, blank = True, upload_to = "images/publication/")
    link = models.CharField(max_length=255, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    pages = models.CharField(max_length=255, null=True, blank=True)
    journal = models.CharField(max_length=255, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    progress = models.CharField(max_length=255,choices=PUBLICATION_PROGRESS, default=0)

    class Meta:
        ordering = ['author_rank', 'progress', '-publication_date']
    def get_absolute_url(self):
        return reverse('blog-home')

    def __str__(self):
        return self.title

class ProjectType(models.Model):
    name = models.CharField(max_length=100, default='Miscellaneous', primary_key = True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    thumbnail_image = models.ImageField(null = True, blank = True, upload_to = "images/project/")
    link = models.CharField(max_length=255, null=True, blank=True)
    date_of_addition = models.DateField(null=True, blank=True)
    category = models.IntegerField(choices=PROJECT_CATEGORY, default=0)
    status = models.IntegerField(choices=STATUS, default=0)
    type = models.CharField(max_length=255, null=True, blank=True)
    progress = models.CharField(max_length=255,choices=PROJECT_PROGRESS, default=0)

    class Meta:
        ordering = ['category', 'progress', '-date_of_addition']
    def get_absolute_url(self):
        return reverse('blog-home')

    def __str__(self):
        return self.title




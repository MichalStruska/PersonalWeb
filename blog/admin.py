from django.contrib import admin
from .models import ProjectType, ProfileSingle, Project, Publication
from django_summernote.admin import SummernoteModelAdmin

class PublicationAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    list_display = ('title','author', 'publication_date','progress')
    ordering = ['-publication_date']

class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    list_display = ('title','date_of_addition','progress')
    ordering = ['category', '-date_of_addition']

admin.site.register(ProjectType)
admin.site.register(ProfileSingle)
admin.site.register(Publication,PublicationAdmin)
admin.site.register(Project,ProjectAdmin)

from django.contrib import admin
from .models import Category, ProfileSingle, Publication
from django_summernote.admin import SummernoteModelAdmin

class PublicationAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')
    list_display = ('title','author', 'publication_date')
    ordering = ['-publication_date']

admin.site.register(Category)
admin.site.register(ProfileSingle)
admin.site.register(Publication,PublicationAdmin)

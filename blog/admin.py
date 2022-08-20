from django.contrib import admin
from .models import Post, Category, Profile, ProfileSingle, Publication

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    #prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(ProfileSingle)
admin.site.register(Publication)

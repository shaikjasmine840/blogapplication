from django.contrib import admin
from blogapp.models import Tag,BlogPost,Comment
# Register your models here.
admin.site.register(Tag)
admin.site.register(BlogPost) 
admin.site.register (Comment)

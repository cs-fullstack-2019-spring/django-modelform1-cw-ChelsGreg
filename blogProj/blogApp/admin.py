from django.contrib import admin

# Register your models here.
from .models import BlogPost
# FOR INFO TO SHOW ON SITE
admin.site.register(BlogPost)


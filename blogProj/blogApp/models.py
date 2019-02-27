from django.db import models
from django.utils import timezone

# Create your models here.
# BLOG MODEL
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

# FOR TITLE TO DISPLAY ON SITE
    def __str__(self):
        return f'{self.title}'

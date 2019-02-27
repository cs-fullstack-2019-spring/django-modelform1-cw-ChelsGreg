from django import forms
from .models import BlogPost

# FORM TO LINK MODEL INFO TO FORM
class BlogForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ['title', 'text']
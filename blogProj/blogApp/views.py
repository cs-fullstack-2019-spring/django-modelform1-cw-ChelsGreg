from django.shortcuts import render
from .forms import BlogForm
from django.http import HttpResponse

# Create your views here.

# JUST A PAGE TO LINK FROM BLOG FORM SUBMIT
def index(request):

    return render(request, 'blogApp/index.html')


# FUNCTION FOR FORM TO SAVE SUBMITTED DATA/FOR FORM DATA TO DISPLAY ON HTML
def blogform(request):
    blog_form = BlogForm()

    if request.method == "POST":
        print("it posted")
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            # SAVES FORM SUBMITTED DATA
            blog_form.save(commit=True)
            return index(request)
    else:
        print("What are you doing?")
# ROUTING FUNCTION TO HTML PAGE
    return render(request, 'blogApp/blogInfo.html', {'blog_form': blog_form})

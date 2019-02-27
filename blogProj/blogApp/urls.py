from django.urls import path
from . import views

# ROUTING PATHS TO FUNCTIONS
urlpatterns = [
    path('', views.index, name='index'),
    path('blogform/', views.blogform, name='blogform')

]
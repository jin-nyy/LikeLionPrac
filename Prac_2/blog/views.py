from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog,pk = blog_id)
    
    return render(request,'detail.html',{'blog':blog_detail})

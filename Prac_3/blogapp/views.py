from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from pytz import timezone
from datetime import datetime
from django.utils import timezone
# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request,'home.html',{'blogs':blogs})
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog,pk = blog_id)
    return render(request,'detail.html',{'details':blog_detail})
def create_new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_data = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

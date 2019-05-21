from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})
    
def newhome(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dic = {}

    for word in words:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1
    return render(request,'newhome.html',{'full' : text,'total' : len(words),'dictionary' : word_dic.items()})
    
def webprac(request):
    return render(request,'newhome.html')
def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'detail':blog_detail})
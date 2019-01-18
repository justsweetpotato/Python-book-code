from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime

from blog.models import BlogPost, BlogPostForm


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponseRedirect('/blog')


def archive(request):
    posts = BlogPost.objects.all()[:10]  # 倒序排列
    content = {
        "posts": posts,
        "form": BlogPostForm()
    }
    return render(request, 'archive.html', content)


def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()  # 因为表单中不含 timestamp 所以必须手动生成
            post.save()
        return HttpResponseRedirect('/blog/')

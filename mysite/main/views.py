from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'main/post/list.html', {'posts': posts})

def post_detail(request, post):
	post = get_object_or_404(Post, slug=post)
	return render(request, 'main/post/detail.html',{'post': post})

def home(request):
	return render(request, 'main/home.html')

def about(request):
	return render(request, 'main/about.html')
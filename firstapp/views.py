from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    return render(request, 'firstapp/post_list.html', {})


def about_page(request):
    return render(request, 'firstapp/about.html')


def index(request):
    text = Post.objects.all()
    return render(request, 'firstapp/index.html', {"text": text})

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'firstapp/post_new.html', {'form': form})

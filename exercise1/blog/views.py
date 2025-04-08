from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'This is the content of blog post 1.',
        'date_posted': 'August 27, 2023'
    },
    {
        'author': 'Jane Smith',
        'title': 'Blog Post 2',
        'content': 'This is the content of blog post 2.',
        'date_posted': 'August 28, 2023'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context,)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


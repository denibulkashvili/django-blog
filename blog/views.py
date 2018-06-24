from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Post


def index(request):
    post_list = Post.objects.all().order_by('-date_published')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)

def topics(request):
    topic_list = Topic.objects.order_by('title')
    context = {'topic_list': topic_list}
    return render(request, 'blog/topics.html', context)

def topic(request, topic_title):
    posts = Post.objects.filter(topic__title=topic_title)
    context = {'topic': topic_title, 'posts': posts}
    return render(request, 'blog/topic.html', context)

def post(request, post_title):
    post = Post.objects.get(title=post_title)
    context = {'post': post}
    return render(request, 'blog/post.html', context)

def about(request):
    return render(request, 'blog/about.html')

# def comment(request, post_id):
#     return HttpResponse(f"You are commenting on post: {post_id}")
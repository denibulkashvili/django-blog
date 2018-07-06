from django.shortcuts import get_object_or_404, render
# from django.http import Http404
from .models import Topic, Post


def index(request):
    post_list = Post.objects.order_by('-date_published')
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
    post = get_object_or_404(Post, title=post_title)
    context = {'post': post}
    return render(request, 'blog/post.html', context)

def about(request):
    return render(request, 'blog/about.html')

# def comment(request, post_id):
#     return HttpResponse(f"You are commenting on post: {post_id}")
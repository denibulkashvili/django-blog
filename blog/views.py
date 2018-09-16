import os
from dotenv import load_dotenv
load_dotenv()

from django.shortcuts import get_object_or_404, render
import random
from .models import Topic, Post
import requests


def index(request):
    post_list = Post.objects.order_by('-date_published')
    context = {'post_list': post_list}
    return render(request, 'blog/index.html', context)

def topics(request):
    topic_list = Topic.objects.order_by('title')
    posts = Post.objects.all()
    context = {'topic_list': topic_list, 'posts': posts}
    return render(request, 'blog/topics.html', context)

def topic(request, topic_title):
    posts = Post.objects.filter(topic__title=topic_title)
    context = {'topic': topic_title, 'posts': posts}
    return render(request, 'blog/topic.html', context)

def post(request, post_title):
    post = get_object_or_404(Post, title=post_title)
    all_posts = Post.objects.order_by('-date_published')
    random_posts = [all_posts[x] for x in random.sample(range(1, len(all_posts)), 2)] #2 rand posts
    context = {'post': post, 'random_posts': random_posts}
    return render(request, 'blog/post.html', context)

def about(request):
    return render(request, 'blog/about.html')

# def comment(request, post_id):
#     return HttpResponse(f"You are commenting on post: {post_id}")

## Geo IP API demo
def geoip(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get('http://ip-api.com/json/%s' % ip_address)
    geodata = response.json()
    return render(request, 'blog/geoip.html', {
        'ip': geodata['query'],
        'country': geodata['country'],
        'latitude': geodata['lat'],
        'longitude': geodata['lon'],
        'SUBSCRIPTION_KEY': os.getenv("SUBSCRIPTION_KEY") 
    })
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<topic_title>/', views.topic, name='topic'),
    path('post/<post_title>/', views.post, name='post'),
    # path('post/<int:post_id>/comment/', views.comment, name='comment'),
    path('about/', views.about, name='about'),
    path('geoip/', views.geoip, name='geoip')
]

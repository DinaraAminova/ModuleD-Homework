#from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, DetailView
from .models import Post, PostCategory, Comment
from datetime import datetime
# Create your views here.

class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')


class PostDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

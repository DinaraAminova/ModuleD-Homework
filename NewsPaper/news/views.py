from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from .models import Post, PostCategory, Comment
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.

class PostsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    ordering = ['-postCategory']
    paginate_by = 1


class PostDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 5

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


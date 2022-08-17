from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .models import Post
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
    ordering = ['-id']
    paginate_by = 1
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news_detail'
    queryset = Post.objects.all()

class PostCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = PostForm
    success_url = '/news/'

class PostUpdateView(UpdateView):
    template_name = 'news_update.html'
    form_class = PostForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 5
    form_class = PostForm

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['form'] = PostForm()
        return context


from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView, TemplateView
from .models import Post, Category, Author
from .filters import PostFilter
from .forms import PostForm
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.

class PostsList(ListView, LoginRequiredMixin):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
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

class PostCreateView(CreateView, PermissionRequiredMixin):
    template_name = 'create.html'
    form_class = PostForm
    success_url = '/news/'
    permission_required = ('newsPaper.add_post',)



class PostUpdateView(UpdateView, PermissionRequiredMixin):
    template_name = 'news_update.html'
    form_class = PostForm
    success_url = '/news/'
    permission_required = ('news.change_post',)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDeleteView(DeleteView, PermissionRequiredMixin):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
    permission_required = ('news.delete_post',)


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




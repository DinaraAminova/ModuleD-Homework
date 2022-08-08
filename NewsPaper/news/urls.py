from django.urls import path
from .views import PostsList, PostDetailView, SearchList, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='news_detail'),
    path('search', SearchList.as_view()),
    path('create', PostCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='news_delete'),

]
from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='news_detail'),
    path('search', SearchList.as_view(), name='search'),
    path('create', PostCreateView.as_view(), name='create'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='news_delete'),

]
from django.urls import path
from .views import PostsList, PostDetailView, SearchList


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetailView.as_view()),
    path('search', SearchList.as_view()),

]
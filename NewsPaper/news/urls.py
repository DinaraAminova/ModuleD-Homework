from django.urls import path
from .views import PostsList, PostDetailView


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetailView.as_view()),

]
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListPost, CreatePost

app_name = 'app'

urlpatterns = [
    path('', ListPost.as_view(template_name='index.html'), name='index'),
    path('create/', login_required(CreatePost.as_view(template_name='create_post.html')), name='create_post')
]

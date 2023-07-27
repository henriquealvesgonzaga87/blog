from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import PostForm
from django.contrib import messages


class ListPost(ListView):
    template_name = 'app/index.html'
    paginate_by = 10
    model = Post


class CreatePost(CreateView):
    template_name = 'app/create_post.html'
    model = Post
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('app:index.html')
    
    def form_valid(self, form):
        try:
            post = form.save(commit=False)
            post.user_profile_id = User.object.get(id=self.request.user.id)
        except Exception:
            messages.error('Problems to save your post!')
            print(Exception)
        else:
            form.save()
        return super().form_valid(form)


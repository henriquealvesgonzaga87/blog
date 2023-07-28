from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


class ListPost(ListView):
    template_name = 'app/index.html'
    paginate_by = 10
    model = Post


class CreatePost(CreateView, LoginRequiredMixin):
    template_name = 'app/create_post.html'
    model = Post
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('app:index.html')
    
    def form_valid(self, form):
        try:
            post = form.save(commit=False)
            post.user_profile_id = User.objects.get(id=self.request.user.id)
        except Exception:
            messages.error('Problems to save your post!')
            print(Exception)
        else:
            form.save()
        return redirect("app:index")


class UpdatePost(UpdateView, LoginRequiredMixin):
    template_name = 'app/create_post.html'
    model = Post
    fields = ['title', 'content', 'tags']
    success_url = reverse_lazy('app:index')

    def get_object(self):
        id = self.kwargs.get('id')
        return get_object_or_404(Post, id=id)

    def form_valid(self, form):
        try:
            post = form.save(commit=False)
            post.user_profile_id = User.objects.get(id=self.request.user.id)
        except Exception as e:
            messages.error(self.request, 'Impossible to save')
            print(e)
        else:
            form.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'app/index.html'
    success_url = reverse_lazy('app:index')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('id')
        return get_object_or_404(Post, pk=pk)

    def delete(self, request, *args, **kwargs):
        try:
            messages.success(request, 'Post deleted successfully.')
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            messages.error(request, 'Unable to delete the post.')
            print(e)
            return super().delete(request, *args, **kwargs)
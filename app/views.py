from django.shortcuts import render, redirect
from .models import Post, MyStudies, MyProjects
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login as app_login, logout as app_logout


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


class ListMyStudies(ListView):
    template_name = 'my_path.html'
    ordering = ["-id"]
    paginate_by = 10
    model = MyStudies


class CreateMyStudies(CreateView, LoginRequiredMixin):
    template_name = "create_my_path.html"
    model = MyStudies
    fields = ['title', 'school', 'start_date', 'end_date', 'description', 'link']
    success_url = reverse_lazy('my_path')

    def form_valid(self, form):
        try:
            myprojects = form.save(commit=False)
            myprojects.user_profile_id = User.objects.get(id=self.request.user.id)
        except Exception as e:
            messages.error(self.request, f'Error to save {e}')
            return self.form_invalid(form)
        else:
            form.save()
        return super().form_valid(form)


class UpdateMyStudies(UpdateView):
    template_name = "create_my_path.html"
    model = MyStudies
    fields = ['title', 'school', 'start_date', 'end_date', 'description', 'link']
    success_url = reverse_lazy('my_path')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('id')
        return get_object_or_404(MyStudies, pk=pk)

    def form_valid(self, form):
        try:
            mystudies = form.save(commit=False)
            mystudies.user_profile_id = User.objects.get(id=self.request.user.id)
        except Exception as e:
            messages.error(f'Impossible to save your form now: {e}')
            print(e)
        else:
            form.save()
        return super().form_valid(form)


class DeleteMyStudies(DeleteView, LoginRequiredMixin):
    template_name = "create_my_path.html"
    model = MyStudies
    success_url = reverse_lazy('my_path')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('id')
        return get_object_or_404(MyStudies, pk=pk)
    
    def delete(self, request, *args, **kwargs):
        try:
            messages.success(request, 'Deleted successfully.')
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            messages.error(request, 'Unable to delete.')
            print(e)
            return super().delete(request, *args, **kwargs)
            

class ListMyProject(ListView):
    template_name = 'my_projects.html'
    paginate_by = 10
    model = MyProjects


class CreateMyProject(CreateView, LoginRequiredMixin):
    template_name = 'create_my_project.html'
    model = MyProjects
    fields = ['name', 'link', 'readme', 'resume']
    success_url = reverse_lazy('my_projects')

    def form_valid(self, form):
        try:
            myprojects = form.save(commit=False)
            myprojects.user_profile_id = User.objects.get(id=self.request.user.id)
        except Exception:
            messages.error('Error to save')
        else:
            form.save()
        return super().form_valid(form)


class UpdateMyProject(UpdateView, LoginRequiredMixin):
    template_name = 'create_my_project.html'
    model = MyProjects
    fields = ['name', 'link', 'readme', 'resume']
    success_url = reverse_lazy('my_projects')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('id')
        return get_object_or_404(MyProjects, pk=pk)
    
    def form_valid(self, form):
        try:
            myprojects = form.save(commit=False)
            myprojects.user_profile_id = User.objects.get(id=self.request.user.id)
        except Exception:
            messages.error('Error to save')
        else:
            form.save()
        return super().form_valid(form)
    

class DeleteMyProject(DeleteView, LoginRequiredMixin):
    template_name = 'my_projects'
    model = MyProjects
    success_url = reverse_lazy('my_projects')

    def get_object(self, queryset=None):
        pk = self.kwargs.get('id')
        return get_object_or_404(MyProjects, pk=pk)

    def delete(self, request, *args, **kwargs):
        try:
            messages.success(request, 'Deleted successfully.')
            return super().delete(request, *args, **kwargs)
        except Exception as e:
            messages.error(request, 'Unable to delete.')
            print(e)
            return super().delete(request, *args, **kwargs)

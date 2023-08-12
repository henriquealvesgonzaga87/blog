"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from app.views import ListMyStudies, CreateMyStudies, UpdateMyStudies, DeleteMyStudies, ListMyProject, CreateMyProject, UpdateMyProject, DeleteMyProject


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="about_me.html"), name="about_me"),
    path('my_path/', ListMyStudies.as_view(template_name = 'my_path.html'), name='my_path'),
    path('my_path/create/', login_required(CreateMyStudies.as_view(template_name = 'create_my_path.html')), name='create_my_path'),
    path('my_path/create/submit', login_required(CreateMyStudies.as_view(template_name = 'create_my_path.html')), name='create_my_path'),
    path('my_path/update/<int:id>', login_required(UpdateMyStudies.as_view(template_name = 'create_my_path.html')), name='update_my_path'),
    path('my_path/update/<int:id>/submit', login_required(UpdateMyStudies.as_view(template_name = 'create_my_path.html')), name='update_my_path'),
    path('mypath/delete/<int:id>/', login_required(DeleteMyStudies.as_view(template_name = 'my_path.html')), name='delete_my_path'),
    path('myproject/', ListMyProject.as_view(template_name = 'my_projects.html'), name='my_projects'),
    path('myproject/create/', login_required(CreateMyProject.as_view(template_name='create_my_project.html')), name='create_my_project'),
    path('myproject/create/submit', login_required(CreateMyProject.as_view(template_name='create_my_project.html')), name='create_my_project'),
    path('myproject/update/<int:id>/', login_required(UpdateMyProject.as_view(template_name='create_my_project.html')), name='update_my_project'),
    path('myproject/update/<int:id>/submit', login_required(UpdateMyProject.as_view(template_name='create_my_project.html')), name='update_my_project'),
    path('myproject/delete/<int:id>/', login_required(DeleteMyProject.as_view(template_name='my_projects.html')), name='delete_my_project'),
    path('post/', include('app.urls'))
]

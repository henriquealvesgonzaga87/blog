from django.contrib import admin
from . models import *


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    fields = ['user_profile', 'first_name', 'surname']

@admin.register(Post)
class PostAdmmin(admin.ModelAdmin):
    fields = ['title', 'content', 'tags', 'user_profile_id']

@admin.register(MyStudies)
class MyStudiesAdmin(admin.ModelAdmin):
    fields = ['title', 'school', 'start_date', 'end_date', 'description', 'link', 'user_profile_id']

@admin.register(MyProjects)
class MyProjectsAdmin(admin.ModelAdmin):
    fields = ['name', 'link', 'readme', 'resume']


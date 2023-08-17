from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    class Meta:
        db_table = 'user'


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    tags = models.CharField(max_length=50)
    publish_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    user_profile_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'


class MyStudies(models.Model):
    title = models.CharField(max_length=100)
    school = models.CharField(max_length=80)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    link = models.URLField(null=True)
    user_profile_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mystudies'
    

    def get_formatted_date(self):
        return f"{self.start_date.strftime('%m/%Y')} - {self.end_date.strftime('%m/%Y')}"


class MyProjects(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()
    readme = models.URLField()
    resume = models.TextField()
    user_profile_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'myprojects'

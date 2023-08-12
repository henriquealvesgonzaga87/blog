from django import forms
from .models import MyProjects

class MyProjectsForms(forms.ModelForm):
    name = forms.CharField(max_length=200)
    link = forms.URLField()
    readme = forms.URLField()
    resume = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = MyProjects
        fields = [
            'name',
            'link',
            'resume'
        ]
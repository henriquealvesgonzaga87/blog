from django import forms
from .models import Post

class DateTimeForm(forms.TextInput):
    input_type = "datetime"


class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField()
    publish_date = forms.DateField(widget=DateTimeForm)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'tags',
        ]

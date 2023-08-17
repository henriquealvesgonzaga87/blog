from django import forms
from .models import MyStudies
from django.forms.widgets import DateInput

class MyStudiesForms(forms.ModelForm):
    title = forms.CharField(max_length=100)
    school = forms.CharField(max_length=80)
    start_date = forms.DateField(widget=DateInput(attrs={"type": "date"}))
    end_date = forms.DateField(widget=DateInput(attrs={"type": "date"}))
    description = forms.CharField(widget=forms.Textarea)
    link = forms.URLField(null=True)


    class Meta:
        model = MyStudies
        fields = '__all__'

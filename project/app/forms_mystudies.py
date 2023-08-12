from django import forms
from .models import MyStudies

class DateForm(forms.TextInput):
    input_type = "date"


class MyStudiesForms(forms.ModelForm):
    title = forms.CharField(max_length=100)
    school = forms.CharField(max_length=80)
    start_date = forms.DateField(widget=DateForm)
    end_date = forms.DateField(widget=DateForm)
    description = forms.CharField(widget=forms.Textarea)
    link = forms.URLField(null=True)

    class Meta:
        model = MyStudies
        fields = [
            'title',
            'school',
            'start_date',
            'end_date',
            'description',
            'link'
        ]

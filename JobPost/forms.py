from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Enter job title'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter job description'}),
                                label='')
    url = forms.URLField(label='',
                        widget=forms.URLInput(attrs={'placeholder': 'Enter URL'}))
    class Meta:
        model = JobPost
        fields = [
            'title',
            'description',
            'url',
        ]
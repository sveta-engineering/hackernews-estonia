from cProfile import label
from django import forms
from .models import Post, Comment
 
 
class PostForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Enter title', 'size': 40}))
    url = forms.URLField(label='',
                           widget=forms.URLInput(attrs={'placeholder': 'Enter URL', 'size': 40}))
    class Meta:
        model = Post
        fields = ('title','url')

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('content',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter comment'}),
                                label='')
    class Meta:
        model = Comment
        fields = ('content',)
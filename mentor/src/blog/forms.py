from django import forms
from .models import Blog, BlogImage


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Your title',
                                            'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': 'Your post',
                                             'class': 'form-control'}),
        }


class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ['image', ]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

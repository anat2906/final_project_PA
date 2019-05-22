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


class DeleteProductForm(forms.Form):
    post_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'datas'}))

    def clean(self):
        prod_id = self.cleaned_data.get('prod_id')
        if not prod_id:
            raise forms.ValidationError("There is not product id data!")
        if not Blog.objects.filter(id=prod_id).exists():
            raise forms.ValidationError("Such product does not exist!")
        return self.cleaned_data

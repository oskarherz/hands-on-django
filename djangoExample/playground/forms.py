from django.forms import ModelForm

from djangoExample.playground.models import Post, Author


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class AuthorForm(ModelForm):
    class Author:
        model = Author
        fields = '__all__'

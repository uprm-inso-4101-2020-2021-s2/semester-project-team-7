from django import forms

from .models import Comment_e


class CommentForm_e(forms.ModelForm):
    class Meta:
        model = Comment_e
        fields = ['name', 'email', 'body']
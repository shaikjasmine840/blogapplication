from django import forms
from .models import BlogPost,Comment,Tag

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=['title','content','tags']
tags=forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),required=False,widget=forms.CheckboxSelectMultiple)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']


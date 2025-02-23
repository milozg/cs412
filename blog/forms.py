#blog/forms.py

from django import forms
from .models import Article, Comment

class CreateArticleForm(forms.ModelForm):
    '''A form to add an article to the database'''

    class Meta:
        '''Associate this form with a model from our database'''
        model = Article
        fields = ['author', 'title', 'text', 'image_url']

class CreateCommentForm(forms.ModelForm):
    '''A form to add a comment about an article'''

    class Meta:
        '''Associate this form with the comment model'''
        model = Comment
        fields = ['author', 'text']
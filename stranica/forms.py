# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms

class PostForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        # 'cols': 80,
        'class' : 'form-control',
        'placeholder' : 'Write your post here'
    }), max_length = 300)

class SearchForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={
        
        'class' : 'form-control search-query',
        'autofocus': 'autofocus',
        'placeholder' : 'text'
    }))

class SearchTagForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={
        
        'class' : 'form-control  search-tag-query typeahead input-md',
        'id' : 'typeahead',
        'autofocus' : 'autofocus',
        'placeholder': 'Название статьи сюды....'
    }))
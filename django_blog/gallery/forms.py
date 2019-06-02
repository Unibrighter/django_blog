# -*- coding: utf-8 -*- 
from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = []

    # extra fields (optional)
    zip = forms.FileField(required=False)
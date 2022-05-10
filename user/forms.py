from django import forms
from django.forms import fields
from pages.models import Photo, ppUser, Photo2

class uploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo_name',)

class uploadForm2(forms.ModelForm):
    class Meta:
        model = Photo2
        fields = ('photo_name1','photo_name2','hide')

class uploadppForm(forms.ModelForm):
    class Meta:
        model = ppUser
        fields = ('pp',)
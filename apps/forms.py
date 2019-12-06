from django import forms
from .models import *
from django.forms import ModelForm


class AppCreationForm(ModelForm):
    # body=forms.CharField(widget=FroalaEditor)#(widget=CKEditorWidget())#(widget=FroalaEditor)
    # username = forms.CharField(max_length=200,
    # widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))
    class Meta:
        model = App
        fields = ('name',)


class AppChangeForm(ModelForm):
    # body=forms.CharField(widget=FroalaEditor)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects, widget=forms.CheckboxSelectMultiple(), required=False)
    class Meta:
        model = App
        fields = ('name','url','categories','description','head_img','owner')
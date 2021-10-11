from django import forms
from django.forms.models import ModelForm
from .models import createnotes

class NoteForm(ModelForm):
    class Meta:
        model=createnotes
        fields=["title","text","image"]
from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):  # ModelForm: creates form automatically from model object
    class Meta:
        model = Entry
        exclude = ('created_at', 'updated_at',) # makes created and updated date and time uneditable

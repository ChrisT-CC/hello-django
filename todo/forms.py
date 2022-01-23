from django import forms
from.models import Item


class ItemForm(forms.ModelForm):
    """ form for modifing items """
    class Meta:
        """
        this class gives to the form information like which fields it should
        render how it should display error messages
        """
        model = Item
        fields = ['name', 'done']

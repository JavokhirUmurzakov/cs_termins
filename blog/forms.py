# forms.py
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'name',
            'id': 'name',
            'type': 'text',
            'placeholder': 'John Doe',
            'maxlength': '36',
            'minlength': '5',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'JohnDoe@mail.com',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'message',
            'id': 'message',
            'type': 'text',
            'placeholder': 'message',
            'maxlength': '22',
            'minlength': '8'
        })

    name = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
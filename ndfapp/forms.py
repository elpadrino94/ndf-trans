from django import forms
from .models import Avis, Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Votre nom'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'exemple@.com'}),
            'subject': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Objet'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message', 'rows':5}),
        }

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre Nom'}),
            'message': forms.Textarea(attrs={'maxlength':'200', 'class':'form-control', 'placeholder':'Message', 'rows':5}),
        }
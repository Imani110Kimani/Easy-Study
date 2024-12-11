from django import forms
from myapp.models import Contact, Trainer

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'role', 'description', 'image', 'twitter', 'facebook', 'instagram', 'linkedin']

    twitter = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'Enter Twitter URL', 'class': 'form-control'}))
    # Similarly for other fields

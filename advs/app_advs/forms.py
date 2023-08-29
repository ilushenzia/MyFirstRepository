from django import forms
from django.core.exceptions import ValidationError
from .models import Advs

class AdvForm(forms.ModelForm):
    class Meta:
        model = Advs
        fields = ['title', 'description', 'image', 'price', 'auction']
        widgets = {
            'title' : forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
            'description' : forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
            'price' : forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
            'auction' : forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
            'image' : forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
        return title
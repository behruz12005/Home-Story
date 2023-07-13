from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['tur', 'joy', 'kv_soni', 'narx', 'describe', 'rasm1', 'rasm2', 'rasm3', 'rasm4', 'rasm5', 'rasm6']
        labels = {
            'tur': 'Turi',
            'joy': 'Joylashuvi',
            'kv_soni': 'Kvartira soni',
            'narx': 'Narxi',
            'describe': 'Tavsifi',
            'rasm1': 'Rasm',
        }
        widgets = {
            'tur': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Turi'}),
            'joy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Joylashuvi'}),
            'kv_soni': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Kvartira soni'}),
            'narx': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Narxi'}),
            'describe': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tavsifi'}),
            'rasm1': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Rasm'}),
            'rasm2': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Rasm'}),
            'rasm3': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Rasm'}),
            'rasm4': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Rasm'}),
            'rasm5': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Rasm'}),
            'rasm6': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Rasm'}),
        }

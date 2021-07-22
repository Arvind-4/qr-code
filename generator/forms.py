from django import forms

class FormClass(forms.Form):
    name = forms.CharField(max_length=300, 
            widget = forms.TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Enter a Text...',
                'label': '',
            }))
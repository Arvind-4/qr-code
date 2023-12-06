from django import forms


class FormClass(forms.Form):
    name = forms.CharField(
        max_length=300,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your contents ...",
                "label": "",
                "rows": 5,
            }
        ),
    )

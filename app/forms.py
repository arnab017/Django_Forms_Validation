from django import forms
from django.core import validators

class StudentForm(forms.Form):
    sid = forms.IntegerField(label_suffix=' ')
    sname = forms.CharField(label_suffix=' ', max_length=50, validators=[validators.MinLengthValidator(5)])
    sage = forms.IntegerField(label_suffix=' ',validators=[validators.MaxValueValidator(18)])
    smail = forms.EmailField(label_suffix=' ',validators=[validators.MinLengthValidator(10)])
    phone = forms.CharField(max_length=10, validators=[validators.RegexValidator('[6-9]\d{9}')])

    
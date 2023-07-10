from django import forms

def sname_Validate_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('Name should not starts with a')

def sname_Validate_length(value):
    if len(value)<=5:
        raise forms.ValidationError('Name should not be less than 5 characters')

class StudentForm(forms.Form):
    sid = forms.IntegerField()
    sname = forms.CharField(max_length=50, validators=[sname_Validate_for_a,sname_Validate_length])
    sage = forms.IntegerField()
    smail = forms.EmailField(validators=[sname_Validate_for_a])
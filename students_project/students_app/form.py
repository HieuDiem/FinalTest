from dataclasses import field
from django import forms
from .models import Teacher
from django.forms import ModelForm



class addStudent(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    address = forms.CharField(max_length=100)
    mobile_number = forms.CharField()

#QS6:

class teacher_Form(forms.ModelForm):
    class Meta:
        model = Teacher
        fields= ['id', 'name', 'age', 'address']

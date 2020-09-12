from django import forms
from part4.models import Registration

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = "__all__" 
        
# By Single Requirement
# fields = ['name','email','contact','address','image']
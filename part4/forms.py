from django import forms
from part4.models import Register

class RegisterForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = "__all__" 
        
# By Single Requirement
# fields = ['name','email','contact','address']
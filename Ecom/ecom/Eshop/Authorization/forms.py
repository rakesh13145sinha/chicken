form django import forms
form Authorization.models import Identification
class Idform(forms.ModelForm):
    
    class Meta:
        model = Identification
        fields = '__all__'
)
# from django import forms

# from .models import Developer,Technology

from django import forms
from data.models import Developer

class DeveloperForm(forms.ModelForm):
    class Meta :
        model=Developer
        fields='__all__'

class SearchForm(forms.Form):
    location = forms.CharField()
    technology = forms.CharField()


# class AddDeveloper(forms.ModelForm):
#     class Meta:
#         model=Developer
#         fields=['name','email' , 'location']
#         # 'technolgy','domain' , 'projects','blogs','qa']


#     name = forms.CharField()
#     email= forms.EmailField() 
#     technology = forms.ModelMultipleChoiceField(
#         queryset=Technology.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )
# class Add(forms.Form):
#     name=forms.CharField( max_length=200)
    
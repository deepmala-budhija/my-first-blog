from django import forms
from .models import MFS

class PostForm(forms.ModelForm):

    class Meta:
        model = MFS
        fields = ('survey_date','name_of_surveyor','village','house_number','household_number',)
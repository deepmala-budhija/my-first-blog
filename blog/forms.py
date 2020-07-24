from django import forms
from .models import Post, LineListing
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)

class LineListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LineListingForm, self).__init__(*args, **kwargs)
       
        self.fields["survey_date"].required = False

    class Meta:
        model = LineListing
        fields = ('village','house_number','household_number','survey_date','person_name_collecting_data',)
        widgets = {
            'survey_date': DatePickerInput(format='%Y-%m-%d'),
        }
from django import forms
from .models import Pedometer


class DateInput(forms.DateInput):
    input_type = 'date'


# Form for the log page
class LogStepsForm(forms.ModelForm):
    class Meta:
        model = Pedometer
        fields = ['steps', 'date']
        widgets = {
            'date': DateInput()
        }


# form for the charts page
class ChartDateForm(forms.Form):
    from_date = forms.DateField(required=True, widget=DateInput())
    to_date = forms.DateField(required=True, widget=DateInput())

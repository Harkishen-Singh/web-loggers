from django import forms
from django.utils import timezone
from models import GeneralLogger
import datetime

class LogForm(forms.Form):
    class Meta:
        model = GeneralLogger
        fields = ('usr_time', 'usr_filepath', 'message', )
    usr_filepath = forms.CharField(max_length=50, required=True)
    message = forms.CharField(max_length=225, required=True)
    

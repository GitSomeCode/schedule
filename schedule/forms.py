from django import forms
from schedule.models import Meeting
#from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

class MeetingForm(forms.ModelForm):
  '''
  
  
  person = forms.CharField(max_length = 30)
  company = forms.CharField(max_length = 30)
  date = forms.DateTimeField()
  location = forms.CharField(max_length = 100)
  priority = forms.CharField(max_length = 1)
  '''
  class Meta:
    model = Meeting
    exclude = ['ended', 'user']
    
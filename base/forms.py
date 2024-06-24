from django.forms import ModelForm
from .models import Alarm

class AlarmForm(ModelForm):
  class Meta:
    model = Alarm
    fields = '__all__'
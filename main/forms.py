import datetime
from django import forms
from.models import Booking, Table

class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(queryset=Table.objects.filter(available=True))
    class Meta:
        model = Booking
        fields = ('table', 'booking_time', 'number_of_people', 'special_requests')

    booking_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'min': datetime.date.today().strftime('%Y-%m-%dT%H:%M'),  # minimum date is today
            'max': (datetime.date.today() + datetime.timedelta(days=90)).strftime('%Y-%m-%dT%H:%M'),  # maximum date is 90 days from today
        }),
    )
    number_of_people = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'min':1
        }),
    )
    special_requests = forms.CharField(label='Special Request', required=False, widget=forms.TextInput(attrs={'size': '60'}))
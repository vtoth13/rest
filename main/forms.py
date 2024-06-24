from django import forms
from .models import Booking, Table

class BookingForm(forms.ModelForm):
    table = forms.ModelChoiceField(queryset=Table.objects.filter(available=True))
    class Meta:
        model = Booking
        fields = ('table', 'booking_time', 'number_of_people', 'special_requests')
        widgets = {
            'booking_time':forms.TextInput(attrs={'type':'datetime-local'}),
        }
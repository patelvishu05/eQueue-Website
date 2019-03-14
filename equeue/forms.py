from django import forms
from . models import *


class KioskSignIn(forms.ModelForm):
    serviceList =(
        (None,'Select'),
        (1, 'Drop Form (1 Minutes)'),
        (10, 'Financial Aid (10 Minutes)'),
        (10, 'Fiscal Service (10 Minutes)'),
        (5, 'One Stop (5 Minutes)'),
        (5, 'Pay Tuition (5 Minutes)'),
        (10, 'Other (10 Minutes)')
    )

    firstName = forms.CharField(label='First Name', widget=forms.TextInput(attrs={"placeholder": "First Name"}))
    lastName = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={"placeholder": "Last Name"}))
    phoneNumber = forms.IntegerField(label='Phone Number')
    service = forms.ChoiceField(choices=serviceList)

    class Meta:
        model = Person
        fields = [
            'firstName',
            'lastName',
            'phoneNumber',
            'service'
        ]

    def save(self, commit=True):
        person = Person()
        person.lineNumber = person.getLineNumber()
        person.firstName = self.cleaned_data['firstName']
        person.lastName = self.cleaned_data['lastName']
        person.phoneNumber = self.cleaned_data['phoneNumber']
        person.service = self.cleaned_data['service']

        if commit:
            person.save()

        return person





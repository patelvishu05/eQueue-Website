from django import forms
from . models import *
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import *
from django.shortcuts import render, redirect


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
            'service',
        ]

    def save(self, commit=True):
        person = Person()
        person.lineNumber = person.getLineNumber()
        person.firstName = self.cleaned_data['firstName']
        person.lastName = self.cleaned_data['lastName']
        person.phoneNumber = self.cleaned_data['phoneNumber']
        person.service = self.cleaned_data['service']
        person.waitTime = person.minuteMinder()

        if commit:
            person.save()

        return person


User = get_user_model()


class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise forms.ValidationError('This User is not active')

        return super(AdminLoginForm, self).clean(*args,**kwargs)




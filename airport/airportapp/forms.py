# forms.py


from django import forms
from django.contrib.auth.models import User
from models import *
from django.utils.translation import ugettext_lazy as _


class v_RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_(
        "Username"), error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(
        required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(
        required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    

    carplate =forms.CharField(widget=forms.TextInput(
    attrs=dict(required=True, max_length=30)), label=_("Car Plate Number"))
    #available_time_start = forms.DateTimeField(label=_("Set your starting avalible time"))
    #available_time_end = forms.DateTimeField(label=_("Set your ending avalible time"))
    driver_license = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=50)), label=_("License number"))

    def clean_username(self):
        try:
            user = Volunteer.objects.get(
                username__iexact=self.cleaned_data['username'])
        except Volunteer.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(
            _("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    _("The two password fields did not match."))
        return self.cleaned_data


class s_RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_(
        "Username"), error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})
    email = forms.EmailField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(
        required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(
        required=True, max_length=30, render_value=False)), label=_("Password (again)"))
    flight_number = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)), label=_("Flight number"))
    

    def clean_username(self):
        try:
            user = NewStudent.objects.get(
                username__iexact=self.cleaned_data['username'])
        except NewStudent.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(
            _("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(
                    _("The two password fields did not match."))
        return self.cleaned_data


from django import forms

class LoginForm(forms.Form):
	team_name = forms.CharField(label='Team Name', max_length=100)
	team_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
from django import forms

class ContactForm(forms.Form):
	name= forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
	email= forms.EmailField(label='Email Address', widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
	message= forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Hi, I am a seller/buyer and I would love to work with you...'}))
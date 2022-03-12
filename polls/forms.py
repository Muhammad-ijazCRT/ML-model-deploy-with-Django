from django import forms


class my_form(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.CharField(label='Your email', max_length=100)
    your_phone = forms.CharField(label='Your phone', max_length=100)
    CHOICES = [('select1', 'select 1')]
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

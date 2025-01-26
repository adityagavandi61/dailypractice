from django import forms

# choices
GENDER_CHOICES = [
    ('M', 'MALE'),
    ('F', 'FEMALE'),
    ('O', 'OTHERS')
]
INTEREST_CHOICES = [
    ('sports', 'Sports'),
    ('music', 'Music'),
    ('reading', 'Reading'),
    ('traveling', 'Traveling'),
    ('cooking', 'Cooking')
]


class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=50)
    profile_picture = forms.ImageField(widget=forms.ClearableFileInput())
    file_upload = forms.FileField(widget=forms.FileInput(attrs={'placeholder': 'Upload a file', 'accept': '.pdf,.doc'}))
    username = forms.CharField(max_length=50, help_text='Username should be unique',
                               label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter a Username'}), required=True)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    mobile_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', required=False)
    address = forms.CharField(widget=forms.Textarea())
    date_of_birth_select = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2100)))
    date_of_birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time_input = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    gender_select = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(), label='Gender', label_suffix=" ")
    gender_radio = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    interest = forms.MultipleChoiceField(choices=INTEREST_CHOICES)
    interest_checkbox = forms.MultipleChoiceField(choices=INTEREST_CHOICES, widget=forms.CheckboxSelectMultiple())
    interest_choice = forms.ChoiceField(choices=INTEREST_CHOICES, widget=forms.SelectMultiple())
    interest_select = forms.ChoiceField(choices=INTEREST_CHOICES, widget=forms.Select())
    website_url = forms.URLField()
    Agreed = forms.BooleanField()  # this and below are working same as checkbox
    agrred = forms.NullBooleanField()
    Agreed_checkbox = forms.ChoiceField(widget=forms.CheckboxInput())  # this and above are working same as checkbox
    key = forms.CharField(widget=forms.HiddenInput(), initial='value')  # this and below are working same as hidden

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    remember_me = forms.BooleanField(required=False)

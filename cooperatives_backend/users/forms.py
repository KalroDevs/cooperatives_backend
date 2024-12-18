from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'role', 'position', 'first_name', 'last_name', 'gender', 'county' )  # Add the role field here

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].choices = [
            ('admin', 'Administrator'),
            ('national', 'National'),
            ('county', 'County'),        
            ('sp', 'Service Provider'),
            ('fa', 'Funding Agency'),
            ('os', 'Other Stakeholders')
        ]  # Limit choices if needed

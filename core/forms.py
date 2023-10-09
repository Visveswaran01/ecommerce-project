from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Consumer

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Consumer
        fields = ['username','fname','lname']
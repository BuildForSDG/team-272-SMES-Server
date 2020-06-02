from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        """
        Defining expected fields when called.
        """
        model = CustomUser
        fields = ('username', 'email', 'Age')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        """
        Defining expected fields when called.
        """
        model = CustomUser
        fields = ('username', 'email', 'Age')

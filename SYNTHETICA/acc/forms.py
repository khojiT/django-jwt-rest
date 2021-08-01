from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import mainUser


class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = mainUser
        fields = '__all__'


class UserChangeForm(UserChangeForm):

    class Meta:
        model = mainUser
        fields = '__all__'
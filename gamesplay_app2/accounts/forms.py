from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from gamesplay_app2.accounts.models import Profile


UserModel = get_user_model()


class CreateProfileForm(auth_forms.UserCreationForm):

    class Meta:
        model = Profile
        fields = ('email', 'age')
        # field_classes = {'email': auth_forms.EmailField}

#     class Meta:
#         model = UserModel
#         fields = ('username', 'email')
#         field_classes = {
#             'username': auth_forms.UsernameField,
#         }


class EditProfileForm(auth_forms.UserChangeForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # field_classes = {'username': auth_forms.UsernameField}


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


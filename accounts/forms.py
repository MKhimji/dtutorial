from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, SetPasswordForm
from django.utils.translation import gettext as _
from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import validate_password








class RegistrationForm(UserCreationForm):



    class Meta:
        model = User


        fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',


        )
    
    email = forms.EmailField(required=True)

    def clean_email(self):
      email = self.cleaned_data['email']
      if User.objects.filter(email=email).exists():
        raise forms.ValidationError("Email already exists")
      return email
   
    password1 = forms.RegexField(
            widget=forms.PasswordInput,
            label= 'Password',
            min_length=8, 
            regex = r'[\w+]{8,}', 
            help_text = "Your password can't be too similar to your other personal information. "
            "Your password must contain at least 8 characters.Your password can't be a commonly "
            "used password.Your password can't be entirely numeric."

        )


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")   

        if password1 and password2 and password1 != password2:
            self.add_error('password1', 'Re-enter password')
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2



 


    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class EditProfileForm(forms.ModelForm):


    class Meta:
        model = User

        fields = (
            'email',
            'first_name',
            'last_name',

        )


class ChangePassword(PasswordChangeForm):

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(label=_("New password"),
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label=_("New password confirmation"),
                                    widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].help_text = "Your password can't be too similar to your other personal information.Your password must contain at least 8 characters.Your password can't be a commonly used password.Your password can't be entirely numeric."
        self.fields['old_password'].help_text = "Enter current password"

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                self.add_error('new_password1','The two password fields didn\'t match')
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user

        old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput)

    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': _("Your old password was entered incorrectly. "
                                "Please enter it again."),
    })
    old_password = forms.CharField(label=_("Current password"),
                                   widget=forms.PasswordInput)



    def clean_old_password(self):

        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password



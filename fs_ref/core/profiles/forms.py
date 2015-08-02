from django.forms.models import ModelForm
from fs_ref.core.profiles.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'user_group')
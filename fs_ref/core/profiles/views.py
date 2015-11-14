from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from fs_ref.core.auth import get_current_user
from fs_ref.core.profiles.forms import ProfileForm
from fs_ref.core.shortcuts import render


@login_required
def edit_profile(request):
    instance = request.user.profile
    form = ProfileForm(instance=instance)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            request.session['django_language'] = get_current_user().profile.language
            return redirect(reverse('admin_topics'))

    return render(request, 'core/profiles/edit.html', {'form': form})

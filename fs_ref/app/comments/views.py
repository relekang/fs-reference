from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import ugettext_lazy as _
from fs_ref.app.comments.forms import CommentForm
from fs_ref.app.comments.models import ReferenceComment


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(ReferenceComment, pk=comment_id, user=request.user)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect(reverse('view_reference', args=[comment.reference.slug]))

    return render(request, 'comments/edit_comment.html', {
        'form': form,
    })


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(ReferenceComment, pk=comment_id, user=request.user)
    reference = comment.reference
    comment.delete()
    messages.success(request, _("The comment was deleted"))
    return redirect(reverse('view_reference', args=[reference.slug]))

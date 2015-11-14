from fs_ref.api.util import login_or_token_required, render_json
from fs_ref.app.references.forms import CustomerForm


@login_or_token_required()
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return render_json({'customer': customer.to_dict()})
        else:
            return render_json(error=[{'field': k, 'error': unicode(v[0])} for k, v in form.errors.items()])

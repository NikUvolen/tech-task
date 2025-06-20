from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class AnonymityRequiredMixin(AccessMixin):
    login_url = 'main_page'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main_page')
        return super().dispatch(request, *args, **kwargs)

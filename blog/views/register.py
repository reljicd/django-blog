from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'email']
    template_name = 'blog/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Hash password before sending it to super
        form.instance.password = make_password(form.instance.password)
        return super().form_valid(form)

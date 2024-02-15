from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView

from apps.forms import UserForm
from apps.models import User


class UserListView(ListView):
    template_name = 'apps/user_list.html'
    paginate_by = 9
    queryset = User.objects.order_by('-id')
    context_object_name = 'users'


class UserDeleteView(DeleteView):
    model = User
    queryset = User.objects.all()
    success_url = reverse_lazy('user_list_page')


class UserUpdateView(UpdateView):
    template_name = 'update_user.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('index')

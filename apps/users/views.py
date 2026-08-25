from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.conf import settings

from apps.users.models import User
from apps.users.forms import UserForm

class UserListView(ListView):
    model = User
    template_name = "users/crud/user_list.html"
    paginate_by = settings.PAGE_NUMBER
    context_object_name = "users"

class UserDetailView(DetailView):
    model = User
    template_name = "users/user_detail.html"
    context_object_name = "user"

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "users/crud/user_create.html"
    success_url = reverse_lazy("users:user_list")

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/crud/user_update.html"

class UserDeleteView(DeleteView):
    model = User
    template_name = "users/crud/user_delete.html"
    success_url = reverse_lazy("users:user_list")
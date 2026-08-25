from django.urls import path
from apps.users.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView

app_name = "users"

urlpatterns = [
    path("user-list/", UserListView.as_view(), name="user_list"),
    path("user-create/", UserCreateView.as_view(), name="user_create"),
    path("user-detail/<slug:slug>/", UserDetailView.as_view(), name="user_detail"),
    path("user-update/<slug:slug>/", UserUpdateView.as_view(), name="user_update"),
    path("user-delete/<slug:slug>/", UserDeleteView.as_view(), name="user_delete"),
]
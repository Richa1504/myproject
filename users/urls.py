from django.urls import path
from .views import register, user_list, index, delete_user, edit_user

urlpatterns = [
    path("",index,name="index"),
    path("register/", register, name="register"),
    path("users/", user_list, name="user_list"),
    path("delete/<int:user_id>/", delete_user, name="delete_user"),
    path("edit/<int:user_id>/",edit_user, name="edit_user"),
]

from django.contrib import admin
from django.urls import path
from users.views import reg, username_auth,add

urlpatterns = [
    path("reg", reg),
    path("username_auth/", username_auth),
    path("add/", add),
]

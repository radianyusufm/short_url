from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("create_short_url", views.create_short_url, name="create_short_url"),
    path("password", views.password, name="password"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("delete/<int:id>", views.delete_url, name="delete_url"),
    path("s/<str:url>", views.get_url_short, name="get_url_short"),
]
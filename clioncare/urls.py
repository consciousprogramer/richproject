from django.urls import path
from . import views

app_name = "clioncare"
urlpatterns = [
    path("", views.index, name = "index"),
    path("costpage", views.costpage, name = "costpage"),
    path("chatform", views.chatform, name = "chatform"),
    path("hairform", views.hairform, name = "hairform"),
    path("createuser", views.createuser, name = "createuser"),
    path("login", views.userlogin, name = "login"),
    path("logout", views.userlogout, name =  "logout"),
]

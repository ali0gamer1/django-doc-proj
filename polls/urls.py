from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("create/", views.create, name = "create"),
    path("vote/<int:hes>/", views.vote_view, name = "vote_view"),
    path("vote/<int:hes>/<int:choice>/", views.vote_choice_view),
    path("sign_up/", views.sign_up_view, name = "sign_up"),
    path("login/", views.login_view, name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    
    
]
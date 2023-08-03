from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('signup1',views.signup,name="signup"),
    path('signin1',views.signin,name="signin_link"),
    path('signout',views.signout,name="signout")
]
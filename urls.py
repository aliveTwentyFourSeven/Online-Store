from django.urls import path
from .views import HomePage, Signup, Login, Logout

urlpatterns = [
    path('home/',  HomePage, name="home-page"),
    path('signup/', Signup, name="signup-page"),
    path('login/', Login, name="login-page"),
    path('logout/', Logout, name="logOut")

]
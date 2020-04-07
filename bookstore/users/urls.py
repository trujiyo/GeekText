from django.urls import path
from .views import SignUpView, ProfileView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', SignUpView, name='signup'),
    path('profile/', ProfileView, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

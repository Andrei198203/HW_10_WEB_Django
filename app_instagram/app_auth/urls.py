from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from .import views
from .forms import LoginForm

app_name = "app_auth"

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm), name='signin'),
    path('logout/', LogoutView.as_view(template_name='app_auth/logout.html'), name='logout')
]


# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import path
#
# from . import views
# from .forms import LoginForm
#
# app_name = "app_auth"
#
# urlpatterns = [
#     path('signup/', views.RegisterView.as_view(), name='signup'),
#     path('signin/', views.CustomLoginView.as_view(template_name='app_auth/login.html', form_class=LoginForm),
#          name='signin'),
#     path('logout/', LogoutView.as_view(template_name='app_auth/logout.html'), name='logout')]


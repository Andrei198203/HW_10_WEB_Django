from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import RegisterForm

# Create your views here.


class RegisterView(View):
    template_name = 'app_auth/register.html'
    form_class = RegisterForm




    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Welcome {username}. Your account successfully created")
            return redirect(to="app_auth:signin")
        return render(request, self.template_name, {"form": form})

# from django.contrib.auth.views import LoginView, LogoutView
# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib import messages
#
# from .forms import RegisterForm, LoginForm
#
#
# # Клас для обробки входу
# class CustomLoginView(LoginView):
#     template_name = 'app_auth/login.html'
#     form_class = LoginForm
#
# # Клас для обробки реєстрації
# class RegisterView(View):
#     template_name = 'app_auth/register.html'
#     form_class = RegisterForm
#
#     def get(self, request):
#         return render(request, self.template_name, {"form": self.form_class})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data["username"]
#             messages.success(request, f"Welcome {username}. Your account successfully created")
#             return redirect(to="app_auth:signin")
#         return render(request, self.template_name, {"form": form})
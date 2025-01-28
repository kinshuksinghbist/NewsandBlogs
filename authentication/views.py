from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True
    next_page = '/'

class UserLogoutView(LogoutView):
    next_page = 'login'


class UserRegistrationView(CreateView):

    from django.shortcuts import render, redirect
    from .forms import CustomUserCreationForm

    def register(request):
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect('login')
        else:
            form = CustomUserCreationForm()

        return render(request, 'authentication/register.html', {'form': form})

    form_class = UserCreationForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('login')

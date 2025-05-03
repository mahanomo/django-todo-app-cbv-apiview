from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import CustomUserCreationForm,SimpleSignupForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "accounts/login.html")

class signup_view(CreateView):
    form_class = SimpleSignupForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/signup.html"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(self.request, user)
        return super().form_valid(form)
    
def logout_view(request):
    logout(request)
    return redirect('/')
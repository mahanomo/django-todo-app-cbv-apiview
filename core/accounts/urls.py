from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path("login/",views.login_view, name="login"),
    path("signup/",views.signup_view.as_view(), name="signup"),
    path("logout/",views.logout_view, name="logout"),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]
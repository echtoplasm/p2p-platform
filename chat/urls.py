from django.urls import path, include 
from chat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  path("chat/", chat_views.chatPage, name="chat-page"),

  #login-section
  path("auth/login/", LoginView.as_view(template_name="templates/registration/login.html"), name="login"), 
  path("auth/logout/", LogoutView.as_view(), name="logout"),
]

from django.urls import path
from mycrm import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('logout', views.logout_user, name="logout"),
    path('Register/', views.register_user, name="Register")
]
from django.urls import path
from .import views
urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('manageprofile/', views.manageprofile, name='manageprofile'),
    path('medicalpro/', views.medicalpro, name='medicalpro'),


]

from django.urls import path
from .import views
urlpatterns = [
    path('prog_details/', views.prog_details, name='prog_details'),
    path('notification/', views.notification, name='notification'),
    path('prescription/', views.prescription, name='prescription'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('term_condition/', views.term_condition, name='term_condition'),




]

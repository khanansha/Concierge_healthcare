from django.urls import path
from .import views
urlpatterns = [
    path('prog_details/', views.prog_details, name='prog_details'),
    path('notification/', views.notification, name='notification'),
    path('prescription/', views.prescription, name='prescription'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('term_condition/', views.term_condition, name='term_condition'),
    path('updnot/<int:notification_id>', views.update_noti, name='update_noti'),
    path('blogindex/', views.blogindex, name='blogindex'),
    path('category/<int:category_id>', views.category, name='category'),
    path('blog_inner/<int:blog_id>', views.blog_inner, name='blog_inner'),
    path('faq/', views.faq, name='faq'),
    path('home/', views.home, name='home'),


]

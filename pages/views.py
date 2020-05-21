from django.http import HttpResponse
from django.shortcuts import render
from.models import Notification

# Create your views here.


def prog_details(request):
    return render(request, 'pages/prog_details.html')


def notification(request):
    notification = Notification.objects.all()
    return render(request, 'pages/notification.html', {'notification': notification})


def prescription(request):
    return render(request, 'pages/prescription.html')


def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')


def term_condition(request):
    return render(request, 'pages/terms_cond.html')


def update_noti(request, notification_id):
    q = Notification.objects.filter(id=notification_id).update(unread=0)
    return HttpResponse("this is a message")


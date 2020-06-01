from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import render
from.models import Notification, Category, blog


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


def blogindex(request):
    category = Category.objects.all()

    blogs = blog.objects.order_by('-created_at')[:9]

    context = {
        'category': category,
        'blogs': blogs,
    }

    return render(request, 'pages/blogindex.html', context)


def category(request, category_id):
    category = Category.objects.all()
    blogs = blog.objects.filter(category_id=category_id)
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    context = {
        'category': category,
        'blogs': paged_blog,
        'url_category': category_id
    }

    return render(request, 'pages/blog.html', context)


def blog_inner(request, blog_id):
    blogs = blog.objects.order_by('-created_at')[:3]
    blogdetail = blog.objects.filter(id=blog_id)
    category = Category.objects.all()

    context = {
        'blogdetail': blogdetail,
        'category': category,
        'blogs': blogs,
    }
    return render(request, 'pages/blog_inner.html', context)


def faq(request):
    return render(request, 'pages/faq.html')


def home(request):
    blogs = blog.objects.order_by('-created_at')[:3]
    context = {
        'blogs': blogs,
    }

    return render(request, 'pages/home.html', context)


from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from .models import Singup, city, Profile
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
import json
import requests
from django.http import JsonResponse


# Create your views here.


def signup(request):
    if request.method == 'POST':

        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # usernm = get_random_string(6, allowed_chars='0123456789')
        # username = first_name + usernm  # single quo
        email = request.POST['email']
        username = email
        password = request.POST['password']
        password2 = request.POST['password2']
        mobile_no = request.POST['mobile_no']
        gender = request.POST['gender']
        location = request.POST['location']

        if password == password2:
            min_length = 8

            if len(password) < min_length:

                messages.error(
                    request, 'password should have atleast 8 characters')
                return redirect('signup')
            else:

                if password.isdigit():
                    messages.error(
                        request, 'password should not all numeric')
                    return redirect('signup')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Id already exist')

                return redirect('signup')

            else:

                min_length = 10
                if len(mobile_no) < min_length:
                    messages.error(
                        request, 'Please enters 10 digits phone number')

                    return redirect('signup')

                else:

                    user = User.objects.create_user(
                        password=password, email=email, first_name=first_name, last_name=last_name, username=username)
                    user.save()
                    u = User.objects.filter(email=email)
                    uid = u[0].id
                    signup = Singup(
                        user_id=uid, mobile_no=mobile_no, gender=gender, location=location)
                    signup.save()
                    pro = Profile(user_id=uid)
                    pro.save()

                    return redirect('login')
        else:

            messages.error(request, 'Passwords do not match')

            return redirect('signup')
    else:

        citydata = city.objects.all()
        return render(request, 'accounts/signup.html', {'citydata': citydata})


def login(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:

            auth.login(request, user)

            messages.success(request, 'You are now logged in')

            return redirect('profile')

        else:

            messages.error(request, 'Invalid credentials')

            return redirect('login')

    else:

        return render(request, 'accounts/login.html')


# @login_required(login_url="login")
def profile(request):
    if request.method == "POST":
        DOB = request.POST['DOB']
        Height = request.POST['Height']
        Weight = request.POST['Weight']
        Smoke = request.POST['Smoke']
        Allergy = request.POST['Allergy']
        Medication = request.POST['Medication']
        Blood_Group = request.POST['Blood_Group']
        Alcohol = request.POST['Alcohol']
        user_id = request.user.id
        print(user_id)
        u = Profile.objects.filter(user_id=request.user.id).update(
            DOB=DOB, Height=Height, Weight=Weight, Smoke=Smoke, Alcohol=Alcohol, Allergy=Allergy, Medication=Medication, Blood_Group=Blood_Group)
        messages.success(
            request, 'your profile has successfully  updated')

        return redirect('profile')

    else:

        profile = Profile.objects.filter(user_id=request.user.id)
        return render(request, 'accounts/profile.html', {'profile': profile})


def manageprofile(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        # usernm = get_random_string(6, allowed_chars='0123456789')
        # username = first_name + usernm  # single quo
        email = request.POST['email']
        username = email
        # password = request.POST['password']
        # password2 = request.POST['password2']
        mobile_no = request.POST['mobile_no']
        gender = request.POST['gender']
        location = request.POST['location']
        DOB = request.POST['DOB']
        Height = request.POST['Height']
        Weight = request.POST['Weight']
        Smoke = request.POST['Smoke']
        Allergy = request.POST['Allergy']
        Medication = request.POST['Medication']
        Blood_Group = request.POST['Blood_Group']
        Alcohol = request.POST['Alcohol']
        user_id = request.user.id
        db_oldemail = User.objects.get(email=request.user.email)
        #old = db_oldemail[0].email
        # print(old)
        # print(db_oldemail)
        print("DB")

        oldemail = request.user.email
        print(email)
        # print(oldemail)
        # print(user_id)
        checkemail = User.objects.filter(email=oldemail)
        # print(checkemail)
        # if checkemail:

        if email == oldemail:
            print("Inside if")
            #akhan@gmail.com (email)
            #akhan@gmail.com (oldemail)
            #13 (userid)

            userpro = User.objects.filter(id=request.user.id).update(
                first_name=first_name, last_name=last_name)

            signup = Singup.objects.filter(user_id=request.user.id).update(
                mobile_no=mobile_no, gender=gender, location=location)

            profile = Profile.objects.filter(user_id=request.user.id).update(
                DOB=DOB, Height=Height, Weight=Weight, Smoke=Smoke, Alcohol=Alcohol, Allergy=Allergy, Medication=Medication, Blood_Group=Blood_Group)

            messages.success(request, 'updated')
            return redirect('manageprofile')
        else:
            # anjkhan@gmail.com (email)
            # akhan@gmail.com (oldemail)
            # 13

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email Id already exist')
                return redirect('manageprofile')

            else:
                userpro = User.objects.filter(id=request.user.id).update(
                    first_name=first_name, last_name=last_name, email=email, username=email)

                signup = Singup.objects.filter(user_id=request.user.id).update(
                    mobile_no=mobile_no, gender=gender, location=location)

                profile = Profile.objects.filter(user_id=request.user.id).update(
                    DOB=DOB, Height=Height, Weight=Weight, Smoke=Smoke, Alcohol=Alcohol, Allergy=Allergy, Medication=Medication, Blood_Group=Blood_Group)
                return redirect(manageprofile)

                user = auth.authenticate(
                    username=username, password=request.user.password)
                if user is not None:
                    auth.login(request, user)
                    messages.success(
                        request, 'your profile has successfully  updated ')

                    return redirect('manageprofile')
    else:
        citydata = city.objects.all()
        singup = Singup.objects.filter(user_id=request.user.id)
        profile = Profile.objects.filter(user_id=request.user.id)
        context = {
            'citydata': citydata,
            'singup': singup,
            'profile': profile,
        }
        # return JsonResponse(list(Singup.objects.filter(user_id=request.user.id).values()), safe=False)
        return render(request, 'accounts/manageprof.html', context)


def medicalpro(request):
    return render(request, 'accounts/medical.html')

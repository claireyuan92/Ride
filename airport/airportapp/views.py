from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from .forms import *
from models import *
from django.contrib.auth import (login as auth_login,  authenticate)
from django.core.urlresolvers import reverse


@csrf_protect
def index(request):
    return render_to_response('index.html')

def volunteerPage(request):
    curr_volunteer= Volunteer.objects.filter(username=request.user)
    print curr_volunteer
    

def volunteer_register(request):

    if request.method == 'POST':
        form = v_RegistrationForm(request.POST)
        if form.is_valid():
            cplate = form.cleaned_data['carplate']
            if not Car.objects.filter(plate_number= cplate):
                newcar=Car(plate_number= cplate)
                newcar.save();
            carObject = Car.objects.filter(plate_number= cplate)[0]

            user = Volunteer.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
    			car_plate = carObject,
                #available_time_start = form.cleaned_data['available_time_start'],
                #available_time_end = form.cleaned_data['available_time_end'],
                driver_license=form.cleaned_data['driver_license'],
                isVolunteer = True,
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = v_RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )

def newstudent_register(request):

    if request.method == 'POST':
        form = s_RegistrationForm(request.POST)
        if form.is_valid():

            fnumber = form.cleaned_data['flight_number']

            if not Flight.objects.filter(flight_number = fnumber):
                newflight = Flight(flight_number = fnumber)
                newflight.save()
                print "save"
            fnumberObject = Flight.objects.filter(flight_number = fnumber)[0]
            user = NewStudent.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                #car_plate = form.cleaned_data['carplate'],
                #available_time_start = form.cleaned_data['available_time_start'],
                #available_time_end = form.cleaned_data['available_time_end'],
                flight = fnumberObject,
                isVolunteer = False,
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = s_RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )

def register_success(request):
    print request.user
    return render_to_response(
        'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/login_success')
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'registration/login.html', context)


@login_required
def login_success(request):
    curr_volunteer= RideUser.objects.filter(username=request.user)[0]

    if curr_volunteer.isVolunteer:
        return  HttpResponseRedirect('/volunteer')

    return render_to_response(
        'home.html',
    )

@login_required
def volunteerView(request):
    curr_volunteer= Volunteer.objects.filter(username=request.user)[0]
    new_student =  NewStudent.objects.all()
    
    #return HttpResponse("Volunteer:" + str(curr_volunteer))

    return render(request,'volunteer.html',{'current_user': curr_volunteer, 'new_student':new_student})


def submitPickup(request):
	checked = request.POST.getlist("checkbox")
	print checked

	return HttpResponse("submit sucess")

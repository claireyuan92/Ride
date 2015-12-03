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

#from weibo import APIClient

APP_KEY = '1234567' # app key
APP_SECRET = 'abcdefghijklmn' # app secret
CALLBACK_URL = 'http://www.example.com/callback' # callback url



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
    return HttpResponseRedirect(
        '/login_success',
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

	
    curr_user= RideUser.objects.filter(username=request.user)[0]

    if curr_user.isVolunteer:
    	return HttpResponseRedirect('/volunteer')
    else:
		return HttpResponseRedirect('/newstudent')
		


@login_required
def volunteerView(request):
    curr_user= Volunteer.objects.filter(username=request.user)[0]
    new_student =  NewStudent.objects.filter(hasPickup = False)

    return render(request,'volunteer.html',{'current_user': curr_user, 'new_student':new_student})

@login_required
def newstudentView(request):
    curr_user= NewStudent.objects.filter(username=request.user)[0]
    pickupObject =  Pickup.objects.filter(newstudent = curr_user)

    return render(request,'newstudent.html',{'current_user': curr_user, 'pickup':pickupObject})


@login_required
def submitPickup(request):
	curr_volunteer= Volunteer.objects.filter(username=request.user)[0]
	checked = request.POST.getlist("checkbox")

	if checked is not None:
		for i in checked:

			print type(curr_volunteer)
			ns = NewStudent.objects.get(username = str(i))
			ns.hasPickup = True
			ns.save()
			Pickup.objects.create(volunteer = curr_volunteer, newstudent = ns )

	return HttpResponse("submit sucess")


'''
def weibologin(request):
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	url = client.get_authorize_url()
	
	"""
	code = your.web.framework.request.get('code')
	client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
	r = client.request_access_token(code)
	access_token = r.access_token # token abc123xyz456
	expires_in = r.expires_in  #token expire http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
	# TODO: save access token
	client.set_access_token(access_token, expires_in)

	print client.statuses.user_timeline.get()
	"""
	return HttpResponseRedirect(url)
	
	#print client.statuses.update.post(status=u'OAuth 2.0 send weibo')
	#print client.statuses.upload.post(status=u'OAuth 2.0figure weibo', pic=open('/Users/michael/test.png'))
'''
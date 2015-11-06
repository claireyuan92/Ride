from django.shortcuts import render
from .models import NewStudent

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the rideapp index.")


def unpaired(request):
	unpaired_student=NewStudent.objects.all()
	return render(request,'index.html')



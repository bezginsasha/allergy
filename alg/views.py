from django.shortcuts import render
from django.http import HttpResponse

from .models import Allergy

# Create your views here.
def index(request):
	allergy_list = Allergy.objects.all()
	output = ', '.join([a.name for a in allergy_list])
	return HttpResponse(output)

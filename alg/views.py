from django.shortcuts import render
from django.http import HttpResponse

from .models import Allergy

# Create your views here.
def index(request):
	allergy_list = Allergy.objects.all()
	context = {
		'allergy_list': allergy_list
	}
	return render(request, 'alg/index.html', context)

def detail(request, allergy_id):
	a = Allergy.objects.get(id=allergy_id)
	return HttpResponse(str(a))
from django.shortcuts import render, get_object_or_404
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
	a = get_object_or_404(Allergy, id=allergy_id)
	return HttpResponse(str(a))
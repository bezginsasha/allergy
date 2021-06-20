from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .imp_alg import handle_uploaded_file, get_extension, handle_json, handle_xml

from .models import Allergy

# Create your views here.
def index(request):
	allergy_list = Allergy.objects.order_by('-anger')
	context = {
		'allergy_list': allergy_list
	}
	return render(request, 'alg/index.html', context)

def add_allergy(request):
	name = request.POST['name']

	a = Allergy(name = name)
	a.save_with_unique_handle()

	return HttpResponseRedirect(reverse('alg:index'))

def del_allergy(request):
	a = get_object_or_404(Allergy, id=request.POST['id'])
	a.delete()
	return HttpResponseRedirect(reverse('alg:index'))

def edit_allergy(request):
	a = get_object_or_404(Allergy, id=request.POST['id'])
	name = request.POST['name']
	if len(name) > 0:
		a.name = name
		a.save()
	return HttpResponseRedirect(reverse('alg:index'))

def detail(request, allergy_id):
	a = get_object_or_404(Allergy, id=allergy_id)
	return HttpResponse(str(a))

def enrage(request):
	a = get_object_or_404(Allergy, id=request.POST['id'])
	a.anger += 1
	a.save()
	return HttpResponseRedirect(reverse('alg:index'))

def imp(request):
	print(request.FILES['file'].name)
	file_name = handle_uploaded_file(request.FILES['file'])
	if file_name == None:
		return HttpResponse('not compatible format')
	file_extension = get_extension(file_name)
	if file_extension == 'json':
		alg_list = handle_json(file_name)
	elif file_extension == 'xml':
		alg_list = handle_xml(file_name)
	Allergy.save_list(alg_list)
	return HttpResponse('ok')

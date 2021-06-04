from django.urls import path

from .  import views

app_name = 'alg'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:allergy_id>', views.detail, name='detail'),
	path('enrage', views.enrage, name='enrage'),
	path('add_allergy', views.add_allergy, name='add_allergy'),
	path('del_allergy', views.del_allergy, name='del_allergy'),
	path('edit_allergy', views.edit_allergy, name='edit_allergy'),
]
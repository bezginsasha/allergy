from django.urls import path

from .  import views

app_name = 'alg'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:allergy_id>', views.detail, name='detail'),
	path('enrage', views.enrage, name='enrage'),
]
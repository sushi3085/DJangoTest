from django.urls import path
from django.conf.urls import url
from . import views # import views.py file in this folder

urlpatterns = [
	path('', views.index, name = "index"),
	path('text/', views.testIndex, name = "text"),
]
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("<h1>alksjdlkj</h1>")

def testIndex(request):
	print(request.GET.get('person', 'no one'))
	result = "<br>"
	for i,j in request.GET.items():
		result += i + " = " + j+"<br>"
	
	return HttpResponse(f"<h1>DASDAS<br>{result}</h1>")

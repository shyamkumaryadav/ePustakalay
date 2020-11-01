from django.shortcuts import render, HttpResponse

def index(request):
	return HttpResponse("<h1>Management index file<h1>", status=200)

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Menu Main list")


def categories(request, catid):
    if catid > 9:
        return redirect('main', permanent=True)
    return HttpResponse(f"<h1>Catid {catid}</h1><p></p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Custom page not found</h1>")

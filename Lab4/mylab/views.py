from django.shortcuts import render
from django.http import HttpResponse
taxRate= 0.15
def default_views(request):
    return HttpResponse("<html><body><h1>This is a site to calculate tax!<h1><body><html>")
def calculateTaxRate(request, amount):
    totalPrice =( amount + ( amount*taxRate))
    return HttpResponse(f"<html><body><h1>the amount is: {totalPrice}<h1><body><html>")
def taxRateView(request):
    return HttpResponse(f"<html><body><h1>{taxRate}<h1><body><html>")
# Create your views here.

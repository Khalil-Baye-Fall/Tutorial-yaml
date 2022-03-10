from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Welcome(request):
    return HttpResponse("hello From Kubernetesmwith some changes!")



def SecondPage(request):
    return HttpResponse("Tes second page in Kubernetes with some changes")

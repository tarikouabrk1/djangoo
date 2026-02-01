from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>hello i am tarik</h1>")

def about(request):
    return HttpResponse("<h2>i am here </h1>")
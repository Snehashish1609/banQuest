from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, from demo index!")

def home(request):
    return HttpResponse("Hello, from demo home!")
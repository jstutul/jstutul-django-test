from django.shortcuts import HttpResponse
import os
from dotenv import load_dotenv
load_dotenv() 
def home(request):
    return HttpResponse(os.getenv("NAME"))

def setV(request):
    os.environ['NAME'] = 'TUTUL'
    return HttpResponse("DONE")

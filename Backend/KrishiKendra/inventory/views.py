from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.
def get_date_time(request):
    time = datetime.now()
    return HttpResponse(f"<h1>The Current date time is: {str(time)} </h1>")
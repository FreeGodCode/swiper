from django.shortcuts import render

from lib.http import render_json


# Create your views here.
def index(request):
    return render_json(None)

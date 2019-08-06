from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
import base64
from django.core.files.base import ContentFile
from subprocess import Popen, PIPE
import json
import os
from textblob import TextBlob

def index(request):
    return render(request, 'parent.html')

def feature(request):
    return render(request, 'feature.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def process_word(request):
    para = request.POST.get('review')
    para = (TextBlob(str(para))).polarity
    if float(para) > 0:
	    return HttpResponse(True)
    else:
    	return HttpResponse(False)

def features(request):
    return render(request, 'feature.html')

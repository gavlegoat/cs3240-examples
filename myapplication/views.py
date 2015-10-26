from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from myapplication.forms import UploadFileForm

def index(request):
    return HttpResponseRedirect("upload")

def success(request):
    return HttpResponse("Successfully uploaded file")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open("test.txt", "wb+") as dest:
                for chunk in request.FILES['file'].chunks():
                    dest.write(chunk)
            return HttpResponseRedirect("success")
    else:
        form = UploadFileForm()
    return render_to_response(
        'upload.html',
        {'form': form},
        context_instance=RequestContext(request))

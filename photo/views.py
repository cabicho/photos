from django.shortcuts import render
from photo.models import PhotoForm


# Create your views here.
def upload(request):
    form = PhotoForm
    return render(request, 'photo/upload.html', {'form': form})

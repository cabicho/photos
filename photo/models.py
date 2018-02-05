from django.db import models
from django.forms import ModelForm


class Photo(models.Model):
    tags = models.CharField(max_length=150)
    image = models.ImageField();
    


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['tags', 'image']

from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^upload/', views.upload, name="upload")
]

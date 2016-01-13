from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^nrg/', views.bereken, name='bereken'),
]

from django.urls import path

from .views import index as iv
from .views import despesa as dv

urlpatterns = [
    path('', iv.index, name="index"),
    path('despesa/nova', dv.nova, name="despesa_nova"),
    path('despesa/', dv.despesa, name="despesa")
]
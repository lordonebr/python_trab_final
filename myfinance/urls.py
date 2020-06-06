from django.urls import path

from .views import index as iv

urlpatterns = [
    path('', iv.index, name="index")
]
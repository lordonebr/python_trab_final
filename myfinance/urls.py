from django.urls import path

from .views import index as iv
from .views import despesa as dv
from .views import receita as rv

urlpatterns = [
    path('', iv.index, name="index"),

    path('despesa/nova', dv.nova, name="despesa_nova"),
    path('despesa/', dv.despesa, name="despesa"),

    path('receita/nova', rv.nova, name="receita_nova"),
    path('receita/', rv.receita, name="receita")
]
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

from ..models import Despesa

@require_http_methods(["GET"])
def despesas(request):
    despesasPendentes = Despesa.objects.filter(data_pagamento=None)
    context = GetContext(despesasPendentes , '')
    
    return render(request, 'relatorioDespesas.html', context)


@require_http_methods(["POST"])    
@csrf_exempt
def despesasFiltro(request):
    dataFiltro = request.POST['data_filtro']
    
    despesasPendentes = Despesa.objects.filter(data_pagamento=None, data_vencimento__lte=dataFiltro)
    context = GetContext(despesasPendentes, dataFiltro)

    return render(request, 'relatorioDespesas.html', context)


def GetContext(despesasPendentes, dateMax):
    valorTotal = 0
    for despesa in despesasPendentes:
        dtVencimento = '%s/%s/%s' % (despesa.data_vencimento.strftime("%d"), despesa.data_vencimento.strftime("%m"), despesa.data_vencimento.strftime("%Y"))
        despesa.data_vencimento = dtVencimento
        valorTotal = valorTotal + despesa.valor
    
    dateMaxBr = ""
    if(dateMax != ""):
        dateTemp = datetime.strptime(dateMax, '%Y-%m-%d').date()
        dateMaxBr = '%s/%s/%s' % (dateTemp.strftime("%d"), dateTemp.strftime("%m"), dateTemp.strftime("%Y"))

    context = {'despesas' : despesasPendentes,
                'valorTotal' : valorTotal,
                'dateMax' : dateMax,
                'dateMaxBr' : dateMaxBr}

    return context
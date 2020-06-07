from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from datetime import date
from django.views.decorators.csrf import csrf_exempt

from ..models import Despesa

@require_http_methods(["GET"])
def nova(request):

    dtToday = '%s-%s-%s' % (date.today().strftime("%Y"), date.today().strftime("%m"), date.today().strftime("%d"))
    despesa = Despesa(classificacao='OU',
                      data_pagamento='',
                      data_vencimento=dtToday,
                      descricao='',
                      formaPagamento='O',
                      situacao='AP',
                      valor=''
                    )
    context = { 
        'despesa' : despesa,
        'classificacoes' : [],
        'formasPagamento' : [],
        'situacoes' : []
    }
    
    fieldsClassificacao = Despesa.CLASSIFICACAO_CHOICES
    for field, value in fieldsClassificacao:
        itemClassificacao = {"key" : field, "value" : value}
        context["classificacoes"].append(itemClassificacao)

    fieldsFormasPagamento = Despesa.FORMA_PAGAMENTO_CHOICES
    for field, value in fieldsFormasPagamento:
        itemFormaPagamento = {"key" : field, "value" : value}
        context["formasPagamento"].append(itemFormaPagamento)

    fieldsSituacoes = Despesa.SITUACAO_CHOICES
    for field, value in fieldsSituacoes:
        itemSituacao = {"key" : field, "value" : value}
        context["situacoes"].append(itemSituacao)

    return render(request, 'despesa.html', context)


@require_http_methods(["POST"])    
@csrf_exempt
def despesa(request):
    valor = request.POST['valor']

    dataPagamento = request.POST['data_pagamento']
    if(dataPagamento == ""):
        dataPagamento = None

    despesa = Despesa(classificacao=request.POST['classificacao'],
                      data_pagamento=dataPagamento,
                      data_vencimento=request.POST['data_vencimento'],
                      descricao=request.POST['descricao'],
                      formaPagamento=request.POST['formaPagamento'],
                      situacao=request.POST['situacao'],
                      valor=valor
                    )

    despesa.save()

    context = {
            'message' : 'Despesa cadastrada com sucesso!'
    }
    return render(request, 'despesa.html', context)

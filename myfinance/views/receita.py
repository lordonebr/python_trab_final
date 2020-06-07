from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from datetime import date
from django.views.decorators.csrf import csrf_exempt

from ..models import Receita

@require_http_methods(["GET"])
def nova(request):

    dtToday = '%s-%s-%s' % (date.today().strftime("%Y"), date.today().strftime("%m"), date.today().strftime("%d"))
    receita = Receita(classificacao='OU',
                      data_expectativa=dtToday,
                      data_recebimento='',
                      descricao='',
                      formaRecebimento='O',
                      situacao='AR',
                      valor=''
                    )
    context = { 
        'receita' : receita,
        'classificacoes' : [],
        'formasRecebimento' : [],
        'situacoes' : []
    }
    
    fieldsClassificacao = Receita.CLASSIFICACAO_CHOICES
    for field, value in fieldsClassificacao:
        itemClassificacao = {"key" : field, "value" : value}
        context["classificacoes"].append(itemClassificacao)

    fieldsFormasRecebimento = Receita.FORMA_RECEBIMENTO_CHOICES
    for field, value in fieldsFormasRecebimento:
        itemFormaRecebimento = {"key" : field, "value" : value}
        context["formasRecebimento"].append(itemFormaRecebimento)

    fieldsSituacoes = Receita.SITUACAO_CHOICES
    for field, value in fieldsSituacoes:
        itemSituacao = {"key" : field, "value" : value}
        context["situacoes"].append(itemSituacao)

    return render(request, 'receita.html', context)


@require_http_methods(["POST"])    
@csrf_exempt
def receita(request):
    valor = request.POST['valor']

    dataRecebimento = request.POST['data_recebimento']
    if(dataRecebimento == ""):
        dataRecebimento = None

    receita = Receita(classificacao=request.POST['classificacao'],
                      data_expectativa=request.POST['data_expectativa'],
                      data_recebimento=dataRecebimento,
                      descricao=request.POST['descricao'],
                      formaRecebimento=request.POST['formaRecebimento'],
                      situacao=request.POST['situacao'],
                      valor=valor
                    )

    receita.save()

    context = {
            'message' : 'Receita cadastrada com sucesso!'
    }
    return render(request, 'receita.html', context)

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from ..models import Conf, Despesa, Receita
import operator

@require_http_methods(["GET", "POST"])
@csrf_exempt
def index(request):
    if(request.method=="GET"):
        saldoInicial = loadSaldoInicial()
        saldoAtual = saldoInicial

        fluxo = initFluxo(saldoInicial)
        for periodo in fluxo:
            saldoAtual = fluxo[periodo]['saldoFinal']
            break

        # iterate fluxo
        # https://stackoverflow.com/questions/16616260/django-template-context-for-loop-traversal
        context = {'getSaldoInicial' : saldoInicial, 'fluxo' : fluxo, 'saldoAtual' : saldoAtual}
        #print(f"""context= {context}""")
        return render(request, 'index.html', context)
    elif(request.method=="POST"):
        saldoInicial = request.POST['saldoInicial']
        print(f"""saldoInicial= {saldoInicial}""")
        conf = Conf(saldoInicial=saldoInicial)
        conf.save()

        saldoInicial = loadSaldoInicial()
        
        context = {'getSaldoInicial' : saldoInicial}
        print(f"""context= {context}""")
        return render(request, 'index.html', context)


def loadSaldoInicial():
    saldoInicial = None
    searchSaldoInicial = Conf.objects.all()
    if(searchSaldoInicial.count() >= 1):
        saldoInicial = searchSaldoInicial[0].saldoInicial

    return saldoInicial


def initFluxo(saldoInicial):
    if(saldoInicial == None):
        return {}

    fluxo = {}
    fluxo = setResumoReceitas(fluxo)
    fluxo = setResumoDespesas(fluxo)
    fluxo = setSaldoIniFinLuc(fluxo, saldoInicial)
    fluxo = setReceitasOrder(fluxo)
    fluxo = setDespesasOrder(fluxo)

    return fluxo


def createFluxoVazio(fluxo, periodo):
    fluxo[periodo] = {  'saldoReceber' : 0, 
                        'saldoRecebido' : 0, 
                        'saldoPagar' : 0, 
                        'saldoPago' : 0,
                        'saldoInicial' : 0,
                        'saldoFinal' : 0,
                        'lucratividade' : 0,
                        'saldoPrevisto' : 0,
                        "receitas" : [],
                        "despesas" : []}
    return fluxo

def setResumoReceitas(fluxo):
    resultReceitas = Receita.objects.all().order_by('-data_expectativa')
    for receita in resultReceitas:
        periodo = '%s/%s' % (receita.data_expectativa.strftime("%m"), receita.data_expectativa.strftime("%Y"))
        if periodo not in fluxo:
            fluxo = createFluxoVazio(fluxo, periodo)
        
        if(receita.situacao == "PR"):
            fluxo[periodo]['saldoRecebido'] = fluxo[periodo]['saldoRecebido'] + receita.valor
        else:
            fluxo[periodo]['saldoReceber'] = fluxo[periodo]['saldoReceber'] + receita.valor

    return fluxo


def setResumoDespesas(fluxo):
    resultDespesas = Despesa.objects.all().order_by('-data_vencimento')
    for despesa in resultDespesas:
        periodo = '%s/%s' % (despesa.data_vencimento.strftime("%m"), despesa.data_vencimento.strftime("%Y"))
        if periodo not in fluxo:
            fluxo = createFluxoVazio(fluxo, periodo)

        if(despesa.situacao == "PG"):
            fluxo[periodo]['saldoPago'] = fluxo[periodo]['saldoPago'] + despesa.valor
        else:
            fluxo[periodo]['saldoPagar'] = fluxo[periodo]['saldoPagar'] + despesa.valor

    return fluxo

def setSaldoIniFinLuc(fluxo, saldoInicial):
    setSaldoInicial = False
    saldoFinalMesAnterior = 0
    for periodo in reversed(fluxo):
        if(not setSaldoInicial):
            fluxo[periodo]['saldoInicial'] =  saldoInicial
            setSaldoInicial = True
        else:
            fluxo[periodo]['saldoInicial'] =  saldoFinalMesAnterior

        fluxo[periodo]['saldoFinal'] = fluxo[periodo]['saldoInicial'] + fluxo[periodo]['saldoRecebido'] - fluxo[periodo]['saldoPago']
        fluxo[periodo]['lucratividade'] = fluxo[periodo]['saldoFinal'] - fluxo[periodo]['saldoInicial']
        saldoFinalMesAnterior = fluxo[periodo]['saldoFinal']
        fluxo[periodo]['saldoPrevisto'] = fluxo[periodo]['saldoFinal'] + fluxo[periodo]['saldoReceber'] - fluxo[periodo]['saldoPagar']
    
    return fluxo


def setReceitasOrder(fluxo):
    receitas = list(Receita.objects.all())
    receitas.sort(key=operator.methodcaller('get_classificacao_display'))
    for receita in receitas:
        periodo = '%s/%s' % (receita.data_expectativa.strftime("%m"), receita.data_expectativa.strftime("%Y"))
        dtExpectativa = '%s/%s/%s' % (receita.data_expectativa.strftime("%d"), receita.data_expectativa.strftime("%m"), receita.data_expectativa.strftime("%Y"))
        receita.data_expectativa = dtExpectativa
        if(receita.data_recebimento):
            dtrecebimento = '%s/%s/%s' % (receita.data_recebimento.strftime("%d"), receita.data_recebimento.strftime("%m"), receita.data_recebimento.strftime("%Y"))
            receita.data_recebimento = dtrecebimento

        fluxo[periodo]['receitas'].append(receita)

    return fluxo


def setDespesasOrder(fluxo):
    despesas = list(Despesa.objects.all())
    despesas.sort(key=operator.methodcaller('get_classificacao_display'))
    for despesa in despesas:
        periodo = '%s/%s' % (despesa.data_vencimento.strftime("%m"), despesa.data_vencimento.strftime("%Y"))
        dtVencimento = '%s/%s/%s' % (despesa.data_vencimento.strftime("%d"), despesa.data_vencimento.strftime("%m"), despesa.data_vencimento.strftime("%Y"))
        despesa.data_vencimento = dtVencimento
        if(despesa.data_pagamento):
            dtpagamento = '%s/%s/%s' % (despesa.data_pagamento.strftime("%d"), despesa.data_pagamento.strftime("%m"), despesa.data_pagamento.strftime("%Y"))
            despesa.data_pagamento = dtpagamento
        
        fluxo[periodo]['despesas'].append(despesa)

    return fluxo

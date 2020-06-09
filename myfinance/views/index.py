from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from ..models import Conf, Despesa, Receita

@require_http_methods(["GET", "POST"])
@csrf_exempt
def index(request):
    if(request.method=="GET"):
        saldoInicial = loadSaldoInicial()

        fluxo = initFluxo(saldoInicial)
        print(f"""fluxo = {fluxo}""")

        # iterate fluxo
        # https://stackoverflow.com/questions/16616260/django-template-context-for-loop-traversal
        context = {'getSaldoInicial' : saldoInicial, 'fluxo' : fluxo}
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
    resultReceitas = Receita.objects.all().order_by('-data_expectativa')
    for receita in resultReceitas:
        periodo = '%s/%s' % (receita.data_expectativa.strftime("%m"), receita.data_expectativa.strftime("%Y"))
        if periodo not in fluxo:
            fluxo = createFluxoVazio(fluxo, periodo)
        
        if(receita.situacao == "PR"):
            fluxo[periodo]['saldoRecebido'] = fluxo[periodo]['saldoRecebido'] + receita.valor
        else:
            fluxo[periodo]['saldoReceber'] = fluxo[periodo]['saldoReceber'] + receita.valor

    resultDespesas = Despesa.objects.all().order_by('-data_vencimento')
    for despesa in resultDespesas:
        periodo = '%s/%s' % (despesa.data_vencimento.strftime("%m"), despesa.data_vencimento.strftime("%Y"))
        if periodo not in fluxo:
            fluxo = createFluxoVazio(fluxo, periodo)

        if(despesa.situacao == "PG"):
            fluxo[periodo]['saldoPago'] = fluxo[periodo]['saldoPago'] + despesa.valor
        else:
            fluxo[periodo]['saldoPagar'] = fluxo[periodo]['saldoPagar'] + despesa.valor

    fluxo = setSaldoIniFinLuc(fluxo, saldoInicial)

    return fluxo


def createFluxoVazio(fluxo, periodo):
    fluxo[periodo] = {  'saldoReceber' : 0, 
                        'saldoRecebido' : 0, 
                        'saldoPagar' : 0, 
                        'saldoPago' : 0,
                        'saldoInicial' : 0,
                        'saldoFinal' : 0,
                        'lucratividade' : 0}
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
    
    return fluxo
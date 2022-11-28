from django import forms
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def realizarcalculo(request):
    salario = formulario(request.GET)
    if salario.is_valid():
        salario = salario.data['salario']
        
        try:
            return render(request, 'index.html', context=ejecutarcalculo(salario))
        except:
            return render(request, 'index.html', context={"error": True})
    else:
        pass

class formulario(forms.Form):
    salario = forms.FloatField(label='Salario')

def ejecutarcalculo(salario):

    def resetmonto(monto): return "{:,}".format(monto)
    
    def porcentaje(numero, p): return float(numero) / 100 * float(p)

    promsalario = float(salario)
    minsalario = 1000000
    transsubsidio = 117.172

    saludobli = porcentaje(promsalario, 4)

    solidFundCount = promsalario / minsalario
    if solidFundCount > 2:
        transsubsidio = 0

    cantidadneta = promsalario - saludobli * 2

    return {
        "promsalario": resetmonto(promsalario),
        "transsubsidio": resetmonto(transsubsidio),
        "saludobli": resetmonto(saludobli),
        "cantidadneta": resetmonto(cantidadneta),
    }


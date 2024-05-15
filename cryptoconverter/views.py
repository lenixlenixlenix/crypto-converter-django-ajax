from django.views.generic import View, TemplateView
from django.shortcuts import render
from django.http import JsonResponse

from .forms import CurrencyConverterForm
from .functions import CryptoClass
# Create your views here.

class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = CurrencyConverterForm()
        return context

def submit(request):
    conv_from = int(request.GET.get('convert_from'))
    conv_to = int(request.GET.get('convert_to'))
    amount = float(request.GET.get('amount'))

    converted = CryptoClass.convert_crypto(conv_from, conv_to, amount)

    response = {
        'converted': converted
    }

    return JsonResponse(response)

def update(request):
    print("CHECK CHECK")
    CryptoClass.update()

    response = {
        "success": "Successfuly updated"
    }
    return JsonResponse(response)




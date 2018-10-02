from django.http import HttpResponse
from django.shortcuts import render
from almacen.utils import dame_token, dame_movimientos, agrega_picking

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {}
    context["resp_token"] = dame_token()
    token = context["resp_token"]["token"]
    movimientos = dame_movimientos(token)
    context["resp_movimientos"] = agrega_picking(movimientos, token)


    return render(request, 'almacen/index.html', context)
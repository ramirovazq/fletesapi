from django.http import HttpResponse
from django.shortcuts import render
from almacen.utils import dame_token

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {}
    context["test"] = "ping"
    context["token"] = dame_token()

    return render(request, 'almacen/index.html', context)
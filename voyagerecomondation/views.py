from django.shortcuts import render
from moteurderecherche import *

# Create your views here.
def index(request):
    budget = request.POST['budget']
    saison = request.POST['saison']
    interet = request.POST['interet']
    preference = request.POST['preference']
    compagnie = request.POST['compagnie']
    climat = request.POST['climat']
    continent = request.POST['continent']
    result = ""
    response = KnowledBase(data['data']).response()
    print(response)
    return render(request, 'index.html', {"result": result})

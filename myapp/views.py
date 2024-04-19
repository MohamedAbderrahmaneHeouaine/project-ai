from django.http import HttpResponse
from django.shortcuts import render
from .models import Feature
from django import template
from .inferenceSystem import final_Distinations
# Create your views here.
def index(request):
    feature1 =Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'This is Fast'
    return render(request, 'acceuil.html',{'feature':feature1})
def goForm(request):
    return render(request, 'formulaire.html')
register = template.Library()
@register.filter
def submit_form(request):
    if request.method == 'POST':
        # Process the form data
        if request.POST.get('budget'):
            budget = request.POST.get('budget')
        else:
            budget = ""
        if request.POST.get('interet'):
            interet = request.POST.get('interet')
        else:
            interet = ""
        if request.POST.get('saison'):
            saison = request.POST.get('saison')
        else:
            saison = ""
        if request.POST.get('climat'):
            climat = request.POST.get('climat')
        else:
            climat = ""
        if request.POST.get('compagnie'):
            compagnie = request.POST.get('compagnie')
        else:
            compagnie = ""

        input_data = {
            'budget': budget,
            'interet': interet,
            'compagnie': compagnie,
            'climat': climat,
            'saison': saison,
        }
        list_data = [budget, interet, compagnie, climat, saison]
        print(input_data)
        dist = final_Distinations(input_data, list_data)
        print(dist)

        return render(request, 'showPage.html', {'values': enumerate(dist[:6], start=1)})


def counter(request):
    words = request.POST['text']
    return render(request, 'counter.html', {'words': words})

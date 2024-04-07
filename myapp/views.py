from django.http import HttpResponse
from django.shortcuts import render
from .models import Feature
from .moteurderecherche import returnDistination
# Create your views here.
def index(request):
    feature1 =Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'This is Fast'
    return render(request, 'acceuil.html',{'feature':feature1})
def goForm(request):
    return render(request, 'formulaire.html')
def submit_form(request):
    if request.method == 'POST':
        # Process the form data
        if request.POST.get('budget'):
            budget = request.POST.get('budget')
        else:
            budget = ""
        if request.POST.get('preference'):
            preference = request.POST.get('preference')
        else:
            preference = ""
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
        if request.POST.get('continent'):
            continent = request.POST.get('continent')
        else:
            continent = ""
        # Retrieve other form data as needed

        # Perform any additional processing (e.g., save to database)

        print("budget")
        print(budget)
        input_data = {
            'budget': budget,
            'preference': preference,
            'interet': interet,
            'compagnie': compagnie,
            'climat': climat,
            'continent': continent,
            'saison': 'Toutes',
        }
        print(input_data)

        dist = ""
        try:
            reponse = returnDistination(input_data)
            if(reponse):
                for value in reponse[0].values():
                    dist = value
        except TypeError:
            print("pas de distination")

        # Render a template and pass context data
        return render(request, 'resultat.html', {'value': dist})


def counter(request):
    words = request.POST['text']
    return render(request, 'counter.html', {'words': words})

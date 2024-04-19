from aima3.logic import *

# Définir une knowledge base
dest_kb = FolKB()

# Ensemble de faits
# kb.tell(expr('Compagnie(Seul)'))
# kb.tell(expr('Interet(Gastronomie)'))
# kb.tell(expr('Budget(Moyen)'))
# kb.tell(expr('Climat(Midétérranéen)'))
# kb.tell(expr('Saison(Eté)'))


# Règles pour remplir la base des connaissances

# Règles pour définir que chaque saison est incluse dans toutes les saisons
dest_kb.tell(expr('Saison(Hiver)==>Saison(Toutes)'))
dest_kb.tell(expr('Saison(Eté)==>Saison(Toutes)'))
dest_kb.tell(expr('Saison(Printemps)==>Saison(Toutes)'))
dest_kb.tell(expr('Saison(Automne)==>Saison(Toutes)'))

# Regles pour définir que le budget moyen est inclu dans l'élevé
dest_kb.tell(expr('Budget(Moyen)==>Budget(Elevé)'))

# Regles pour définir que la compagnie seul est incluse dans la compagnie groupe
dest_kb.tell(expr('Compagnie(Groupe)==>Compagnie(Seul)'))

# Regles pour définir l'interet
dest_kb.tell(expr('Interet(Tourisme)==>Interet(Aventure)'))
dest_kb.tell(expr('Interet(Tourisme)==>Interet(Relaxation)'))
dest_kb.tell(expr('Interet(Tourisme)==>Interet(Découverte)'))
dest_kb.tell(expr('Interet(Tourisme)==>Interet(Gastronomie)'))

#-----------Regles definissant les continents-----------------------------------------------#

#Continenet Europe
dest_kb.tell(expr('Climat(Midétérranéen)&Saison(Toutes)==>Continent(Europe)'))
dest_kb.tell(expr('Climat(Océanique)&Saison(Toutes)==>Continent(Europe)'))
dest_kb.tell(expr('Climat(Subtropical)&Saison(Toutes)==>Continent(Europe)'))
dest_kb.tell(expr('Climat(Modéré)&Saison(Toutes)==>Continent(Europe)'))

#Continenet Asie
dest_kb.tell(expr('Climat(Tropical)&Saison(Toutes)==>Continent(Asie)'))
dest_kb.tell(expr('Climat(Subropical)&Saison(Toutes)==>Continent(Asie)'))
dest_kb.tell(expr('Climat(Continenetal)&Saison(Toutes)==>Continent(Asie)'))

#Continenet Amérique
dest_kb.tell(expr('Climat(Subropical)&Saison(Toutes)==>Continent(Amérique)'))
dest_kb.tell(expr('Climat(Océanique)&Saison(Toutes)==>Continent(Amérique)'))
dest_kb.tell(expr('Climat(Modéré)&Saison(Toutes)==>Continent(Amérique)'))
dest_kb.tell(expr('Climat(Tropical)&Saison(Toutes)==>Continent(Amérique)'))
dest_kb.tell(expr('Climat(Modéré)&Saison(Toutes)==>Continent(Amérique)'))

#Continenet Afrique
dest_kb.tell(expr('Climat(Midétérranéen)&Saison(Toutes)==>Continent(Afrique)'))
dest_kb.tell(expr('Climat(Subropical)&Saison(Toutes)==>Continent(Afrique)'))
dest_kb.tell(expr('Climat(Désertique)&Saison(Toutes)==>Continent(Afrique)'))
dest_kb.tell(expr('Climat(Océanique)&Saison(Toutes)==>Continent(Afrique)'))

#----------------------------------------------------------------------------------------------#

#-----------Règles définissant les destinations selon la compagnie et la préférence------------#


#Destination "Alger"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Alger)'))

#Destination "Tunis"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Tunis)'))

#Destination "Marrakech"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Marrakech)'))

#Destination "Le Caire"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Caire)'))
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Gastronomie)==>Destination(Caire)'))
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Aventure)==>Destination(Caire)'))

#Destination "Singapour"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Singapour)'))

#Destination "Bali"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Relaxation)==>Destination(Bali)'))
dest_kb.tell(expr('Compagnie(Seul)&Interet(Aventure)==>Destination(Bali)'))
dest_kb.tell(expr('Compagnie(Seul)&Interet(Découverte)==>Destination(Bali)'))

#Destination "Istabul"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Istanbul)'))

#Destination "NewYork"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(NewYork)'))

#Destination "Mexico"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Gastronomie)==>Destination(Mexico)'))
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Mexico)'))

#Destination "Rome"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Gastronomie)==>Destination(Rome)'))
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Rome)'))

#Destination "Tokyo"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Tokyo)'))
dest_kb.tell(expr('Compagnie(Seul)&Interet(Découverte)==>Destination(Tokyo)'))
dest_kb.tell(expr('Compagnie(Seul)&Interet(Gastronomie)==>Destination(Tokyo)'))

#Destination "Luminaria"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Relaxation)==>Destination(Luminaria)'))
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Luminaria)'))

#Destination "Varna"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Relaxation)==>Destination(Varna)'))
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Varna)'))

#Destination "Monaco"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Monaco)'))

#Destination "Kilimandjaro"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Aventure)==>Destination(Kilimandjaro)'))

#Destination "BuenosAires"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(BuenosAires)'))
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(BuenosAires)'))

#Destination "Vancouver"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Vancouver)'))
dest_kb.tell(expr('Compagnie(Seul)&Interet(Tourisme)==>Destination(Vancouver)'))

#Destination "RioDeJanerio"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(RioDeJanerio)'))

#Destination "BangKok"
dest_kb.tell(expr('Compagnie(Seul)&Interet(Découverte)==>Destination(BangKok)'))
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(BangKok)'))

#Destination "Séoul"
dest_kb.tell(expr('Compagnie(Seul)&Interet(Découverte)==>Destination(Séoul)'))

#Destination "Alta"
dest_kb.tell(expr('Compagnie(Seul)&Interet(Découverte)==>Destination(Alta)'))
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Alta)'))

#Destination "Caraibes"
dest_kb.tell(expr('Compagnie(Seul)&Interet(Relaxation)==>Destination(Caraibes)'))

#Destination "Munich"
dest_kb.tell(expr('Compagnie(Seul)&Interet(Découverte)==>Destination(Munich)'))

#Destination "IleMaurice"
dest_kb.tell(expr('Compagnie(Groupe)&Interet(Relaxation)==>Destination(IleMaurice)'))

#------------------------------------------------------------------------------------------------#

#-----------Règles définissant les destinations selon le continent et le budget------------------#


#Destinations D'Europe
dest_kb.tell(expr('Continent(Europe)&Budget(Eleve)==>Destination(Paris)'))
dest_kb.tell(expr('Continent(Europe)&Budget(Eleve)==>Destination(Rome)'))
dest_kb.tell(expr('Continent(Europe)&Budget(Moyen)==>Destination(Istanbul)'))
dest_kb.tell(expr('Continent(Europe)&Budget(Elevé)==>Destination(Luminaria)'))
dest_kb.tell(expr('Continent(Europe)&Budget(Moyen)==>Destination(Varna)'))
dest_kb.tell(expr('Continent(Europe)&Budget(Elevé)==>Destination(Monaco)'))
dest_kb.tell(expr('Continent(Europe)&Budget(Elevé)==>Destination(Alta)'))
dest_kb.tell(expr('Continent(Europe)&Budget(Elevé)==>Destination(Munich)'))

#Destinations D'Afrique
dest_kb.tell(expr('Continent(Afrique)&Budget(Moyen)==>Destination(Marrakech)'))
dest_kb.tell(expr('Continent(Afrique)&Budget(Moyen)==>Destination(Caire)'))
dest_kb.tell(expr('Continent(Afrique)&Budget(Moyen)==>Destination(Alger)'))
dest_kb.tell(expr('Continent(Afrique)&Budget(Elevé)==>Destination(Kilimandjaro)'))
dest_kb.tell(expr('Continent(Afrique)&Budget(Moyen)==>Destination(Tunis)'))
dest_kb.tell(expr('Continent(Afrique)&Budget(Moyen)==>Destination(IleMaurice)'))

#Destinations D'Asie
dest_kb.tell(expr('Continent(Asie)&Budget(Elevé)==>Destination(Tokyo)'))
dest_kb.tell(expr('Continent(Asie)&Budget(Elevé)==>Destination(Singapour)'))
dest_kb.tell(expr('Continent(Asie)&Budget(Moyen)==>Destination(Istanbul)'))
dest_kb.tell(expr('Continent(Asie)&Budget(Moyen)==>Destination(Bali)'))
dest_kb.tell(expr('Continent(Asie)&Budget(Moyen)==>Destination(BangKok)'))
dest_kb.tell(expr('Continent(Asie)&Budget(Moyen)==>Destination(Séoul)'))

#Destinations D'Amérique
dest_kb.tell(expr('Continent(Amérique)&Budget(Moyen)==>Destination(Mexico)'))
dest_kb.tell(expr('Continent(Amérique)&Budget(Elevé)==>Destination(NewYork)'))
dest_kb.tell(expr('Continent(Amérique)&Budget(Moyen)==>Destination(BuenosAires)'))
dest_kb.tell(expr('Continent(Amérique)&Budget(Moyen)==>Destination(Vancouver)'))
dest_kb.tell(expr('Continent(Amérique)&Budget(Moyen)==>Destination(RioDeJanerio)'))
dest_kb.tell(expr('Continent(Amérique)&Budget(Moyen)==>Destination(Caraibes)'))

#------------------------------------------------------------------------------------------------------#


from aima3.logic import *

#Définir une knowledge base
kb=FolKB()

#Ensemble de faits
kb.tell(expr('Compagnie(Seul)'))
kb.tell(expr('Interet(Gastronomie)'))
kb.tell(expr('Budget(Moyen)'))
kb.tell(expr('Climat(Midétérranéen)'))
kb.tell(expr('Saison(Eté)'))


#Règles pour remplir la base des connaissances

#Règles pour définir que chaque saison est incluse dans toutes les saisons
kb.tell(expr('Saison(Hiver)==>Saison(Toutes)'))
kb.tell(expr('Saison(Eté)==>Saison(Toutes)'))
kb.tell(expr('Saison(Printemps)==>Saison(Toutes)'))
kb.tell(expr('Saison(Automne)==>Saison(Toutes)'))

#Regles pour définir que le budget moyen est inclu dans l'élevé
kb.tell(expr('Budget(Moyen)==>Budget(Elevé)'))

#Regles pour définir que la compagnie seul est incluse dans la compagnie groupe
kb.tell(expr('Compagnie(Groupe)==>Compagnie(Seul)'))

#Regles pour définir l'interet
kb.tell(expr('Interet(Tourisme)==>Interet(Aventure)'))
kb.tell(expr('Interet(Tourisme)==>Interet(Relaxation)'))
kb.tell(expr('Interet(Tourisme)==>Interet(Découverte)'))
kb.tell(expr('Interet(Tourisme)==>Interet(Gastronomie)'))


#-----------Regles definissant les continents-------------------------#
kb.tell(expr('Climat(Midétérranéen)&Saison(Toutes)==>Continent(Europe)'))
kb.tell(expr('Climat(Océanique)&Saison(Toutes)==>Continent(Europe)'))

kb.tell(expr('Climat(Tropical)&Saison(Toutes)==>Continent(Asie)'))
kb.tell(expr('Climat(Subropical)&Saison(Toutes)==>Continent(Asie)'))

kb.tell(expr('Climat(Subropical)&Saison(Toutes)==>Continent(Amérique)'))
kb.tell(expr('Climat(Modéré)&Saison(Toutes)==>Continent(Amérique)'))

kb.tell(expr('Climat(Midétérranéen)&Saison(Toutes)==>Continent(Afrique)'))
kb.tell(expr('Climat(Subropical)&Saison(Toutes)==>Continent(Afrique)'))
kb.tell(expr('Climat(Désertique)&Saison(Toutes)==>Continent(Afrique)'))

#Règles définissant les destinations selon la compagnie et la préférence
#-------------------------------------------------------------#
kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Alger)'))
kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Marrakech)'))
kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Caire)'))
kb.tell(expr('Compagnie(Groupe)&Interet(Gastronomie)==>Destination(Caire)'))
kb.tell(expr('Compagnie(Groupe)&Interet(Aventure)==>Destination(Caire)'))

kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Singapour)'))
kb.tell(expr('Compagnie(Groupe)&Interet(Relaxation)==>Destination(Bali)'))
kb.tell(expr('Compagnie(Seul)&Interet(Aventure)==>Destination(Bali)'))

kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Istanbul)'))
kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(NewYork)'))

kb.tell(expr('Compagnie(Groupe)&Interet(Gastronomie)==>Destination(Mexico)'))
kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Mexico)'))

kb.tell(expr('Compagnie(Groupe)&Interet(Gastronomie)==>Destination(Rome)'))
kb.tell(expr('Compagnie(Groupe)&Interet(Découverte)==>Destination(Rome)'))

kb.tell(expr('Compagnie(Groupe)&Interet(Tourisme)==>Destination(Tokyo)'))
kb.tell(expr('Compagnie(Seul)&Interet(Découverte)==>Destination(Tokyo)'))
kb.tell(expr('Compagnie(Seul)&Interet(Gastronomie)==>Destination(Tokyo)'))




#Règles définissant les destinations selon le continent et le budget
#-------------------------------------------------------------#

kb.tell(expr('Continent(Europe)&Budget(Eleve)==>Destination(Paris)'))
kb.tell(expr('Continent(Europe)&Budget(Eleve)==>Destination(Rome)'))
kb.tell(expr('Continent(Europe)&Budget(Moyen)==>Destination(Istanbul)'))

kb.tell(expr('Continent(Afrique)&Budget(Moyen)==>Destination(Marrakech)'))
kb.tell(expr('Continent(Afrique)&Budget(Moyen)==>Destination(Caire)'))
kb.tell(expr('Continent(Afrique)&Budget(Moyen)==>Destination(Alger)'))

kb.tell(expr('Continent(Asie)&Budget(Elevé)==>Destination(Tokyo)'))
kb.tell(expr('Continent(Asie)&Budget(Elevé)==>Destination(Singapour)'))
kb.tell(expr('Continent(Asie)&Budget(Moyen)==>Destination(Istanbul)'))
kb.tell(expr('Continent(Asie)&Budget(Moyen)==>Destination(Bali)'))

kb.tell(expr('Continent(Amérique)&Budget(Moyen)==>Destination(Mexico)'))
kb.tell(expr('Continent(Amérique)&Budget(Elevé)==>Destination(NewYork)'))


#-------------------------------------------------------------#



result=fol_fc_ask(kb,expr('Destination(x)'))

print(list(result))
from .final_facts import *
from aima3.logic import *


def generateLogicExDist(data):
    expression_parts = []
    for key, value in data.items():
        if key in mapper:
            expression_parts.append(str(mapper[key](value)))
    expression = " & ".join(expression_parts) + " ==> Destination(x)"
    return expression


def generateLogicExContinent(data):
    expression_parts = []
    for key, value in data.items():
        if key in mapper:
            expression_parts.append(str(mapper[key](value)))
    expression = " & ".join(expression_parts) + " ==> Continent(y)"
    return expression


mapper = {
    'interet': lambda val: expr(f'Interet({val})'),
    'climat': lambda val: expr(f'Climat({val})'),
    'compagnie': lambda val: expr(f'Compagnie({val})'),
    'saison': lambda val: expr(f'Saison({val})'),
    'budget': lambda val: expr(f'Budget({val})'),
    'continent': lambda val: expr(f'Continent({val})'),
}


def final_Distinations(input_data, list_data):
    agenda = []
    destinations = []
    for key, value in input_data.items():
        if key in mapper:
            agenda.append(expr(str(mapper[key](value))))
    seen = set()
    memory = {}
    while agenda:
        p = agenda.pop(0)
        if p in seen:
            continue
        seen.add(p)
        if fol_fc_ask(dest_kb, p):
            memory[p] = True
        else:
            memory[p] = False
        data_one = {
            'compagnie': list_data[2],
            'interet': list_data[1]
        }
        data_continent = {
            'climat': list_data[3],
            'saison': 'Toutes'
        }
        if memory.get(expr(f'Compagnie({list_data[2]})'), False) and memory.get(expr(f'Interet({list_data[1]})'),
                                                                                False):
            dist1 = list(fol_fc_ask(dest_kb, expr(generateLogicExDist(data_one))))
            if dist1:
                for elem in dist1:
                    for value in elem.values():
                        destinations.append(value)
                        agenda.append(str('dist: ' + value))
        if memory.get(expr(f'Climat({list_data[3]})'), False) and memory.get(expr(f'Saison({list_data[4]})'), False):
            contient = list(fol_fc_ask(dest_kb, expr(generateLogicExContinent(data_continent))))
            if contient:
                for elem in contient:
                    for value in elem.values():
                        value_continent = value
                        expr_contient = str(expr(f'Continent({value})'))
                        agenda.append(expr(expr_contient))
                        data_two = {
                            'continent': value_continent,
                            'budget': list_data[0]
                        }
                        if memory.get(expr(expr_contient), False) and memory.get(expr(f'Budget({list_data[0]})'),
                                                                                 False):
                            dist2_exp = str(generateLogicExDist(data_two))
                            dist2 = list(fol_fc_ask(dest_kb, expr(dist2_exp)))
                            if dist2:
                                for elem in dist2:
                                    for value in elem.values():
                                        destinations.append(value)
                                        agenda.append(str('dist: ' + value))

    return list(set(destinations))

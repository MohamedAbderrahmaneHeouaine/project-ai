from .facts import *

def generateLogicEx(data):
    expression_parts = []
    for key, value in data.items():
        if key in mapper:
            expression_parts.append(str(mapper[key](value)))
    expression = " & ".join(expression_parts) + " ==> Destination(x)"
    return expression




mapper = {
    'interet': lambda val: expr(f'Interet({val})'),
    'continent': lambda val: expr(f'Continent({val})'),
    'climat': lambda val: expr(f'Climat({val})'),
    'compagnie': lambda val: expr(f'Compagnie({val})'),
    'preference': lambda val: expr(f'Preference({val})'),
    'saison': lambda val: expr(f'Saison({val})'),
    'budget': lambda val: expr(f'Budget({val})'),
}

# Create an instance of KnowledBase
# kb_instance = KnowledBase(input_data).response()

# Print the result
def returnDistination(input_data):
    logicEx = generateLogicEx(input_data)
    result = str(logicEx)
    return list(fol_fc_ask(dest_kb, expr(result)))
# result2 = fol_fc_ask(dest_kb, expr('Budget(Moyen) & Preference(Plage) & Interet(Tourisme) & Compagnie(Famille) & Climat(Tropical) & Continent(Amérique) & Saison(Toutes) ==>Destination(x)'))
# result = str(generateLogicEx(input_data))
# print(result)
# print("Possible destinations:", list(fol_fc_ask(dest_kb, expr(result))))
# print(list(result2))
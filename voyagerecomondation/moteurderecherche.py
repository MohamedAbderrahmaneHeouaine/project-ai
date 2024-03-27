from aima3.logic import fol_fc_ask, expr
from aima3.utils import *
from facts import *


class FormatingData:
    def __init__(self, data):
        self.data = data
        self.mapper = {
            'interet': lambda val: expr(f'Interet({val})'),
            'continent': lambda val: expr(f'Continent({val})'),
            'climat': lambda val: expr(f'Climat({val})'),
            'compagnie': lambda val: expr(f'Compagnie({val})'),
            'preference': lambda val: expr(f'Preference({val})'),
            'saison': lambda val: expr(f'Saison({val})'),
            'budget': lambda val: expr(f'Budget({val})'),
        }

    def generateLogicEx(self, **kwargs):
        expression_parts = []
        for key, value in kwargs.items():
            if key in self.mapper:
                expression_parts.append(str(self.mapper[key](value)))
        expression = " & ".join(expression_parts) + " ==> Destination(x)"
        return expression


class KnowledBase:
    def __init__(self, data):
        self.KB = dest_kb
        self.expressions = FormatingData(data).generateLogicEx(**data)

    def synchronize_KB(self):
        self.KB.tell(self.expressions)

    def reset_KB(self, extraData=[]):
        self.KB.retract(self.expressions)
        for sentence in extraData:
            self.KB.retract(expr(f'Destination({sentence})'))

    def response(self):
        self.synchronize_KB()
        res = fol_fc_ask(self.KB, expr('Destination(x)'))
        return res
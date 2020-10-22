import numpy as np
import pandas as pd
monthly_income = float(input('Enter you monthly income after tax deduction: \n'))
budget_list = {}
def list_of_items_entry():
    item_dict = {}
    item = ''
    cost = 0.0
    end_entry = ''
    while end_entry[0:1].lower() != 'n':
        item = input('Enter Item:\n')
        cost = input('Enter Cost for {}\n'.format(item))
        item_dict.update({item: float(cost)})
        end_entry = input('Would you like to add another item, y/n\n')
    return item_dict

budget_list = list_of_items_entry()
ps = pd.Series(budget_list)
ps['TOTAL'] = ps.sum()
print('Monthly income: {}\nAnd Your budget:\n{}'.format(monthly_income, ps))

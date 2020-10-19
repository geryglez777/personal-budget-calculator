item_dict = {}
def data_entry():
    item = ''
    cost = 0.0
    end_entry = ''    
    while end_entry[0:1].lower() <> 'y':
        item = input('Enter Item: '\n)
        cost = input('Enter Cost for: {}\n'.format(item))
        end_entry = input('Would you like to add another item, y/n\n')
    return item, cost

data_entry()
print('This is {}, {}'.format(item, cost))

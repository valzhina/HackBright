"""Print out all the melons in our inventory."""
# all_melons = {
#     'Honeydew':{'prices':0.99,'seedlessness': True, 'flesh_color': None, 'weight': None, 'rind_color': None,},


from melons import all_melons


def print_melon(dic_name, dic_value):
    """Print each melon with corresponding attribute information."""

    # have_or_have_not = 'have'
    # if seedless:
    #     have_or_have_not = 'do not have'

    # print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')

    # print(name.upper())
    # print (f'   seedless: {seedless}')
    # print (f'   price: {price}')
    # print (f'   flesh_color: {flesh_color}')
    # print (f'   weight: {weight}')
    # print (f'   rind_color: {rind_color}\n')
    
    print(dic_name.upper())
    for parameter, value in dic_value.items():
        print(f'    {parameter}: {value}')

for melon in all_melons:
    print_melon(melon, all_melons[melon])

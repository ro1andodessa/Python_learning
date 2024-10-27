orders = {'Руслан': {'Пирог': 1, 'Линейка': 2}, 'Тимур': {'Карандаш': 5}}
for i in sorted(orders.keys()):
    print(i, ':', sep='')
    print(*(f'{k} {v}' for k, v in sorted(orders[i].items())), sep='\n')

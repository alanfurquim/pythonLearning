from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt-BR')
months = map(lambda x:month_name[x], range(1,13))
days = map(lambda x:mdays[x], range(1,13))

dict_months = [{'Mês': month, 'Days': day} for month, day in zip(months, days)]

meses_filter = filter(lambda dict_months: dict_months['Days'] == 31, dict_months)

meses_map = map(lambda p: f"O mês de {p['Mês']} tem 31 dias.", meses_filter)
print(list(meses_map))

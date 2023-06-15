from functools import reduce
from operator import add

#tupla só aceita funções imutaveis
valores = [30, 10, 25, 70, 100, 94]

print(sorted(valores))
print(valores)

# valores.sort()
# print(valores)
print(min(valores))
print(max(valores))
print(sum(valores))
print(reduce(add, valores))
print(list(reversed(valores)))

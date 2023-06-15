compras = (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)

def calc_preco_total(c): return c['quantidade'] * c['preco']

totais = tuple(map(calc_preco_total,compras))

print('Preços totais:', totais)
print('Total geral:', sum(totais))

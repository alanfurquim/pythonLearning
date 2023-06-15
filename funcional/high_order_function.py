from first_class_function import dobro, quadrado

def processar(titulo, lista, funcao):
    print(f'Processando {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))

if __name__ == '__main__':
    processar('Dobro de 1 a 10', range(1,11), dobro)
    processar('Quadrado de 1 a 10', range(1,11), quadrado)
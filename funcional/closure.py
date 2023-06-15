def multiplicador(x):
    def calcular(y):
        return x * y
    return calcular

if __name__ == '__main__':
    dobro = multiplicador(2)
    triplo = multiplicador(3)
    print(f'O triplo de 3 é {triplo(3)}')
    print(f'O dobro de 5 é {dobro(5)}')
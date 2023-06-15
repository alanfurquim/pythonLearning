#decorator function
def log(function):
    def decorator(*args, **kwargs):
        print(f'Nome da função: {function.__name__}')
        print(f'Args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'resultado: {resultado}')
        print('\n')
        return resultado
    return decorator

@log
def soma(a, b):
    return a + b

@log
def subtrai(a, b):
    return a - b

if __name__ == '__main__':
    print(soma(1, 2))
    print(subtrai(2, 1))

def fatorial(n):
    return n if n == 1 else n * fatorial(n - 1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')

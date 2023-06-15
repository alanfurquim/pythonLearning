def sequence():
    """
    The function creates an infinite sequence of numbers starting from 1 using a generator.
    """
    num = 0
    while True:
        num += 1
        yield num

if __name__ == '__main__':
    sequence = sequence()
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))
    print(next(sequence))

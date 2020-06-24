class EvenNumbersUsingListComprehension:
    def __init__(self):
        return


if __name__ == '__main__':
    even_numbers = [x for x in range(21) if x%2 == 0]
    print(f'{even_numbers}')

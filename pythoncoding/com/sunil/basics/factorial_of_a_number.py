class FactorialOfANumber:
    def __init__(self):
        return


if __name__ == '__main__':
    a = 5
    result = 1

    for i in range(1, a+1):
        result = result * i

    print(f'Factorial of {a} is {result}')

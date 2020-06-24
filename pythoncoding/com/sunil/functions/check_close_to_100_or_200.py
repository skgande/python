class CheckCloseTo100Or200:
    """
    Given an integer n, return True if n is within +-10 of either 100 or 200

        almost_there(90) --> True
        almost_there(104) --> True
        almost_there(150) --> False
        almost_there(209) --> True
    """
    def __init__(self):
        return


def _almost_there(num):
    if abs(num - 100) <= 10 or abs(num - 200) <= 10:
        return True
    return False


if __name__ == '__main__':
    number = int(input(f'Enter a number to check close to 100 or 200'))
    result = _almost_there(number)
    print(f'{result}')

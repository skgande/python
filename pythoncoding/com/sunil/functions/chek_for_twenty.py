class CheckForTwenty:
    """
    Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20.
    If not, return False\n",
        makes_twenty(20,10) --> True,
        makes_twenty(12,8) --> True,
        makes_twenty(2,3) --> False
    """

    def __init__(self):
        return


def _make_twenty(first, second):
    if first + second == 20 or first == 20 or second == 20:
        return True
    return False


if __name__ == '__main__':
    first_number = int(input(f'Enter first number'))
    second_number = int(input(f'Enter second number'))
    result = _make_twenty(first_number, second_number)
    print(f'{result}')

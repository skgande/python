class CheckForConsecutiveThreesInArray:
    """
    Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

        has_33([1, 3, 3]) → True
        has_33([1, 3, 1, 3]) → False
        has_33([3, 1, 3]) → False"
    """

    def __init__(self):
        return


def _has_33(numbers):
    for i in range(len(numbers)-1):
        if numbers[i] == 3 and numbers[i+1] == 3:
            return True
    return False


if __name__ == '__main__':
    given_numbers = [3, 1, 3]
    result  = _has_33(given_numbers);
    print(f'{result}')

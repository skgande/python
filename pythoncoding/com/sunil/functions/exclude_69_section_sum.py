class Exclude69SectionSum:
    """
    Return the sum of the numbers in the array, except ignore sections of numbers starting with
    a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

        summer_69([1, 3, 5]) --> 9
        summer_69([4, 5, 6, 7, 8, 9]) --> 9,
        summer_69([2, 1, 6, 9, 11]) --> 14
    """

    def __init__(self):
        return


def _get_exclude_69_sum(numbers):
    sum  = 0
    is_six_and_nine_section = False

    for number in numbers:
        if number == 6:
            is_six_and_nine_section = True
        elif number == 9:
            is_six_and_nine_section = False
        else:
            if not is_six_and_nine_section:
                sum = sum + number
    return sum


if __name__ == '__main__':
    given_numbers = [2, 1, 6, 9, 11]
    result = _get_exclude_69_sum(given_numbers)
    print(f'{result}')

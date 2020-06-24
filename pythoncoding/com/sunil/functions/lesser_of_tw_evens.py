class LesserOfTwoEvens:
    """
    LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even,
    but returns the greater if one or both numbers are odd?

        lesser_of_two_evens(2,4) --> 2
        lesser_of_two_evens(2,5) --> 5
    """
    def __init__(self):
        return


def _print_based_on_inputs(num_one, num_two):
    if num_one % 2 == 0 and num_two % 2 == 0:
        lesser_number = num_one
        if num_one > num_two:
            lesser_number = num_two
        print(f'Lesser of two numbers is {lesser_number}')
    else:
        highest_number = num_one
        if num_one < num_two:
            highest_number = num_two
        print(f'Highest of two numbers is {highest_number}')


if __name__ == '__main__':
    first_number = int(input('Enter first number'))
    second_number = int(input('Enter second number'))
    _print_based_on_inputs(first_number, second_number)

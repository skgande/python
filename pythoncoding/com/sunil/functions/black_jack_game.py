class BlackJackGame:
    """
    Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
    If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally,
    if the sum (even after adjustment) exceeds 21, return 'BUST

        blackjack(5,6,7) --> 18
        blackjack(9,9,9) --> 'BUST’
        blackjack(9,9,11) --> 19
    """

    def __init__(self):
        return


def _black_jack(numbers):
    is_11_present = False
    sum = 0
    for number in numbers:
        if number == 11:
            is_11_present = True
        sum = sum + number
    if sum <= 21:
        return sum
    elif is_11_present:
        return sum - 10
    else:
        return sum


if __name__ == '__main__':
    given_numbers = [9, 9, 11]
    sum = _black_jack(given_numbers)
    if sum > 21:
        print(f'BUST')
    else:
        print(f'{sum}')

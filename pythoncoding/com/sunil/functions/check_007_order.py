class Check007Order:
    """
    Write a function that takes in a list of integers and returns True if it contains 007 in order
        spy_game([1,2,4,0,0,7,5]) --> True
        spy_game([1,0,2,4,0,5,7]) --> True
        spy_game([1,7,2,0,4,5,0]) --> False
    """

    def __init__(self):
        return


def _check_007_order(nums):
    is_first_zero = False
    is_second_zero = False
    is_seven = False

    for num in nums:
        if num == 0:
            if not is_first_zero:
                is_first_zero = True
            elif not is_second_zero:
                is_second_zero = True
        elif num == 7:
            if is_first_zero and is_second_zero:
                return True
    return False


if __name__ == '__main__':
    numbers = [1, 7, 2, 0, 4, 5, 0]
    result = _check_007_order(numbers)
    print(f'{result}')

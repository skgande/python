class CapitalizeFirstAndFourthCharacterOfString:
    """
    Write a function that capitalizes the first and fourth letters of a name.
    old_macdonald('macdonald') --> MacDonald
    """

    def __init__(self):
        return


def _capitalize_first_and_fourth_character(input_string):
    input_string = input_string.replace(input_string[0], input_string[0].capitalize(), 1)
    input_string = input_string.replace(input_string[3], input_string[3].capitalize(), 1)
    return input_string


if __name__ == '__main__':
    given_string = input('Enter input string')
    result = _capitalize_first_and_fourth_character(given_string)
    print(f'{result}')

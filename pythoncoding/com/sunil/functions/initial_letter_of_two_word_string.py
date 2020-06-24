class InitialLetterOfTwoWordString:
    """
    Write a function takes a two-word string and returns True if both words begin with same letter
        animal_crackers('Levelheaded Llama') --> True
        animal_crackers('Crazy Kangaroo') --> False

    """
    def __init__(self):
        return


def _check_first_letter(first, second):
    return first[0] == second[0]


if __name__ == '__main__':
    given_string = input('Enter two word string')
    words = given_string.split(' ')
    first_word = words[0]
    second_word = words[1]
    result = _check_first_letter(first_word, second_word)
    print(f'{result}')

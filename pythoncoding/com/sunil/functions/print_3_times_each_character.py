class Print3TimesEachCharacter:
    """
    Given a string, return a string where for every character in the original there are three characters.
        paper_doll('Hello') --> 'HHHeeellllllooo’
        paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii’
    """

    def __init__(self):
        return

    def print_3_times(self, given_string):
        result = ''
        for letter in given_string:
            temp = letter * 3
            result = result + temp
        return result

    def is_palindrome(self, input_string):
        return input_string == input_string[::-1]


if __name__ == '__main__':
    input_string = input('Enter input string')
    my_obj = Print3TimesEachCharacter()
    result = my_obj.print_3_times(input_string)
    print(f'{result}')
    print(f'{my_obj.is_palindrome(input_string)}')

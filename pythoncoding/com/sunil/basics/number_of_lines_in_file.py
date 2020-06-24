class NumberOfLinesInFile:
    def __init__(self):
        return


if __name__ == '__main__':
    given_string = "abc\ndef\nghi\njkl\n"
    lines = given_string.count('\n')
    print(f'number of lines are {lines}')

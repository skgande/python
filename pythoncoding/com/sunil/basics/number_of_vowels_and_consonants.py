class NumberOfVowelsAndConsonants:
    def __init__(self):
        return


if __name__ == '__main__':
    given_string = 'environment'
    vowels_count = 0
    consonants_count = 0

    for i in range(len(given_string)):
        if given_string[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels_count = vowels_count + 1
        else:
            consonants_count = consonants_count + 1

    print(f'In a {given_string} number of vowels are {vowels_count} and number of consonants are {consonants_count}')

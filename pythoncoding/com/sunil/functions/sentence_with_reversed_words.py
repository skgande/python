class SentenceWithReversedWords:
    """
    Given a sentence, return a sentence with the words reversed.

        master_yoda(I am home) --> home am I
        master_yoda(We are ready) --> ready are We
    """

    def __init__(self):
        return


def _get_reverse_words(sentence):
    words = sentence.split(' ')
    reverse_sentence = ''
    print(words)
    for index in range(len(words)-1, -1, -1):
        reverse_sentence = reverse_sentence + words[index] + ' '
    return reverse_sentence


if __name__ == '__main__':
    given_string = input('Enter a sentence')
    sentence_with_revered_words  = _get_reverse_words(given_string)
    print(f'{sentence_with_revered_words}')

class MaxOccurrenceOfWordInSentence:
    def __init__(self):
        return


if __name__ == '__main__':
    given_string = "this is python learning to learn python and python"

    words = given_string.split(' ')
    words_dict = {}

    for i in range(len(words)):
        word = words[i]
        if word in words_dict:
            value = words_dict[word]
            words_dict[word] = value+1
        else:
            words_dict[word] = 1

    distinct_words = list(words_dict.keys())
    max_word = ''
    max_occurrence = 0

    for i in range(len(distinct_words)):
        if words_dict[distinct_words[i]] > max_occurrence:
            max_occurrence = words_dict[distinct_words[i]]
            max_word = distinct_words[i]

    print(f'{max_word} occurred {max_occurrence} times in a given sentence')

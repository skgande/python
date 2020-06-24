class IsPalindrome:
    def __init__(self):
        return


if __name__ == '__main__':
    a = "abcba"

    if a == a[::-1]:
        print(f'Given string {a} is palindrome')
    else:
        print(f'Given string {a} is not palindrome')

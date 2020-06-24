class IsPowerOfTwo:
    def __init__(self):
        return


if __name__ == '__main__':
    a = 16

    if a & (a-1) == 0:
        print(f'Given number {a} is power of 2')
    else:
        print(f'Given number {a} is not power of 2')

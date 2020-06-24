class IsFibonacci:
    def __init__(self):
        return


if __name__ == '__main__':
    a = [0, 1, 1, 2, 3, 5, 8]
    is_fibonacci = True

    for i in range(2, len(a)):
        if a[i] != a[i-2] + a[i-1]:
            is_fibonacci = False
            break

    if is_fibonacci:
        print(f'Given series is fibonacci series')
    else:
        print(f'Given series is not fibonacci series')

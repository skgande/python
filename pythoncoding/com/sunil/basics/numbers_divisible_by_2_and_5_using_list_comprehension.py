class NumbersDivisibleBy2And5UsingListComprehension:
    def __init__(self):
        return


if __name__ == '__main__':
    numbers_divisible_by_2_and_5 = [c for c in range(21) if c % 2 == 0 if c % 5 == 0]
    print(f'{numbers_divisible_by_2_and_5}')

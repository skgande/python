class CountPrimeNumbers:
    """
    Write a function that returns the *number* of prime numbers that exist up to and including a given number
        count_primes(100) --> 25

    """

    def __init__(self):
        return


def _count_primes(number):
    count  = 0
    for num in range(number+1):
        if num <= 1:
            pass
        else:
            is_prime = True
            for a in range(2,num):
                if num % a == 0:
                    is_prime = False
            if is_prime:
                count += 1
    return count


if __name__ == '__main__':
    result = _count_primes(100)
    print(f'{result}')

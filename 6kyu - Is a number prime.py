# Is Prime
# Define a function isPrime/is_prime() that takes one integer argument and returns true/True or false/False depending on
# if the integer is a prime.
#
# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than
# 1 and itself.
#
# Example
# isPrime(5)
# => true
# Assumptions
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).


def is_prime(num):
    primes = {2, 3}
    if num <= max(primes):
        if num in primes:
            return True
        else:
            return False
    maybe_primes = set()
    for k in range(1, int((num ** (1 / 2)) // 6) + 1):
        maybe_primes.add(6 * k - 1)
        maybe_primes.add(6 * k + 1)
    for maybe_prime in sorted(maybe_primes):
        for prime in sorted(primes):
            if maybe_prime % prime == 0:
                break
        else:
            primes.add(maybe_prime)
    for prime in sorted(primes):
        if num % prime == 0:
            return False
    else:
        return True


tests = ((0, False),
         (1, False),
         (2, True),
         (3, True),
         (4, False),
         (213657, False),
         (165887, True),
         (387419, False),
         (514229, True),
         (325841, False))


for test in tests:
    test_outcome = is_prime(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))

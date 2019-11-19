# In this kata you will create a function to check a non-negative input to see if it is a prime number.
#
# The function will take in a number and will return True if it is a prime number and False if it is not.
#
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#
# Examples
# isPrime(0) is false
# isPrime(1) is false
# isPrime(2) is true
# isPrime(11) is true
# isPrime(12) is false


def is_prime(n):
    primes = {2, 3}
    maybe_primes = {5, 7}
    if n < min(primes):
        return False
    elif n in primes:
        return True
    else:
        for k in range(1, n ** (1 // 2) + 1):
            maybe_primes.add(6 * k - 1)
            maybe_primes.add(6 * k + 1)
        for maybe_prime in sorted(maybe_primes):
            for prime in sorted(primes):
                if maybe_prime % prime == 0:
                    break
            else:
                primes.add(maybe_prime)
        for prime in sorted(primes):
            if n % prime == 0:
                return False
        else:
            return True


tests = ((5, False),
         (1237, True),
         (2000, False),
         (4283, True),
         (5000, False),
         (6761, True))

for test in tests:
    test_outcome = is_prime(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))

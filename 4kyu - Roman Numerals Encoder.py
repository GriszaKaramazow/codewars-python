# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral
# representation of that integer.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
# any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is
# written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Example:
#
# solution(1000) # should return 'M'
# Help:
#
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# Remember that there can't be more than 3 identical symbols in a row.
#
# More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals

roman = {1000: "M",
         500: "D",
         100: "C",
         50: "L",
         10: "X",
         5: "V",
         1: "I"}


def solution(n):
    n = [n % 10000 - n % 1000, n % 1000 - n % 100, n % 100 - n % 10, n % 10]
    # result = ""
    # for i in sorted(roman.keys(), reverse=True):
    #     c = 0
    #     while n >= i:
    #         n -= i
    #         c += 1
    #     else:
    #         if i == 1000 or c < 4:
    #             result += roman[i] * c
    #         else:
    #             result += roman[i] + roman[i*5]
    return n


tests = ((1, "I"),
         (4, "IV"),
         (6, "VI"),
         (30, "XXX"),
         (89, "LXXXIX"),
         (1000, "M"),
         (1666, "MDCLXVI"),
         (2008, "MMVIII"),
         (5000, "MMMMM"))

for test in tests:
    test_outcome = solution(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))
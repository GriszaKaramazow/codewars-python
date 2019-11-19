# Write a program that will calculate the number of trailing zeros in a factorial of a given number.
#
# N! = 1 * 2 * 3 * ... * N
#
# Be careful 1000! has 2568 digits...
#
# For more info, see: http://mathworld.wolfram.com/Factorial.html
#
# Examples
# zeros(6) = 1
# # 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
#
# zeros(12) = 2
# # 12! = 479001600 --> 2 trailing zeros
# Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.



def zeros(n):
    k = 1
    trailing_zeros = 0
    while 5 ** k < n:
        trailing_zeros += n //(5 ** k)
        k += 1
    return trailing_zeros


tests = ((0, 0),
         (6, 1),
         (12, 2),
         (20, 4),
         (25, 6),
         (30, 7),
         (40, 9),
         (50, 12),
         (100, 24),
         (1000, 249),
         (100000, 24999),
         (1000000000, 249999998))


for test in tests:
    test_outcome = zeros(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))
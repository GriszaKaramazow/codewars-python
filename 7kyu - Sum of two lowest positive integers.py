# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No
# floats or empty arrays will be passed.
#
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
#
# [10, 343445353, 3453445, 3453545353453] should return 3453455.
#
# Hint: Do not modify the original array.


def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]


tests = (([5, 8, 12, 18, 22], 13),
         ([7, 15, 12, 18, 22], 19),
         ([25, 42, 12, 18, 22], 30))

for test in tests:
    if sum_two_smallest_numbers(test[0]) == test[1]:
        print("Test passed!")
    else:
        print("Wrong output!")

# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in
# descending order. Essentially, rearrange the digits to create the highest possible number.
#
# Examples:
# Input: 21445 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 1254859723 Output: 9875543221


def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


tests = ((21445, 54421),
         (145263, 654321),
         (1254859723, 9875543221),
         (0, 0),
         (15, 51),
         (123456789, 987654321))


for test in tests:
    test_outcome = Descending_Order(test[0])
    if test_outcome == test[1]:
        print("\t{} is {}, test passed!".format(test_outcome, test[1]))
    else:
        print("!!! {} is not {}, wrong output!".format(test_outcome, test[1]))


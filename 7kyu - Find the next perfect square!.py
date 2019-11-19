# You might know some pretty large perfect squares. But what about the NEXT one?
#
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
#
# If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.
#
# Examples:
#
# findNextSquare(121) --> returns 144
# findNextSquare(625) --> returns 676
# findNextSquare(114) --> returns -1 since 114 is not a perfect


def find_next_square(sq):
    if (sq ** 0.5) == int(sq ** 0.5):
        return (int(sq ** 0.5) + 1) ** 2
    else:
        return -1


tests = ((121, 144),
         (625, 676),
         (319225, 320356),
         (15241383936, 15241630849),
         (155, -1),
         (342786627, -1))

for test in tests:
    test_outcome = find_next_square(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))
# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The
# range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at
# least 3 numbers. For example ("12, 13, 15-17")
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
# in the range format.
#
# Example:
#
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# # returns "-6,-3-1,3-5,7-11,14,15,17-20"


def solution(args):
    print(args)
    # simplified = list()
    # simplified.append(args[0])
    # simplified.append(args[1])
    # for i in range(2, len(args)):
    #     if args[i] - args[i - 2] == 2:
    #         count = 1
    #         while args[i + n] - args[i - 2] == 2 + n:
    #
    #     else:
    #         simplified.append(args[i])
    # print(simplified)
    for num in args:
        count_list = list()
        count = 0
        while args[args.index(num) + count] - args[args.index(num) - 2] == (2 + count):
            count += 1
            count_list.append(count)
            if args.index(num) + count == len(args):
                break
    print(count_list)

    return ",".join([str(x) for x in args])


tests = (([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20], '-6,-3-1,3-5,7-11,14,15,17-20'),
         ([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], '-3--1,2,10,15,16,18-20'))


for test in tests:
    test_outcome = solution(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))
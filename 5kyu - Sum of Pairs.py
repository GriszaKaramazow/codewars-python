# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of
# appearance that add up to form the sum.
#
# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]
#
# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * entire pair is earlier, and therefore is the correct answer
# == [4, 2]
#
# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)
#
# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * entire pair is earlier, and therefore is the correct answer
# == [3, 7]
# Negative numbers and duplicate numbers can and will appear.
#
# NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.


def sum_pairs(num_list, s):
    # outcome = None
    # while num_list != []:
    #     for a in range(len(num_list)):
    #         temp_num = num_list.pop(a)
    #         if (s - temp_num) in num_list:
    #             outcome = [temp_num, (s - temp_num)]
    #             num_list = num_list[a:num_list.index(s - temp_num)]
    #             break
    #         num_list.insert(a, temp_num)
    #     else:
    #         return outcome
    # else:
    #     return outcome

    missing_numbers = set()
    for num in num_list:
        if (s - num) in missing_numbers:
            return [s - num, num]
        missing_numbers.add(num)
    else:
        return None


tests = (([1, 4, 8, 7, 3, 15], 8, [1, 7]),
         ([1, -2, 3, 0, -6, 1], -6, [0, -6]),
         ([20, -13, 40], -7, None),
         ([1, 2, 3, 4, 1, 0], 2, [1, 1]),
         ([10, 5, 2, 3, 7, 5], 10, [3, 7]),
         ([4, -2, 3, 3, 4], 8, [4, 4]),
         ([0, 2, 0], 0, [0, 0]),
         ([5, 9, 13, -3], 10, [13, -3]))

for test in tests:
    test_outcome = sum_pairs(test[0], test[1])
    if test_outcome == test[2]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[2]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[2]))
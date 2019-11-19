# In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you
# to shuffle all letters from the input in all possible orders.
#
# Examples:
#
# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']


def permutations(string, letter):
    result = set()
    while True:
        for i in range(len(string)):
            temp = list(string)
            temp.insert(i, letter)
            result.add("".join(temp))
        else:
            return sorted(result)

print(permutations("grzechu", "j"))


# tests = (('a', ['a']),
#          ('ab', ['ab', 'ba']),
#          ('aabb', ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']))
#
# for test in tests:
#     test_outcome = permutations(test[0])
#     if test_outcome == test[1]:
#         print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
#     else:
#         print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))
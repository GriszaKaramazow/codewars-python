# Your goal in this kata is to implement an difference function, which subtracts one list from another.
#
# It should remove all values from list a, which are present in list b.
#
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
#
# array_diff([1,2,2,2,3],[2]) == [1,3]

# Test.describe("Basic Tests")
# Test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
# Test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
# Test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
# Test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
# Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")

def array_diff(a, b):
    c = list()
    for i in range(len(a)):
        if a[i] not in set(b):
            c.append(a[i])
    return c

list_a = [1,2,2,2,3]
list_b = [2]
print(array_diff(list_a, list_b))

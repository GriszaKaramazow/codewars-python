# Find the longest substring in alphabetical order.
#
# Eg: the longest alphabetical substring in asdfaaaabbbbcttavvfffffdf is aaaabbbbctt.
#
# There are tests with strings up to 10000 characters long so your code will need to be efficient.
#
# The input will only consist of lowercase characters and will be at least one letter long.
#
# Good luck :)


def longest(s):
    temp_str = ""
    longest_str = s[0]
    for char in s:
        if temp_str == "":
            temp_str = char
        elif char >= temp_str[-1]:
            temp_str += char
        else:
            if len(temp_str) > len(longest_str):
                longest_str = temp_str
            temp_str = char
    else:
        if len(temp_str) > len(longest_str):
            longest_str = temp_str
    return longest_str


tests = (('asd', 'as'),
         ('nab', 'ab'),
         ('abcdeapbcdef', 'abcde'),
         ('asdfaaaabbbbcttavvfffffdf', 'aaaabbbbctt'),
         ('asdfbyfgiklag', 'fgikl'),
         ('z', 'z'),
         ('zyba', 'z'),
         ('zaaaaaaaaaaaaa', 'aaaaaaaaaaaaa'))

for test in tests:
    test_outcome = longest(test[0])
    if test_outcome == test[1]:
        print("\t{} is {}, test passed!".format(test_outcome, test[1]))
    else:
        print("!!! {} is not {}, wrong output!".format(test_outcome, test[1]))

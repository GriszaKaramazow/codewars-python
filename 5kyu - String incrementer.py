# Your job is to write a function which increments a string, to create a new string. If the string already ends with a
# number, the number should be incremented by 1. If the string does not end with a number the number 1 should be
# appended to the new string.
#
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be considered.


def increment_string(strng):
    strng = list(strng)
    number = list()
    for char in strng[::-1]:
        if char in "0123456789":
            number.append(char)
            strng.pop(-1)
        else:
            break
    if number == list():
        strng.append("1")
        return "".join(strng)
    for digit in range(len(number)):
        if number[digit] == "9":
            number[digit] = "0"
        elif number[digit] in "012345678":
            number[digit] = str(int(number[digit]) + 1)
            break
    else:
        if number[digit] == "9":
            number[digit] = "10"
        else:
            number.append("1")
    return "".join(strng) + "".join(number[::-1])


tests = (("foo", "foo1"),
         ('foobar001', 'foobar002'),
         ('foobar1', 'foobar2'),
         ('foobar00', 'foobar01'),
         ('foobar99', 'foobar100'),
         ('foobar099', 'foobar100'),
         ('foobar99999', 'foobar100000'),
         ('foobar099999', 'foobar100000'),
         ('8', '9'),
         ('9', '10'),
         ('', '1'))


for test in tests:
    test_outcome = increment_string(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))
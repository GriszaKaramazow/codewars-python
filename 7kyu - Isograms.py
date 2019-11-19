# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore
# letter case.
#
# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case


def is_isogram(string):
    string = list(string.lower())
    while string != []:
        letter = string.pop(0)
        if letter in string:
            return False
    else:
        return True


tests = (("Dermatoglyphics", True),
         ("isogram", True),
         ("aba", False),
         ("moOse", False),
         ("isIsogram", False),
         ("", True))


for test in tests:
    test_outcome = is_isogram(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))


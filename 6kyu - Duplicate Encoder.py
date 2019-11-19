# The goal of this exercise is to convert a string to a new string where each character in the new string is '(' if that
# character appears only once in the original string, or ')' if that character appears more than once in the original
# string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples:
#
# "din" => "((("
#
# "recede" => "()()()"
#
# "Success" => ")())())"
#
# "(( @" => "))(("


def duplicate_encode(word):
    encoded_str = ""
    for char in word.lower():
        if word.lower().count(char) > 1:
            encoded_str += ")"
        else:
            encoded_str += "("
    return encoded_str


tests = (("din", "((("),
         ("recede", "()()()"),
         ("Success", ")())())"),
         ("(( @", "))(("))


for test in tests:
    test_outcome = duplicate_encode(test[0])
    if test_outcome == test[1]:
        print("\t{} is {}, test passed!".format(test_outcome, test[1]))
    else:
        print("!!! {} is not {}, wrong output!".format(test_outcome, test[1]))

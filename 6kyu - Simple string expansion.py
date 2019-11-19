# Consider the following expansion:
#
# solve("3(ab)") = "ababab" -- "ab" repeats 3 times
# solve("2(a3(b))" = "abbbabbb" -- "a3(b)" == "abbb" repeats twice.
# Given a string, return the expansion of that string.
#
# Input will consist of only lowercase letters and numbers in valid parenthesis. There will be no letters or numbers
# after the last closing parenthesis.
#
# More examples in test cases.
#
# Good luck!


def solve(st):
    outcome_st = ""
    for char in st[::-1]:
        if char.isalpha():
            outcome_st += char
        elif char.isdigit():
            outcome_st *= int(char)
    return outcome_st[::-1]


tests = (("3(ab)", "ababab"),
         ("2(a3(b))", "abbbabbb"),
         ("3(b(2(c)))", "bccbccbcc"),
         ("k(a3(b(a2(c))))", "kabaccbaccbacc"))

for test in tests:
    test_outcome = solve(test[0])
    if test_outcome == test[1]:
        print("{} is {}, test passed!".format(test_outcome, test[1]))
    else:
        print("{} is not {}, wrong output!".format(test_outcome, test[1]))

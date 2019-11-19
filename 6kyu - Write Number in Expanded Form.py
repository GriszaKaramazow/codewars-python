# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.


def expanded_form(num):
    outcome = list()
    for i in range(len(str(num))):
        outcome.append(str((num % 10) * (10 ** i)))
        num = int((num - (num % 10)) / 10)
    return " + ".join(list(x for x in outcome[::-1] if x != "0"))


tests = ((12, "10 + 2"),
         (42, "40 + 2"),
         (70304, "70000 + 300 + 4"))


for test in tests:
    test_outcome = expanded_form(test[0])
    if test_outcome == test[1]:
        print("\t{} is {}, test passed!".format(test_outcome, test[1]))
    else:
        print("!!! {} is not {}, wrong output!".format(test_outcome, test[1]))

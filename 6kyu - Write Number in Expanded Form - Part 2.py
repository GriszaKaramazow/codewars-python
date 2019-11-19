# This is version 2 of my 'Write Number in Exanded Form' Kata.
#
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(1.24) # Should return '1 + 2/10 + 4/100'
# expanded_form(7.304) # Should return '7 + 3/10 + 4/1000'
# expanded_form(0.04) # Should return '4/100'


def expanded_form(num):
    temp_str = list()
    num = str(num).split(".")
    for i in range(len(num[0])):
        if (int(num[0]) % 10) != 0:
            temp_str.append(str((int(num[0]) % 10) * (10 ** i)))
        num[0] = (int(num[0]) // 10)
    num[0] = " + ".join(temp_str[::-1])
    temp_str = list()
    num[1] = str(num[1])[::-1]
    for i in range(len(num[1])):
        if (int(num[1]) % 10) != 0:
            temp_str.append("{}/{}".format(int(num[1]) % 10, 10 ** (i + 1)))
        num[1] = (int(num[1]) // 10)
    num[1] = " + ".join(temp_str)
    return " + ".join(list(x for x in num if x != ""))


tests = ((693.23459, "600 + 90 + 3 + 2/10 + 3/100 + 4/1000 + 5/10000 + 9/100000"),
         (7004.560032, "7000 + 4 + 5/10 + 6/100 + 3/100000 + 2/1000000"),
         (7.304, "7 + 3/10 + 4/1000"),
         (0.04, "4/100"),
         (1.24, "1 + 2/10 + 4/100"))


for test in tests:
    test_outcome = expanded_form(test[0])
    if test_outcome == test[1]:
        print("\t{} is {}, test passed!".format(test_outcome, test[1]))
    else:
        print("!!! {} is not {}, wrong output!".format(test_outcome, test[1]))

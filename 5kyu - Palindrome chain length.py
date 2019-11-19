# Number is a palindrome if it is equal to the number with digits in reversed order. For example, 5, 44, 171, 4884 are
# palindromes and 43, 194, 4773 are not palindromes.
#
# Write a method palindrome_chain_length which takes a positive number and returns the number of special steps needed to
# obtain a palindrome. The special step is: "reverse the digits, and add to the original number". If the resulting
# number is not a palindrome, repeat the procedure with the sum until the resulting number is a palindrome.
#
# If the input number is already a palindrome, the number of steps is 0.
#
# Input will always be a positive integer.
#
# For example, start with 87:
#
# 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884
#
# 4884 is a palindrome and we needed 4 steps to obtain it, so palindrome_chain_length(87) == 4


# def palindrome_check(m):
#     for i in range(len(str(m))//2):
#         if list(str(m))[i] != list(str(m))[-1 - i]:
#             return False
#     else:
#         return True
#
#
# def palindrome_chain_length(n):
#     i = 0
#     while True:
#         if palindrome_check(n):
#             break
#         n += int("".join(list(str(n)[::-1])))
#         i += 1
#     return i


def palindrome_chain_length(n):
    i = 0
    while str(n) != str(n)[::-1]:
        n += int("".join(list(str(n)[::-1])))
        i += 1
    return i


tests = ((87, 4),
         (165, 3),
         (726, 2),
         (10, 1),
         (187, 23),
         (5, 0))

for test in tests:
    test_outcome = palindrome_chain_length(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))
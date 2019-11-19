# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
# alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
# characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
# should be shifted, like in the original Rot13 "implementation".
#
# Please note that using "encode" in Python is considered cheating.


def rot13(message):
    # ciphered_message = list()
    # for char in message:
    #     if ord(char) in (list(range(65, 78)) + list(range(97, 110))):
    #         ciphered_message.append(chr(ord(char) + 13))
    #     elif ord(char) in (list(range(78, 91)) + list(range(110, 123))):
    #         ciphered_message.append(chr(ord(char) - 13))
    #     else:
    #         ciphered_message.append(char)
    # return "".join(ciphered_message)
    return "".join([chr(ord(x) + 13) if ord(x) in list(range(65, 78)) + list(range(97, 110)) else chr(ord(x) - 13) if
                    ord(x) in list(range(78, 91)) + list(range(110, 123)) else x for x in message])


tests = (("test", "grfg"),
         ("Test", "Grfg"),
         ('Avoid success at all costs!', 'Nibvq fhpprff ng nyy pbfgf!'),
         ('nopqrstuvwxyzabcdefghijklm', 'abcdefghijklmnopqrstuvwxyz'))


for test in tests:
    test_outcome = rot13(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))

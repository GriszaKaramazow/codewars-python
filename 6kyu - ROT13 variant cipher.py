# You have been recruited by an unknown organization for your cipher encrypting/decrypting skills.
# Being new to the organization they decide to test your skills.
# Your first test is to write an algorithm that encrypts the given string in the following steps.
#
# The first step of the encryption is a standard ROT13 cipher. This is a special case of the caesar cipher where the
# letter is encrypted with its key that is thirteen letters down the alphabet,
# i.e. A => N, B => O, C => P, etc..
#
# Part two of the encryption is to take the ROT13 output and replace each letter with its exact opposite. A => Z,
# B => Y, C => X.
# The return value of this should be the encrypted message.
#
# Do not worry about capitalization or punctuation. All encrypted messages should be lower case and punctuation free.
# As an example, the string "welcome to our organization" should return "qibkyai ty ysv yvgmzenmteyz".
#
# Good luck, and congratulations on the new position.


def encrypter(strng):
    # rot13 = [chr(ord(x) + 13) if ord(x) in list(range(97, 110)) else chr(ord(x) - 13) if ord(x) in list(range(110, 123))
    #          else x for x in strng]
    # return "".join([chr(219 - (ord(x))) if x.isalpha() else x for x in rot13])
    return "".join([chr(219 - (ord(x) + 13)) if ord(x) in set(range(97, 110)) else chr(219 - (ord(x) - 13)) if ord(x)
                    in set(range(110, 123)) else x for x in strng])


tests = (("amz", "man"),
         ("welcome to the organization", "qibkyai ty tfi yvgmzenmteyz"),
         ('hello', 'fibby'),
         ('my name is', 'ao zmai eu'),
         ('goodbye', 'gyyjloi'))


for test in tests:
    test_outcome = encrypter(test[0])
    if test_outcome == test[1]:
        print("\tfor case {}, {} is {}, test passed!".format(test[0], test_outcome, test[1]))
    else:
        print("!!! for case {}, {} is not {}, wrong output!".format(test[0], test_outcome, test[1]))

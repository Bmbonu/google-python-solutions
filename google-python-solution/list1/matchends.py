
# Written by Mbonu Basil
# On Thur 30-March-2017

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    countword = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            countword += 1
    return countword


# test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
#  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
#  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

list1 = ['aba', 'xyz', 'aa', 'x', 'bbb']   #3
list2 = ['', 'x', 'xy', 'xyx', 'xx']       #2
list3 = ['aaa', 'be', 'abc', 'hello']      #1

print(match_ends(list1))
print(match_ends(list2))
print(match_ends(list3))
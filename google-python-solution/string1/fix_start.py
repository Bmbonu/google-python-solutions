
# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

def fix_start(s):
    firstLetter = s[0]
    for xter in s[1:]:
        #change every other occurence
        others = s[1:].replace(firstLetter, '*')
        #print(firstLetter)
    return firstLetter + others


word = 'google'
word2 = 'babble'
print(fix_start(word))
print(fix_start(word2))
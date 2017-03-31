# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count



#def test(got, expected):
 #   if got == expected:
  #      prefix = ' OK '
   # else:
    #    prefix = '  X '
    #print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
#def main():
 #   print('match_ends')
  #  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    #test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    #test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  #  if__name__=='__main__':
   #     main()



list1 = ['word', 'speeds', 'illuminati', 'the_mathematict', 'test']
print(match_ends(list1))
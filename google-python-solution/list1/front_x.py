# Written by Mbonu Basil
# on Thur 30-3-2017

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

def front_x(words):
    listwith_x = []
    other_list = []
    combinedlist = []
    for word in words:
        if word.startswith('x'):#word[0] == 'x':   #start with x or X
            listwith_x.append(word) #put in list_x
            listwith_x.sort()
        else:
            other_list.append(word)
            other_list.sort()
    combinedlist = listwith_x + other_list
    return combinedlist

  #print 'front_x'
  #test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),       #    ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  #test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),       #    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  #test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),  #    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


list1 = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
list2 = ['ccc', 'bbb', 'aaa', 'xcc', 'xaa']
list3 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']


print(front_x(list1))
print(front_x(list2))
print(front_x(list3))

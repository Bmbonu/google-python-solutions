
# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.

def mix_up(a, b):
    if len(a) >= 2 and len(b) >= 2:
        #collect the first two letters from the second word, then put the rest of the first
        first = b[0:2] + a[2:]
        #collect the first two letters from the first word, then put the rest of the second
        second = a[0:2] + b[2:]
        return first +' '+ second



a1 = 'uchee'
a2 = 'Basil'

print(mix_up(a1, a2))
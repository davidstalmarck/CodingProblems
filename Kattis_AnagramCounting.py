# you can find the problem here https://open.kattis.com/problems/anagramcounting
# written by David Stålmarck 2020-01-10

# two solutions for it, one ugly but short that is written for the sake of "troll", and one longer but more readeble

from math import factorial
import sys

def find_comb(a):
    d = {}
    len_a = len(a)-1
    perm = factorial(len_a)
    for el in a:

        ord_a = ord(el)
        if d.get(ord_a):
            d[ord_a] += 1
        else:
            d[ord_a] = 1
    for el in d:
        if d[el] != 1:
            perm = perm//factorial(d[el])

    print(int(perm))

for line in sys.stdin:
    find_comb(line)

    '''
    from collections import Counter
from math import factorial
from functools import reduce

while True:
    try:
        a = input()
    except:
        break
    print(factorial(len(a)) // reduce(lambda x, y: x * y, [factorial(n) for n in Counter(a).values()]))
    '''
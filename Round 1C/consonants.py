# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2013 Round 1C - Problem A. Consonants
# https://code.google.com/codejam/contest/2437488/dashboard#s=p0
#
# Time:  O(L)
# Space: O(1)
#

def consonants():
    name, n = raw_input().strip().split()
    L, n = len(name), int(n)
    result, cnt, left = 0, 0, n-2 # (i-(n-1))+1 = i-left => left = n-2
    for i, c in enumerate(name):
        cnt = cnt+1 if c not in "aeiou" else 0
        if cnt >= n:
            result += (i-left)*(L-i)
            left = i
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, consonants())

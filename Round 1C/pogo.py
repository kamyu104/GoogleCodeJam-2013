# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2013 Round 1C - Problem B. Pogo
# https://code.google.com/codejam/contest/2437488/dashboard#s=p1
#
# Time:  O(sqrt(X + Y))
# Space: O(1)
#

def pogo():
    X, Y = map(int, raw_input().strip().split())
    N, total = 0, 0
    while not (total >= abs(X)+abs(Y) and total%2 == (abs(X)+abs(Y))%2):
        N += 1
        total += N
    result = []
    while N > 0:
        if abs(X) > abs(Y):
            if X > 0: 
                result.append('E')
                X -= N
            else:
                result.append('W')
                X += N
        else:
            if Y > 0:
                result.append('N')
                Y -= N
            else:
                result.append('S')
                Y += N
        N -= 1
    return "".join(reversed(result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, pogo())

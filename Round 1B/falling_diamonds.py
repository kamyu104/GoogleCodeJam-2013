# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2013 Round 1B - Problem B. Falling Diamonds
# https://code.google.com/codejam/contest/2434486/dashboard#s=p1
#
# Time:  O(N)
# Space: O(1)
#

def binomial(n, k):
    if n-k < k:
        return binomial(n, n-k)
    c = 1
    for k in xrange(1, k+1):
        c *= n-k+1
        c //= k
    return c

def falling_diamonds():
    N, X, Y = map(int, raw_input().strip().split())
    D = (abs(X)+Y)//2
    if X == 0:
        if N < ((4*D+1)+1)*(D+1)//2:
            return 0.0
        return 1.0
    N -= ((4*(D-1)+1)+1)*D//2
    if N < Y+1:
        return 0.0
    if N >= 2*D+Y+1:
        return 1.0
    result = c = binomial(N, Y+1)
    for k in xrange((Y+1)+1, N+1):
        c *= N-k+1
        c //= k
        result += c
    return float(result)/(2**N)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, falling_diamonds())

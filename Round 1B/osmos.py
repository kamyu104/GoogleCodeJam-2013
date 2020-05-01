# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2013 Round 1B - Problem A. Osmos
# https://code.google.com/codejam/contest/2434486/dashboard#s=p0
#
# Time:  O(NlogN)
# Space: O(1)
#

def osmos():
    curr, N = map(int, raw_input().strip().split())
    motes = sorted(map(int, raw_input().strip().split()))
    result = 0
    for i, mote in enumerate(motes):  # Time: O(N)
        for _ in xrange(N - max(i, result)):
            if curr > mote:
                curr += mote
                break
            curr += curr-1
            result += 1  # at most N times
        else:
            break
    return result        

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, osmos())

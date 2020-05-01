# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2013 Round 1B - Problem C. Garbled Email
# https://code.google.com/codejam/contest/2434486/dashboard#s=p2
#
# Time:  hash: O(N * L^3), N is the number of words
#                        , L is the max length of words
#        dp:   O(S * D * L^4)
# Space: hash: O(N * L^3)
#        dp:   O(S * D)
#

def garbled_email():
    S = raw_input().strip()
    dp = [[float("inf") for _ in xrange(D)] for _ in xrange(len(S)+1)]
    dp[0][-D] = 0
    for i in xrange(len(S)):
        for j in xrange(-D, 0):
            for l in xrange(1, min(L, len(S)-i)+1):
                word = S[i:i+l]
                # no change
                if word in LOOKUP:
                    prev = max(j-l, -D)  # merge states
                    dp[i+l][prev] = min(dp[i+l][prev], dp[i][j])
                # one change
                for k in xrange(j+D, l):
                    if word[:k]+'*'+word[k+1:] not in LOOKUP:
                        continue
                    prev = max(k-l, -D)  # merge states
                    dp[i+l][prev] = min(dp[i+l][prev], dp[i][j]+1)
                # two changes
                for k in xrange(j+D, l):
                    for m in xrange(k+D, l):
                        if word[:k]+'*'+word[k+1:m]+'*'+word[m+1:] not in LOOKUP:
                            continue
                        prev = max(m-l, -D)  # merge states
                        dp[i+l][prev] = min(dp[i+l][prev], dp[i][j]+2)
    return min(dp[-1])

D, L = 5, 0
LOOKUP = set()
with open("garbled_email_dictionary.txt") as f:
    for line in f:
        word = line.strip()
        L = max(L, len(word))
        LOOKUP.add(word)
        for j in xrange(len(word)):
            LOOKUP.add(word[:j]+'*'+word[j+1:])
        for j in xrange(len(word)-D):
            for k in xrange(j+D, len(word)):
                LOOKUP.add(word[:j]+'*'+word[j+1:k]+'*'+word[k+1:])
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, garbled_email())

# Copyright (c) 2020 kamyu. All rights reserved.
#
# Google Code Jam 2013 Round 1C - Problem C. The Great Wall
# https://code.google.com/codejam/contest/2437488/dashboard#s=p2
#
# Time:  O(AlogA), A is the number of total attacks
# Space: O(A)
#

# Template:
# https://github.com/kamyu104/FacebookHackerCup-2018/blob/master/Final%20Round/the_claw.py
class SegmentTree(object):
    def __init__(self, N,
                 build_fn=lambda x, y: [y]*(2*x),
                 query_fn=max,
                 update_fn=lambda x, y: y if x is None else x+y,
                 default_val=0):
        self.N = N
        self.H = (N-1).bit_length()
        self.query_fn = query_fn
        self.update_fn = update_fn
        self.default_val = default_val
        self.tree = build_fn(N, default_val)
        self.lazy = [None]*N

    def __apply(self, x, val):
        self.tree[x] = self.update_fn(self.tree[x], val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)

    def update(self, L, R, h):  # Time: O(logN), Space: O(N)
        def pull(x):
            while x > 1:
                x //= 2
                self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])
                if self.lazy[x] is not None:
                    self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])
        L += self.N
        R += self.N
        L0, R0 = L, R
        while L <= R:
            if L & 1:  # is right child
                self.__apply(L, h)
                L += 1
            if R & 1 == 0:  # is left child
                self.__apply(R, h)
                R -= 1
            L //= 2
            R //= 2
        pull(L0)
        pull(R0)

    def query(self, L, R):  # Time: O(logN), Space: O(N)
        def push(x):
            n = 2**self.H
            while n != 1:
                y = x // n
                if self.lazy[y] is not None:
                    self.__apply(y*2, self.lazy[y])
                    self.__apply(y*2 + 1, self.lazy[y])
                    self.lazy[y] = None
                n //= 2

        result = None  # modified for max-min query
        if L > R:
            return result

        L += self.N
        R += self.N
        push(L)
        push(R)
        while L <= R:
            if L & 1:  # is right child
                result = self.query_fn(result, self.tree[L])
                L += 1
            if R & 1 == 0:  # is left child
                result = self.query_fn(result, self.tree[R])
                R -= 1
            L //= 2
            R //= 2
        return result
    
    def __str__(self):
        showList = []
        for i in xrange(self.N):
            showList.append(self.query(i, i))
        return ",".join(map(str, showList))

def the_great_wall():
    N = input()
    attacks = []
    x_set = set()
    for _ in xrange(N):
        di, ni, wi, ei, si, delta_di, delta_pi, delta_si = map(int, raw_input().strip().split())
        for _ in xrange(ni):
            attacks.append([di, wi, ei, si])
            x_set.add(wi)
            x_set.add(ei)
            di += delta_di
            wi += delta_pi
            ei += delta_pi
            si += delta_si
    segment_tree = SegmentTree(2*len(x_set),
                               query_fn=lambda x, y: y if x is None else max(x, y),
                               update_fn=lambda x, y: y if x is None else min(x, y),
                               default_val=float("inf"))
    x_to_idx = {x: 2*i for i, x in enumerate(sorted(x_set))}  # Time: O(AlogA), coordinate compression of x, 2*i is for keeping interval discrete
    result = 0
    attacks.sort(key=lambda x: (-x[3], x[0]))  # sort si descendingly, di ascendingly
    for di, wi, ei, si in attacks:
        if di <= segment_tree.query(x_to_idx[wi], x_to_idx[ei]):
            result += 1
        segment_tree.update(x_to_idx[wi], x_to_idx[ei], di)
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, the_great_wall())

#!/usr/bin/env python
# coding: utf-8

# Homework Assignment
# DP - Local sequence alignment 

class LocalAlign():
    def __init__(self, match, mismatch, indel, th, m, n):
        self.match = match 
        self.mismatch = mismatch
        self.indel = indel
        self.th = th

        self.m = m
        self.n = n
        #self.sequence = [0]*(self.n+1)

        self.result = []

    def align(self, p, s):
        score = [0]*(self.m+1)
        dprev = 0
        iprev = 0
        jprev = 0
        #patt = [0]*(self.m+1)

        # Compute score alignment for all position of sequence
        for j in range(1, self.n + 1):
            #score[0] = 0
            dprev = 0
            for i in range(1, self.m + 1):
                # print('s and p', s[j-1], p[i -1])
                # print('patt:', patt)
                # print('i-1, j-1:', patt[i-1] + (self.match if s[j-1] == p[i-1] else self.mismatch))
                # print('i, j-1:', patt[i] + self.indel)
                # print('i-1, j:', score[i - 1] + self.indel)
                iprev = score[i-1]
                jprev = score[i]

                # print('dprev', dprev)
                # print('iprev', iprev)
                # print('jprev', jprev)

                currd = max(dprev + (self.match if s[j-1] == p[i-1] else self.mismatch),
                            jprev + self.indel,
                            iprev + self.indel)

                # score[i] = max(patt[i-1] + (self.match if s[j-1] == p[i-1] else self.mismatch),
                #             patt[i] + self.indel,
                #             score[i - 1] + self.indel)

                dprev = score[i]
                score[i] = currd
                

                #print('score', i, ':', score[i])
                if i == self.m:
                    #print('last:',i)
                    if score[i] >= self.th:
                        #self.result[j] = score[i]
                        self.result.append((j,score[i]))
            
                    #print('prev score',patt)
                    #patt = score.copy()
                    
        
        return self.result


ma, mi, d, th = map(int, input().split())
m, n = map(int, input().split())
p = [char for char in input()]
s = [char for char in input()]


approxMatching = LocalAlign(ma, mi, d, th, m, n)
res = approxMatching.align(p, s)

#print(res)
for l in res:
    print(l[0], l[1])

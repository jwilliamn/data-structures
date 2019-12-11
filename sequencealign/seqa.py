#!/usr/bin/env python
# coding: utf-8

# Homework Assignment
# DP - Local sequence alignment 
import sys

class LocalAlign():
    def __init__(self, match, mismatch, indel, th, m, n):
        self.match = match 
        self.mismatch = mismatch
        self.indel = indel
        self.th = th

        self.m = m
        self.n = n
        #self.sequence = [0]*(self.n+1)

        #self.result = []

    def align(self, p):
        score = [0]*(self.m+1)
        dprev = 0 # s(i-1, j-1)
        iprev = 0 # s(i-1, j)
        jprev = 0 # s(i, j-1)

        # Compute score alignment for all position of sequence
        for j in range(1, self.n + 1):
            s = sys.stdin.read(1)
            dprev = 0
            for i in range(1, self.m + 1):
                #print('s_char', s)
                iprev = score[i-1]
                jprev = score[i]

                currd = max(dprev + (self.match if s == p[i-1] else self.mismatch),
                            jprev + self.indel,
                            iprev + self.indel)

                dprev = score[i]
                score[i] = currd
                
                #print('score:', score[i])
                if i == self.m:
                    #print('last:',i)
                    if score[i] >= self.th:
                        print(j, score[i])
                        #self.result.append((j,score[i]))
                    
        
        #return self.result


ma, mi, d, th = map(int, input().split())
m, n = map(int, input().split())
# p = [char for char in input()]
# s = [char for char in input()]
p = input()
approxMatching = LocalAlign(ma, mi, d, th, m, n)
approxMatching.align(p)

#s = input()

#approxMatching.align(p, s)

#print(res)
# for l in res:
#     print(l[0], l[1])

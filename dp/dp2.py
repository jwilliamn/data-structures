#!/usr/bin/env python
# coding: utf-8

# Homework Assignment
# Dynamic programming 

class DP():
    def __init__(self, n, l):
        self.n = n 
        self.l = l
        self.INF = 2147483647
        self.margin = [0]*(n+1)
        self.mincost = 0
        self.result = [0]*(n+1)

    def justify(self, lwords):
        costM = [self.INF]*(n+1)
        costM[0] = 0            

        # Min cost of margin
        for i in range(1, self.n + 1):
            #costM.append(costM[i -1] + len(words[i-1]))
            self.margin[i] = self.margin[i -1] + lwords[i-1]
            for j in range(i, 0, -1):
                words_length = (self.margin[i] - self.margin[j-1] + i - j)
                if words_length > self.l:
                    break 
                else:
                    self.mincost = (self.l - words_length)**2
                    new_costM = costM[j-1] + self.mincost
                    if new_costM < costM[i]:
                        costM[i] = new_costM
                        self.result[i] = self.result[j -1] + 1
                    
        
        return costM, self.result


n, l = map(int, input().split())
lwords = [len(x) for x in input().split()]

dp = DP(n,l)
minc, res = dp.justify(lwords)

#print(minc, res)
print(minc[-1], res[-1])

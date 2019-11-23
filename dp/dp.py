#!/usr/bin/env python
# coding: utf-8

# Homework Assignment
# Dynamic programming 

class DP():
    def __init__(self, n, l):
        self.n = n 
        self.l = l
        self.INF = 2147483647
        self.mincost = [0]*n
        self.result = [0]*n

    def justify(self, words):
        costM = [[0 for i in range(self.n)] for j in range(self.n)]

        #print(costM)
        
        for i in range(self.n):
            costM[i][i] = self.l - len(words[i])
            for j in range(i+1,self.n):
                costM[i][j] = costM[i][j-1] - len(words[j]) - 1
        
        # Badness: Distance from the page limit - total length of words
        # 2nd part is define recurrence
        for i in range(self.n):
            for j in range(i,self.n):
                if costM[i][j] < 0:
                    costM[i][j] = self.INF
                else:
                    costM[i][j] = costM[i][j]**2
                

        #print(costM)
        for i in range(self.n-1, -1,-1):
            self.mincost[i] = costM[i][self.n - 1]
            self.result[i] = self.n
            #print(self.mincost)
            for j in range(self.n-1, i, -1):
                if costM[i][j-1] == self.INF:
                    pass
                if self.mincost[i] > self.mincost[j] + costM[i][j-1]:
                    self.mincost[i] = self.mincost[j] + costM[i][j-1]
                    self.result[i] = j
        
        return self.mincost, self.result


n, l = map(int, input().split())
words = [x for x in input().split()]

dp = DP(n,l)
minc, res = dp.justify(words)

nl = 0
i = 0
j = 0
while j < n:
    j = res[i]
    f = False
    for i in range(j):
        f = True
    if f:
        nl+=1
    i = j

print(minc[0], nl)

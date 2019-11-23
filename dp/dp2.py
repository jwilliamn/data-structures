#!/usr/bin/env python
# coding: utf-8

# Homework Assignment
# Dynamic programming 

INF = 2147483647
def numLines(p, n): 
    k = 0
    if p[n] == 1: 
        k = 1
    else: 
        k = numLines(p, p[n] - 1) + 1
    return k 
  
def justify (lwords, n, l): 
    margin = [[0 for i in range(n + 1)] 
                 for i in range(n + 1)] 
                   
    margincost = [[0 for i in range(n + 1)] 
             for i in range(n + 1)] 

    # Optimum cost 
    c = [0 for i in range(n + 1)] 
    
    # Indexes of words
    p = [0 for i in range(n + 1)] 
      
    for i in range(n + 1):
        margin[i][i] = l - lwords[i - 1] 
        for j in range(i + 1, n + 1): 
            margin[i][j] = (margin[i][j - 1] - 
                                    lwords[j - 1] - 1) 
    # Cost computation                          
    for i in range(n + 1): 
        for j in range(i, n + 1): 
            if margin[i][j] < 0: 
                margincost[i][j] = INF; 
            else: 
                margincost[i][j] = (margin[i][j] ** 
                            2) 
  
    # Compute minimum cost and find words in each line
    c[0] = 0
    for j in range(1, n + 1): 
        c[j] = INF 
        for i in range(1, j + 1): 
            if (c[i - 1] != INF and 
                margincost[i][j] != INF and 
                ((c[i - 1] + margincost[i][j]) < c[j])): 
                c[j] = c[i-1] + margincost[i][j] 
                p[j] = i 
    return c, p


n, l = map(int, input().split())
lwords = [len(x) for x in input().split()]

c, p = justify(lwords, n, l) 
k = numLines(p, n)

print(c[-1], k)

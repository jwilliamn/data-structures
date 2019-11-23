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
    #print('Line number ', k, ': From word no. ', 
    #                             p[n], 'to ', n) 
    return k 
  
def solveWordWrap (l, n, M): 
      
    # For simplicity, 1 extra space is 
    # used in all below arrays  
  
    # extras[i][j] will have number  
    # of extra spaces if words from i  
    # to j are put in a single line 
    extras = [[0 for i in range(n + 1)] 
                 for i in range(n + 1)] 
                   
    # lc[i][j] will have cost of a line  
    # which has words from i to j 
    lc = [[0 for i in range(n + 1)] 
             for i in range(n + 1)] 
               
    # c[i] will have total cost of  
    # optimal arrangement of words  
    # from 1 to i 
    c = [0 for i in range(n + 1)] 
      
    # p[] is used to print the solution. 
    p = [0 for i in range(n + 1)] 
      
    # calculate extra spaces in a single 
    # line. The value extra[i][j] indicates 
    # extra spaces if words from word number 
    # i to j are placed in a single line  
    for i in range(n + 1):
        extras[i][i] = M - l[i - 1] 
        for j in range(i + 1, n + 1): 
            extras[i][j] = (extras[i][j - 1] - 
                                    l[j - 1] - 1) 
                                      
    # Calculate line cost corresponding  
    # to the above calculated extra  
    # spaces. The value lc[i][j] indicates  
    # cost of putting words from word number 
    # i to j in a single line  
    for i in range(n + 1): 
        for j in range(i, n + 1): 
            if extras[i][j] < 0: 
                lc[i][j] = INF; 
            #elif j == n and extras[i][j] >= 0: 
            #    lc[i][j] = 0
            else: 
                lc[i][j] = (extras[i][j] ** 
                            2) 
  
    # Calculate minimum cost and find  
    # minimum cost arrangement. The value 
    # c[j] indicates optimized cost to  
    # arrange words from word number 1 to j. 
    c[0] = 0
    for j in range(1, n + 1): 
        c[j] = INF 
        for i in range(1, j + 1): 
            if (c[i - 1] != INF and 
                lc[i][j] != INF and 
                ((c[i - 1] + lc[i][j]) < c[j])): 
                c[j] = c[i-1] + lc[i][j] 
                p[j] = i 
    return c, p
    #printSolution(p, n) 


# Driver Code 

n, l = map(int, input().split())

words = [len(x) for x in input().split()]

c, p = solveWordWrap(words, n, l) 
k = printSolution(p, n)

print(c[-1], k)

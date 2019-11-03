#!/usr/bin/env python
# coding: utf-8

# Homework Assignment
# Hash Table 

class MyHash():
    def __init__(self, n):
        self.hash_table = [[] for _ in range(n)]

    def hashing_func(self, hash_table, key):
        hashsum = key[0]*(10**9) + key[1]
        return hashsum%len(hash_table)

    def insert(self, hash_table, key, value):
        hash_key = self.hashing_func(hash_table, key)
        bucket = hash_table[hash_key]
        ne = 0

        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                if value > v:
                    # update hash table with the max new min dimension
                    bucket[i] = (key,value)
            else:
                ne += 1
        if ne == len(bucket):
            bucket.append((key,value))

    def search(self, hash_table, key):
        hash_key = self.hashing_func(hash_table, key)
        bucket = hash_table[hash_key]
        return bucket


dmax = 0
dcurr = 0
count = 0
f = True

n = int(input())
myhash = MyHash(n)
hash_table = myhash.hash_table

while n:
    a, b, c = map(int, input().split())
    
    box = [a,b,c]

    nbox = sorted(box)
    pair = tuple(nbox[1:])
    dmin = nbox[0]

    f = True
    # First skip if max dim is less than the global max
    if dmin > dmax:
        #count += 1
        dmax = dmin

        bucket = myhash.search(hash_table, pair)
        nbucket = len(bucket)
        for i in range(nbucket):
            k, v = bucket[i]
            if pair == k or pair[::-1] == k:
                dcurr = min(min(pair), v + dmin)
                if dcurr > dmax:
                    #print('yes')
                    #count += 1
                    dmax = dcurr
        count += 1

    else:
        if min(pair) < dmax:
            f = False
        else:
            nf = False
            bucket = myhash.search(hash_table, pair)
            nbucket = len(bucket)
            for i in range(nbucket):
                k, v = bucket[i]
                if pair == k or pair[::-1] == k:
                    dcurr = min(min(pair), v + dmin)
                    if dcurr > dmax:
                        #print('yes')
                        #count += 1
                        nf = True
                        dmax = dcurr
            
            if nf:
                count += 1

    if f:
        myhash.insert(hash_table, pair, dmin)
    
    #print('count',count)
    #print(dmax)
    n-=1

#print(hash_table)
print(count)
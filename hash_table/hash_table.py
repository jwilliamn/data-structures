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
f = False

n = int(input())
myhash = MyHash(n)
hash_table = myhash.hash_table

while n:
    a, b, c = map(int, input().split())
    
    box = [a,b,c]
    dmin = min(box)
    box.remove(dmin)
        
    pair = tuple(box)
    # First skip if max dim is less than the global max
    if max(a,b,c) > dmax:
        bucket = myhash.search(hash_table, pair)

        if bucket:
            nbucket = len(bucket)
            while nbucket:
                k, v = bucket[nbucket - 1]
                if pair == k or pair[::-1] == k:
                    dcurr = min(min(pair), v + dmin)
                    if dcurr > dmax:
                        f = True
                
                nbucket -= 1
            
        if not f:
            dcurr = dmin
            if dcurr > dmax:
                f = True

        if f:
            count += 1
            dmax = dcurr
            f = False
            
        myhash.insert(hash_table, pair, dmin)

    n-=1

#print(hash_table)
print(count)
#!/usr/bin/env python
# coding: utf-8

# Homework Assignment
# Hash Table 

def hashing_func(hash_table, key):
    return hash(key)%len(hash_table)

def insert(hash_table, key, value):
    hash_key = hashing_func(hash_table, key)
    bucket = hash_table[hash_key]
    ne = 0

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            if value > v:
                #print('bucket before', bucket)
                #print('condition holds')
                #print('dbucket after', bucket)
                bucket[i] = (key,value)
        else:
            ne += 1
    if ne == len(bucket):
        bucket.append((key,value))

def search(hash_table, key):
    hash_key = hashing_func(hash_table, key)
    bucket = hash_table[hash_key]
    return bucket


dmax = 0
dcurr = 0
count = 0
f = False

n = int(input())
# set hash table with a fix number
hash_table = [[] for _ in range(n)]

while n:
    a, b, c = map(int, input().split())
    
    box = [a,b,c]
    dmin = min(box)
    box.remove(dmin)
        
    pair = tuple(box)
    # First check the min 
    # skip the box
    if max(a,b,c) > dmax:
        # update hash table with the max new min dimension
        bucket = search(hash_table, pair)

        if bucket:
            nbucket = len(bucket)
            while nbucket:
                k, v = bucket[nbucket - 1]
                if pair == k:
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
            
        insert(hash_table, pair, dmin)

    n-=1

#print(hash_table)
print(count)
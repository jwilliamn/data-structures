# Hash Table

from collections import defaultdict

n = int(input())
dmax = 0
dcurr = 0
count = 0
f = False
dicv = defaultdict(list)
while n:
    a, b, c = map(int, input().split())
    pairs = {(a,b):c, (b,c):a, (a,c):b}
    notpair = 0

    box = [a,b,c]
    dtmp = min(box)
    while dtmp in box:
        box.remove(dtmp)
        
    pair = tuple(box)


    #print(pairs)
    for pair in pairs:
        if dicv.get(pair) and len(dicv[pair]) == 1:
                newbox = list(pair)
                nedge = dicv[pair][0] + pairs[pair]
                newbox.append(nedge)
                dcurr = min(newbox)
                if dcurr > dmax:
                    count += 1
                    dmax = dcurr
                if pairs[pair] != dicv[pair]:   
                    dicv[pair].append(pairs[pair])
        elif dicv.get(pair) and len(dicv[pair]) > 1:
            for i in range(len(dicv[pair])):
                newbox = list(pair)
                nedge = dicv[pair][i] + pairs[pair]
                newbox.append(nedge)
                dcurr = min(newbox)
                # check this logic
                if dcurr > dmax:
                    f = True
                if pairs[pair] != dicv[pair]:   
                    dicv[pair].append(pairs[pair])
            if f:
                count += 1
                dmax = dcurr
        else:
            notpair += 1
            dicv[pair].append(pairs[pair])
    
    if notpair == len(pairs):
        if min(a,b,c) > dmax:
            count += 1
            dmax = min(a,b,c)
    n-=1

print(count)
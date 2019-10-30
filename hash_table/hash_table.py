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

    if dicv.get(pair) and len(dicv[pair]) == 1:
            newbox = list(pair)
            nedge = dicv[pair][0] + dtmp
            newbox.append(nedge)
            dcurr = min(newbox)
            if dcurr > dmax:
                count += 1
                dmax = dcurr
            if dtmp != dicv[pair]:   
                dicv[pair].append(dtmp)
    elif dicv.get(pair) and len(dicv[pair]) > 1:
        for i in range(len(dicv[pair])):
            newbox = list(pair)
            nedge = dicv[pair][i] + dtmp
            newbox.append(nedge)
            dcurr = min(newbox)
            if dcurr > dmax:
                f = True
            if dtmp != dicv[pair]:   
                dicv[pair].append(dtmp)
        if f:
            count += 1
            dmax = dcurr
            f = False
    else:
        if dtmp > dmax:
            count += 1
            dmax = dtmp

        if len(pair) == 0:
            dicv[(a,b)].append(c)
        elif len(pair) == 1:
            dicv[(dtmp,dtmp)].append(box[0])
            dicv[(dtmp,box[0])].append(dtmp)
            
    n-=1

print(count)
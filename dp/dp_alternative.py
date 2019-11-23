
class DynamicP():
    def __init__(self, n, l, words):
        self.n = n 
        self.l = l
        self.INF = 2147483647
        self.words = words
        self.bestchoice = [0]*n
        self.result = [-1]*n

    def badness(self, i, j):
        subw = self.words[i:j]
        spaces = j - i
        total = spaces
        for a in subw:
            total += len(a)

        if total > self.l:
            return self.INF
        else:
            return (self.l - total - spaces)**2

    def DP(self, i):
        print('i', i)
        if i == self.n:
            return 0
        if self.result[i] != -1:
            return self.result[i]

        mincost = self.INF 
        for j in range(i+1, self.n + 1):
            print('j', j)
            cost = self.badness(i, j) + self.DP(j)

            if mincost > cost:
                print('yes')
                self.bestchoice[i] = j
                mincost = cost
            
        self.result[i] = mincost
        return mincost


n, l = map(int, input().split())
words = [x for x in input().split()]

dp = DynamicP(n,l,words)
minc = dp.DP(0)

print(minc)
print(dp.bestchoice)
print(dp.result)
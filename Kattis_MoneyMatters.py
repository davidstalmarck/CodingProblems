# you can find the problem here https://open.kattis.com/problems/moneymatters
# partly written by David Stålmarck 2020-01-19, the class UnionFind is from stackoverflow if I remember correct

class UnionFind:

    def __init__(self, N):
        self.N = N
        self.parent = [i for i in range(self.N)]
        self._rank = [1] * self.N

    def find(self, x):
        while x != self.parent[self.parent[x]]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unite(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self._rank[j] > self._rank[i]:
            i, j = j, i
        self.parent[j] = i
        self._rank[i] += self._rank[j]


friends, friendships = tuple(map(int, input().split()))
balances = [int(input()) for n in range(friends)]

u = UnionFind(friends)

for n in range(friendships):
    u.unite(*tuple(map(int, input().split())))

groups = [0] * friends
for n in range(friends):
    groups[u.find(n)] += balances[n]

if any(groups):
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
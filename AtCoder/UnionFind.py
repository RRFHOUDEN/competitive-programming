class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def sample():
    uf = UnionFind(6)
    print(uf.parents)
    uf.union(0, 2)
    print(uf.parents)
    uf.union(1, 3)
    print(uf.parents)
    uf.union(4, 5)
    print(uf.parents)

def atc001():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    for i in range(q):
        p, a, b = map(int, input().split())
        if p == 0:
            uf.union(a, b)
        else:
            if uf.same(a, b):
                print("Yes")
            else:
                print("No")

def abc049():
    n, k, l = map(int, input().split())
    road = UnionFind(n)
    train = UnionFind(n)
    for i in range(k):
        p, q = map(int, input().split())
        road.union(p - 1, q - 1)
    for i in range(l):
        p, q = map(int, input().split())
        train.union(p - 1, q - 1)

    pair = []
    pair_cnt = {}
    for i in range(n):
        t, r = road.find(i), train.find(i)
        pair.append([t, r])
        key = t * (10 ** 6) + r
        if key in pair_cnt:
            pair_cnt[key] += 1
        else:
            pair_cnt[key] = 1

    for i in range(n):
        [t, r] = pair[i]
        key = t * (10 ** 6) + r
        print(pair_cnt[key], end = " ")

def arc097():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    pair = UnionFind(n)
    for i in range(m):
        x, y = map(int, input().split())
        pair.union(x - 1, y - 1)

    cnt = 0
    for i in range(n):
        if pair.same(i, p[i] - 1):
            cnt += 1
    print(cnt)

def arc032():
    n, m = map(int, input().split())
    road = UnionFind(n)
    for i in range(m):
        a, b = map(int, input().split())
        road.union(a - 1, b - 1)

    print(road.group_count() - 1)

def abc075():
    n, m = map(int, input().split())
    input_list = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0
    for i in range(m):
        road = UnionFind(n)
        for j in range(m):
            p1 = input_list[j][0] - 1
            p2 = input_list[j][1] - 1
            if i != j:
                road.union(p1, p2)
        if road.group_count() >= 2:
            cnt += 1

    print(cnt)
abc075()
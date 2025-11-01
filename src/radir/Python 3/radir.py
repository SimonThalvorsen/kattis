from itertools import *

n, p = map(int, input().split())
c = [tuple(map(int, input().split())) for _ in range(n)]
f = lambda h: any(
    sorted(v)[i + 1] == v[i] + 1 == v[i + 2] - 1
    for s in {x[0] for x in h}
    for v in [[x[1] for x in h if x[0] == s]]
    for i in range(len(v) - 2)
)
hands = {tuple(c[:p])}
if any(f(x) for x in hands):
    print(0)
    exit()
for t in range(p, n):
    nc = c[t]
    nh = set()
    for h in hands:
        hh = list(h) + [nc]
        for i in range(len(hh)):
            nh.add(tuple(sorted(hh[:i] + hh[i + 1 :])))
    hands = nh
    if any(f(x) for x in hands):
        print(t - p + 1)
        exit()
print("Neibb")

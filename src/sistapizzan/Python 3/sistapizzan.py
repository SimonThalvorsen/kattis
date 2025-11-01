N = int(input())
p = [int(input()) for _ in range(N)]
print("Ja" if (not sum(p) & 1 ^ (len(p) > 1)) or sum(p[:-1]) & 1 else "Nej")

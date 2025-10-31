from decimal import Decimal

a, b, c = input().split()
print(Decimal(a) * Decimal(b) / Decimal(c))

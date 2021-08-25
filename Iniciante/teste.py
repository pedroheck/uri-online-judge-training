A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

c = min(A, B, C)
a = max(A, B, C)
b = round(A + B + C - c - a, 1)

print(a)
print(b)
print(c)

print("\n")
print(95.4 + 95.4 + 95.4 - 95.4 - 95.4)

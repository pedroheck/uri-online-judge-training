X, Y = input().split()

X = int(X)
Y = int(Y)

if X == 1:
    total = 4 * Y
if X == 2:
    total = 4.5 * Y
if X == 3:
    total = 5 * Y
if X == 4:
    total = 2 * Y
if X == 5:
    total = 1.5 * Y

print("Total: R$ %.2f" % total)

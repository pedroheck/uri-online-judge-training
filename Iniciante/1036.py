import math
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if b**2 - 4*a*c < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    r2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print("R1 = %.5f" % r1)
    print("R2 = %.5f" % r2)

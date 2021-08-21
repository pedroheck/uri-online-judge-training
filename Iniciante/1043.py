A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

if A >= B + C or B >= C + A or C >= A + B or A <= abs(B - C) or B <= abs(A - C) or C <= abs(A - B):
    area = (A + B)*C/2
    print("Area = %.1f" % area)
else:
    perimetro = A + B + C
    print("Perimetro = %.1f" % perimetro)

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

c = min(A, B, C)
a = max(A, B, C)
b = round(A + B + C - c - a, 1)  # Sem o round, dá erro por conta do float

if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
elif a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")


if a == b and b == c:
    print("TRIANGULO EQUILATERO")
elif a == b or b == c or a == c:
    print("TRIANGULO ISOSCELES")

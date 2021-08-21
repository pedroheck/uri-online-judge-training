A, B, C = input().split()

A = float(A)
B = float(B)
C = float(C)

area_triangle = (A * C)/2
area_circle = 3.14159 * C**2
area_trapezium = (A + B)*C/2
area_square = B**2
area_rectangle = A*B

print("TRIANGULO: %.3f" % area_triangle)
print("CIRCULO: %.3f" % area_circle)
print("TRAPEZIO: %.3f" % area_trapezium)
print("QUADRADO: %.3f" % area_square)
print("RETANGULO: %.3f" % area_rectangle)

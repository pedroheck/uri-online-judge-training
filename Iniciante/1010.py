code1, units1, price1 = input().split()
code2, units2, price2 = input().split()

valor = float(float(units1)*float(price1)) + float(float(units2)*float(price2))

print("VALOR A PAGAR: R$ %.2f" % valor)

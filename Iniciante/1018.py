n = int(input())

notas_cem = n//100
notas_cinquenta = (n % 100)//50
notas_vinte = ((n % 100) % 50)//20
notas_dez = (((n % 100) % 50) % 20)//10
notas_cinco = ((((n % 100) % 50) % 20) % 10)//5
notas_dois = (((((n % 100) % 50) % 20) % 10) % 5)//2
notas_um = int(((((((n % 100) % 50) % 20) % 10) % 5) % 2)/1)

print(n)
print(notas_cem, "nota(s) de R$ 100,00")
print(notas_cinquenta, "nota(s) de R$ 50,00")
print(notas_vinte, "nota(s) de R$ 20,00")
print(notas_dez, "nota(s) de R$ 10,00")
print(notas_cinco, "nota(s) de R$ 5,00")
print(notas_dois, "nota(s) de R$ 2,00")
print(notas_um, "nota(s) de R$ 1,00")

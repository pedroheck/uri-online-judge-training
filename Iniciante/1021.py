n = float(input()) + 0.001

notas_cem = n//100
notas_cinquenta = (n % 100)//50
notas_vinte = ((n % 100) % 50)//20
notas_dez = (((n % 100) % 50) % 20)//10
notas_cinco = ((((n % 100) % 50) % 20) % 10)//5
notas_dois = (((((n % 100) % 50) % 20) % 10) % 5)//2

moedas_um = ((((((n % 100) % 50) % 20) % 10) % 5) % 2)//1
moedas_cinquenta = (((((((n % 100) % 50) % 20) % 10) % 5) % 2) % 1)//.5
moedas_vinte_e_cinco = (
    (((((((n % 100) % 50) % 20) % 10) % 5) % 2) % 1) % .5)//.25
moedas_dez = (
    ((((((((n % 100) % 50) % 20) % 10) % 5) % 2) % 1) % .5) % .25)//.10
moedas_cinco = (
    (((((((((n % 100) % 50) % 20) % 10) % 5) % 2) % 1) % .5) % .25) % .10)//.05
moedas_zero_um = (
    ((((((((((n % 100) % 50) % 20) % 10) % 5) % 2) % 1) % .5) % .25) % .10) % .05)//.01


print("NOTAS:")
print(int(notas_cem), "nota(s) de R$ 100.00")
print(int(notas_cinquenta), "nota(s) de R$ 50.00")
print(int(notas_vinte), "nota(s) de R$ 20.00")
print(int(notas_dez), "nota(s) de R$ 10.00")
print(int(notas_cinco), "nota(s) de R$ 5.00")
print(int(notas_dois), "nota(s) de R$ 2.00")
print("MOEDAS:")
print(int(moedas_um), "moeda(s) de R$ 1.00")
print(int(moedas_cinquenta), "moeda(s) de R$ 0.50")
print(int(moedas_vinte_e_cinco), "moeda(s) de R$ 0.25")
print(int(moedas_dez), "moeda(s) de R$ 0.10")
print(int(moedas_cinco), "moeda(s) de R$ 0.05")
print(int(moedas_zero_um), "moeda(s) de R$ 0.01")

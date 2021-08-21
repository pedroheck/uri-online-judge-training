t = int(input())

years = t // 365
months = (t % 365) // 30
days = (t % 365) % 30

print(years, "ano(s)")
print(months, "mes(es)")
print(days, "dia(s)")

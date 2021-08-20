list_of_positives = []
counter = 0
sum = 0

for i in range(6):
    n = float(input())
    if n > 0:
        list_of_positives.append(n)

for i in list_of_positives:
    sum += i

print(len(list_of_positives), "valores positivos")
print("%.1f" % (sum/len(list_of_positives)))


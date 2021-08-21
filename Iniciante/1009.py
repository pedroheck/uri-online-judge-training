name = input()
fixed_salary = float(input())
sold = float(input())

total_recieved = fixed_salary + 0.15*sold

print("TOTAL = R$ %.2f" % total_recieved)

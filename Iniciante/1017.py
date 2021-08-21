time_hours = int(input())
speed_km_h = int(input())

distance_km = time_hours * speed_km_h

liters_gas = float(distance_km/12)

print("%.3f" % liters_gas)

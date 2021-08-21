N = int(input())

hours = N // 3600
minutes = (N % 3600) // 60
seconds = ((N % 3600) % 60)

print("%d:%d:%d" % (hours, minutes, seconds))

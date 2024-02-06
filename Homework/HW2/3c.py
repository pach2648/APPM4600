import math

x = 9.999999995000000*10**(-10)
y = math.e**x
result = y-1

print(y)
print(result)

condition_number = abs((x*math.e**x)/((math.e**x)-1))
print(condition_number)

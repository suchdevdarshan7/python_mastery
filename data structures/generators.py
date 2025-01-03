from sys import getsizeof
values = (x*2 for x in range(1000000))

print(values)

print(type(values))

print(getsizeof(values))


values2 = [x*2 for x in range(1000000)]

print(type(values2))

print(getsizeof(values2))

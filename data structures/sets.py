numbers = [1, 2, 3, 4, 5, 6, 6]

newSet = set(numbers)

colors = set([1, 2, 3, 4])


print(newSet)
print(colors)


#  a union b

print(newSet | colors)

# a intersection b

print(newSet & colors)

# a difference b

print(newSet - colors)

# symmetric difference a and b

print(newSet ^ colors)

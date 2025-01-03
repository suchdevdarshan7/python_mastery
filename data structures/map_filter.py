items = [
    ('Product 1', 199),
    ('Product 2', 289),
    ('Product 3', 19),
]

# x = list(map(lambda x: x[1], items))

# x.sort()

# print(x)


filtered = list(filter(lambda x: x[1] > 100, items))

print(filtered)

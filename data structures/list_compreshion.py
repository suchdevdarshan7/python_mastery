items = [
    ('Product 1', 199),
    ('Product 2', 289),
    ('Product 3', 19),
]

filtered = [item for item in items if item[1] > 100]


print(filtered)

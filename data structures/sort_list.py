# numbers = [10, 39, 34, 2, 35, 1, 3]


# # numbers.sort(reverse=True)

# sorted(numbers)

# print(numbers)

# positional arguments are the arguments which are the position of a paticular parameter

# sort has keyword arguments


# def sort_items(items):
#     return items[1]


items = [
    ('Product 1', 99),
    ('Product 2', 289),
    ('Product 3', 19),
]

# items.sort(key=sort_items)

items.sort(key=lambda item: item[1])


print(items)

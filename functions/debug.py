def multiply(*numbers):
    total = 1

    for i in numbers:
        total *= i
    return total


ans = multiply(1, 2, 3, 4, 5)

print(ans)


# ~ If we use xargs we can use the parameter as a list
def multiply(*numbers):
    total = 1

    for i in numbers:
        total *= i
    return total


answer = multiply(2, 3, 4, 5,)

print(answer)

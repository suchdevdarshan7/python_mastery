
# ^ You can write the name of the parameter while you pass it as a argument when calling the function it is for readiblty purposes


def increment(number, by):
    return number + by


print(increment(2, by=1))


# ~ Default parameter

def incrementDefault(number, by=1):
    return number + by


value = incrementDefault(3)
print(value)

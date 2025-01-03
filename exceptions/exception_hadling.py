try:
    a = int(input("Age:"))
except ValueError as e:
    print(e)
    print(type(e))
else:
    print("No exception was thrown ")


print("Execution continues")

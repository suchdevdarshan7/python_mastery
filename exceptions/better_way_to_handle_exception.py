from timeit import timeit

code2 = """
def calculate_age(age=10):
    if age <= 0:
        raise ValueError("Age must be above zero")
try:
    calculate_age()
except ValueError as error:
    pass
"""


code1 = """
def calculate_age(age):
    if age <= 0:
        return None

ans = calculate_age(-1)
if ans is None:
    pass
"""

print("first code", timeit(code2, number=10000))
print("second code", timeit(code1, number=10000))

def fizz_buzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    else:
        return number


print(fizz_buzz(7))

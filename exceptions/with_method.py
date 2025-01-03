

try:
    with open('./exceptions/app.py') as file:
        print("File opened")
except FileNotFoundError as error:
    print(error)
else:
    print("No exception was found!")

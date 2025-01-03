try:
    file = open('app.txt')  # Attempt to open the file
    ans = file.read()
    print(ans)
    a = int(input("Age:"))
    xfactor = 10 / a
except FileNotFoundError:
    print("The file was not found.")
    file = None  # Ensure file is defined, even if it wasn't opened
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    if file:  # Check if the file was successfully opened
        file.close()


#! Bad practice
# except ValueError:
#     print("Please enter a valid age")
# except ZeroDivisionError:
#     print("Please enter a valid age")
